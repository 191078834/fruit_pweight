#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auther: WQM
# Time: 2019/1/5 22:06
IMAGES_DIR = '/home/pweight/images'

from PyQt4 import QtGui, Qt, QtCore
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QMovie
from pweight.qt_gui.ui.procedure_ui import Ui_Procedure
from pweight import utils
from pweight.dbs import api as db_api
from pweight.http_client import UploadImage
from PyQt4.QtCore import pyqtSignal
import time
import logging
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


logger = logging.getLogger('pweight')


class Procedure(QtGui.QWidget, Ui_Procedure):

    def __init__(self, conf_path):
        QtGui.QWidget.__init__(self)
        Ui_Procedure.__init__(self)
        self.setupUi(self)
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))

        self.image_advertisement_path = utils.get_static_images_path(conf_path, 'image_advisediment_name')
        self.image_advertisement_path_other = utils.get_static_images_path(conf_path, 'image_advisediment_name2')
        self.image_guide_path = utils.get_static_images_path(conf_path, 'image_guide_name')
        self.image_recogniting_path = utils.get_static_images_path(conf_path, 'image_recogniting_name')
        self.image_unidentified_path = utils.get_static_images_path(conf_path, 'image_unidentified_name')

        self.guide_timeout = int(utils.get_conf_value(conf_path, 'guide', 'timeout'))
        self.unidentified_timeout = int(utils.get_conf_value(conf_path, 'unidentified', 'timeout'))

        self.rec_sys_path = utils.get_static_images_path(conf_path, 'rec_sys_name')
        self.pra_sys_path = utils.get_static_images_path(conf_path, 'pra_sys_name')
        self.save_image_base_path = utils.get_conf_value(
            conf_path, 'cache_fruits_images', 'save_image_base_path')
        self.pra_button.setStyleSheet(
            "QPushButton{border-image: url(%s)}" %
            self.pra_sys_path)
        self.rec_button.setStyleSheet(
            "QPushButton{border-image: url(%s)}" %
            self.rec_sys_path)

        self.advertisement_movie = QMovie(self.image_advertisement_path)
        self.guide_movie = QMovie(self.image_guide_path)
        self.recogniting_movie = QMovie(self.image_recogniting_path)
        self.unidentified_movie = QMovie(self.image_unidentified_path) 

        self.advertisement_button.clicked.connect(self.show_guide_ui)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.running_dialog = ''
        self.timeout_timer = QTimer()
        self.timeout_timer.timeout.connect(self.timeout_handler)

        self.image_choice_system_path = utils.get_static_images_path(conf_path, 'image_logo_name')
        self.pra_button.clicked.connect(self.show_praitce_dialog)
        self.rec_button.clicked.connect(self.show_advertisment_ui)
        self.return_choice_button.clicked.connect(self.upload_cloud)
        self.choice_system()
        self.change_shop_button.clicked.connect(self.show_praitce_dialog)
        self.file_path = ''
        self.practice_mode = False
        self.qthread = UploadImage(self.save_image_base_path)
        self.qthread.signal_upload_resp.connect(self.set_if_success_label)
        self.setStyleSheet("QPushButton{outline: none}")

    def set_if_success_label(self, is_or_not):
        if is_or_not:
            self.if_success.setText(
                _translate(
                    "RecognitionResult", '成功', None))
        else:
            self.if_success.setText(
                _translate(
                    "RecognitionResult", '失败', None))

    def choice_system(self):
        self.show()
        self.shop_image.hide()
        self.change_shop_button.hide()
        self.return_choice_button.hide()
        self.advertisement_button.hide()
        self.gif = QMovie(self.image_choice_system_path)
        self.change_status_label.setMovie(self.gif)
        self.gif.start()
        self.if_success.setText('')
        # self.change_status_label.setStyleSheet(
        #     "QPushButton{background-image: url(%s)}" %
        #     self.image_choice_system_path)
        self.change_status_label.show()

    def upload_cloud(self):
        lists_folder = os.listdir(self.save_image_base_path)
        for folder in lists_folder:
            if os.path.isdir(self.save_image_base_path + folder):
                self.qthread.set_folder_name(folder)
                self.qthread.start()
                self.qthread.wait()
        self.timeout_timer.start(2000)
        self.running_dialog ='advertisment'


    def timeout_handler(self):
        self.timeout_timer.stop()
        if self.running_dialog == 'guide':
            logger.warning('%s seconds, timeout waiting user to weight, '
                           'return advertisement dialog.' % self.guide_timeout)
            req_id = utils.generate_uuid()
            logger.info("new req id generate %s" % req_id)
            self.db_api.update_device_req_id(req_id)
            self.show_advertisment_ui()
        elif self.running_dialog == 'advertisment':
            self.show_advertisment_ui()
        elif self.running_dialog == 'unidentified':
            logger.info('%s seconds, identified failed notice finished.' % self.unidentified_timeout)
            self.show_guide_ui()
        else:
            self.hide()

    def show_praitce_dialog(self):
        self.pra_button.hide()
        self.rec_button.hide()
        self.shop_image.show()
        self.return_choice_button.show()
        self.change_shop_button.show()
        self.if_success.setText(
            _translate(
                "RecognitionResult", '', None))
        self.practice_mode = True
        self.file_path = str(time.time())
        if not os.path.exists(self.save_image_base_path):
            os.makedirs(self.save_image_base_path)
        lists_folder = os.listdir(self.save_image_base_path)
        for folder in lists_folder:
            if os.path.isdir(self.save_image_base_path + folder):
                self.qthread.set_folder_name(folder)
                self.qthread.start()
                self.qthread.wait()

    def show_advertisment_ui(self):
        self.if_success.hide()
        self.practice_mode = False
        self.hide_button_show_procedure()
        self.advertisement_button.show()
        self.change_status_label.hide()
        self.advertisement_button.setStyleSheet(
            "QPushButton{border-image: url(%s)}" %
            self.image_advertisement_path)
        req_id = utils.generate_uuid()
        logger.info("new req id generate %s" % req_id)
        self.db_api.update_device_req_id(req_id)

    def show_guide_ui(self):
        self.hide_button_show_procedure()
        self.change_status_label.setMovie(self.guide_movie)
        self.guide_movie.start()
        self.change_status_label.show()
        self.advertisement_button.hide()
        self.running_dialog = 'guide'
        self.timeout_timer.start(self.guide_timeout*1000)

    def show_recogniting_ui(self):
        self.hide_button_show_procedure()
        self.timeout_timer.stop()
        self.change_status_label.setMovie(self.recogniting_movie)
        self.recogniting_movie.start()
        self.change_status_label.show()
        self.advertisement_button.hide()
        self.running_dialog = 'recogniting'

    def delay_hide(self, recognition_result_win):
        self.running_dialog = 'recognited'
        recognition_result_win.show()
        self.timeout_timer.start(300)

    def show_unidentified_ui(self):
        self.hide_button_show_procedure()
        task_id = self.db_api.get_device_task_id()
        self.db_api.update_task_status(task_id, 'unidentified')
        self.change_status_label.setMovie(self.unidentified_movie)
        self.unidentified_movie.start()
        self.change_status_label.show()
        self.advertisement_button.hide()
        self.running_dialog = 'unidentified'
        self.timeout_timer.start(self.guide_timeout*1000)

    def hide_button_show_procedure(self):
        self.show()
        self.shop_image.hide()
        self.pra_button.hide()
        self.rec_button.hide()
        self.return_choice_button.hide()
        self.change_shop_button.hide()

