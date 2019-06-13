# coding:utf-8
import logging
import numpy as np
from ctypes import CDLL
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from pweight import utils
from pweight.dbs import api as db_api
logger = logging.getLogger('pweight')


class WeightThread(QThread):
    steady_weight_signal = pyqtSignal(int, name='weight')

    def __init__(self, conf_path):
        super(WeightThread, self).__init__()
        self.history = []
        self.history_size = 4
        self.last_steady = 0
        self.interval = 0.12
        self.var_threshold = 5
        self.avr_threshold = 50
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))
        self.SCK_PORT = 15
        self.DT_PORT = 16
        self.libweight = CDLL("./clib/libweight.so")
        if self.libweight.init_weight(self.DT_PORT, self.SCK_PORT)!=0:
            logger.info("init weight error.")
        else:
            logger.info("init weight ok.")

    def check_steady(self):
        weight = self.libweight.get_weight()
        self.history.append(weight)
        if len(self.history) < self.history_size:
            return False
        elif len(self.history) > self.history_size:
            self.history.pop(0)
        avr = int(np.mean(self.history))
        var = np.var(self.history)
        if var < self.var_threshold:
            if abs(avr-self.last_steady) < self.avr_threshold:
                return False
            else:
                self.last_steady = avr
                if avr < self.avr_threshold:
                    return False
                else:
                    return True

    def run(self):
        while True:
            if self.check_steady() and self.db_api.get_device_status() in ['continue_weight', 'idle']:
                self.db_api.update_device_status('running')
                task_id = utils.generate_uuid()
                logger.info("new task id generate %s" % task_id)
                self.db_api.update_device_task_id(task_id)
                self.steady_weight_signal.emit(self.last_steady)
            self.msleep(150)


# w = Weight()
# w.start_worker()


