#!/usr/bin/python
# coding:utf-8
import cv2
from pweight import weight
from pweight import utils
from pweight import http_client
from pweight import printer
from pweight import camara
from pweight.balance_screen import BalanceScreen
from PyQt4.QtGui import QMovie
from pweight.dbs import api as db_api
import sys
import time
import logging
logger = logging.getLogger('pweight')


class Photos(object):
    def __init__(self):
        # self.led = led.Led(38, 40, 36)
        # 初始化界面
        self.conf_path = sys.argv[2]
        self.db_api = db_api.DBApi(
            utils.get_conf_value(
                self.conf_path, 'db', 'db_path'))
        self.db_api.create_tables(
            utils.get_conf_value(self.conf_path,'default','device_id'))
        self.save_image_base_path = utils.get_conf_value(
            self.conf_path, 'cache_fruits_images', 'save_image_base_path')
        self.logger_init()
        self.screen = BalanceScreen(self.conf_path)
        self.http_client = http_client.HttpClient()
        self.capture_thread = camara.CaptureThread(self.save_image_base_path)
        self.weight_thread = weight.WeightThread(self.conf_path)
        self.weight_thread.steady_weight_signal.connect(
            self.steady_weight_callback)
        self.http_client.signal_identify_goods_resp.connect(
            self.get_identify_resp)

    def steady_weight_callback(self, steady_weight):
        logger.info("Weight is steady %s g" % steady_weight)
        if self.screen.procedure_dialog.practice_mode:
            frame = self.capture_thread.get_one_frame()
            cur_str_time = time.strftime("%Y%m%d%H%M%S")
            current_timestamp = self.screen.procedure_dialog.file_path
            file_path = self.capture_thread.save_image_to_file(
                frame,cur_str_time +'.jpg', current_timestamp,return_path=True)
            # 更新界面图像
            self.screen.procedure_dialog.shop_image.setStyleSheet(
                "QLabel{background-image: url(%s)}" % file_path)
            self.screen.procedure_dialog.if_success.setText('')
            logger.info("take photo finished.")
            self.db_api.update_device_status('idle')
        else:
            self.screen.procedure_dialog.show_recogniting_ui()
            req_id = self.db_api.get_device_req_id()
            task_id = utils.generate_uuid()
            self.db_api.insert_task(
                {'id': task_id, 'reqId': req_id, 'status': 'taking_photo'})
            self.db_api.update_device_task_id(task_id)
            image = self.capture_thread.take_one_photo()
            self.db_api.update_task_status(task_id, 'identifying')
            self.http_client.set_info([image], steady_weight)
            self.http_client.start()
            logger.info("take photo finished.")

    def get_identify_resp(self, identify_resp, weight):
        req_id = self.db_api.get_device_req_id()
        task_id = self.db_api.get_device_task_id()

        self.db_api.update_task_identified_info(task_id,
                                                identify_resp.record_id,
                                                identify_resp.code,
                                                identify_resp.msg,
                                                weight)
        if identify_resp.code == 0:
            logger.info("identified code 0.")
            for fruit in identify_resp.results:
                fruit['id'] = utils.generate_uuid()
                fruit['reqId'] = req_id
                fruit['taskId'] = task_id
                fruit['recordId'] = identify_resp.record_id
                self.db_api.insert_fruit(fruit)
            # 切换到展示识别结果界面
            self.screen.recognition_result_win.update(weight)
            self.screen.procedure_dialog.delay_hide(
                self.screen.recognition_result_win)
        else:
            # 日志记录识别失败
            logger.warn("Identity interface response code not 0.")
            # 切换到识别失败界面
            self.screen.procedure_dialog.show_unidentified_ui()
            self.db_api.update_task_status(task_id, 'unidentified')
            self.db_api.update_device_status('idle')

    def logger_init(self):
        logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler(
            utils.get_conf_value(
                self.conf_path,
                'default',
                'log_file'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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

        self.screen.procedure_dialog.show()
        # 启动界面
        self.screen.mainloop()


p = Photos()
p.manager()
