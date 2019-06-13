# coding:utf-8
import Queue
import logging
import os
import threading
import time

import cv2
import sys
from pweight import led
from pweight import camara
from pweight import utils
from pweight import weight
from pweight.dbs import api as db_api
from PyQt4 import QtGui

logger = logging.getLogger('pweight')

DEVICE_NUMBER = "0001"

PHOTO_WIDTH = 800
PHOTO_HEIGHT = 600


class Photos(object):
    def __init__(self):
        self.conf_path = sys.argv[2]
        self.led = led.Led(38, 40, 36)
        self.led.blue(True)
        self.db_api = db_api.DBApi(utils.get_conf_value(self.conf_path, 'db', 'db_path'))
        self.db_api.update_device_status('idle')
        self.logger_init()
        self.capture_thread = camara.CaptureThread()
        self.weight_thread = weight.WeightThread(self.conf_path)
        self.weight_thread.steady_weight_signal.connect(self.steady_weight_callback)
        logger.info("Weight initialization finished.")

        cv2.namedWindow("AdjustCamera", 0)
        cv2.setWindowProperty("AdjustCamera", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

        logger.info("Video out is enabled, window created.")
        self.led.blue(False)

    def steady_weight_callback(self, weight):
        logger.info("Weight is steady %s g" % self.weight_thread.last_steady)
        frame = self.capture_thread.get_one_frame()
        cv2.imshow("AdjustCamera", frame)
        cur_str_time = time.strftime("%Y%m%d%H%M%S")
        self.capture_thread.save_image_to_file(frame, cur_str_time+'.jpg')
        logger.info("take photo finished.")
        self.db_api.update_device_status('idle')

    def logger_init(self):
        logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler(utils.get_conf_value(self.conf_path, 'default', 'log_file'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        logger.addHandler(handler)
        logger.addHandler(console)

        logger.info("Start print log")

    def manager(self):
        self.weight_thread.start()
        logger.info("Weight worker start.")

        self.capture_thread.start()
        logger.info("Video worker start.")

        screen = QtGui.QApplication(sys.argv)
        screen.exec_()

p = Photos()
p.manager()


