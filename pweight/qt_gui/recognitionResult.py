#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auther: WQM
# Time: 2019/1/3 13:47
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui, Qt
from PyQt4.QtCore import QTimer
from pweight.qt_gui.ui.recognition_result import Ui_RecognitionResult
from pweight import http_client
from pweight import utils
from pweight.dbs import api as db_api
from PyQt4.QtGui import QPixmap
import logging
import os
import time
from PIL import Image, ImageFont, ImageDraw, ImageQt
reload(sys)
sys.setdefaultencoding('utf-8')
logger = logging.getLogger('pweight')

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


class RecognitionResultWindow(QtGui.QMainWindow, Ui_RecognitionResult):
    def __init__(self, conf_path, next_dialog, procedure_dialog, mesgbox):
        QtGui.QMainWindow.__init__(self)
        Ui_RecognitionResult.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.next_dialog = next_dialog
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))
        self.procedure_dialog = procedure_dialog
        self.cache_fruit_images_path = utils.get_conf_value(conf_path, 'cache_fruits_images', 'cache_fruit_images_path')
        self.wait_confirm_timeout = int(utils.get_conf_value(conf_path, 'recognition_result', 'timeout'))
        self.confirmed_info_timeout = int(utils.get_conf_value(conf_path,
                                                               'recognition_result',
                                                               'confirmed_info_timeout'))
        self.mesgbox = mesgbox
        self.label_title.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_title_name'))
        self.button_home.setStyleSheet(
            "QPushButton{background-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_home_name'))
        self.confirm_fruit_path = utils.get_static_images_path(
            conf_path, 'confirm_name')
        # self.image_unit_price_bg_path = utils.get_static_images_path(
        #     conf_path, 'image_unit_price_bg')

        self.image_1.clicked.connect(self.image_onclick1)
        self.image_2.clicked.connect(self.image_onclick2)
        self.image_3.clicked.connect(self.image_onclick3)
        self.image_4.clicked.connect(self.image_onclick4)
        self.image_5.clicked.connect(self.image_onclick5)
        self.image_6.clicked.connect(self.image_onclick6)

        self.index = 0
        self.fruits = []
        self.image_list = []
        self.image_list.append(self.image_1)
        self.image_list.append(self.image_2)
        self.image_list.append(self.image_3)
        self.image_list.append(self.image_4)
        self.image_list.append(self.image_5)
        self.image_list.append(self.image_6)

        self.image_name_list = []
        self.image_name_list.append(self.image_1_name)
        self.image_name_list.append(self.image_2_name)
        self.image_name_list.append(self.image_3_name)
        self.image_name_list.append(self.image_4_name)
        self.image_name_list.append(self.image_5_name)
        self.image_name_list.append(self.image_6_name)

        self.unit_price_list = []
        self.unit_price_list.append(self.unit_price_1)
        self.unit_price_list.append(self.unit_price_2)
        self.unit_price_list.append(self.unit_price_3)
        self.unit_price_list.append(self.unit_price_4)
        self.unit_price_list.append(self.unit_price_5)
        self.unit_price_list.append(self.unit_price_6)

        self.set_label_text_alignment()

        self.page_next.clicked.connect(self.page_next_onclick)
        self.page_last.clicked.connect(self.page_last_onclick)

        self.timeout_timer = QTimer()
        self.timeout_timer.timeout.connect(self.timeout_handler)
        self.timer = QTimer()
        self.timer.timeout.connect(self.hide_recognition)
        self.setStyleSheet("QPushButton{outline: none}")

    def timeout_handler(self):
        self.timeout_timer.stop()
        self.next_dialog.update()
        self.next_dialog.show()
        self.timer.start(200)

    def hide_recognition(self):
        self.timer.stop()
        self.hide()

    def set_label_text_alignment(self):
        for i in self.image_name_list:
            i.setAlignment(QtCore.Qt.AlignCenter)
        for i in self.unit_price_list:
            i.setAlignment(QtCore.Qt.AlignCenter)
        self.weight.setAlignment(QtCore.Qt.AlignCenter)

    def set_imagebutton_disable(self, goods_name):
        for butt in self.image_list:
            butt.setEnabled(False)
        self.label_notice.setText(
            _translate(
                "RecognitionResult",
                '您选择的商品为',
                None))
        self.choice_name.setText(
            _translate(
                "RecognitionResult", goods_name, None))

    def set_imagebutton_enable(self):
        for butt in self.image_list:
            butt.setEnabled(True)
    @utils.func_timer
    def confirm_fruit(self, selected):
        self.timeout_timer.stop()
        confirm_resp = http_client.confirm_goods(selected.recordId, selected.goodsId)
        if confirm_resp:
            self.set_imagebutton_disable(confirm_resp.results['goodsName'])
            # self.to_show_fruits_info(confirm_resp.results)
            self.db_api.confirm_fruit(selected.id, confirm_resp.results)
            self.db_api.select_fruit(selected.id)
            self.timeout_timer.start(3000)
        else:
            task_id = self.db_api.get_device_task_id()
            self.db_api.update_task_status(task_id, 'network_disconnection')

            req_id = utils.generate_uuid()
            logger.info("new req id generate %s" % req_id)
            self.db_api.update_device_req_id(req_id)

            self.db_api.update_device_status('idle')
            logger.info('network_disconnection, change device status to idle.')
            if not os.system('ping -c 5 -i 0.2 baidu.com'):
                logger.error('Failed to create order.')
                self.mesgbox.create_order_fail()
                self.mesgbox.show()
            else:
                logger.error('network connect to Failed ')
                self.mesgbox.network_fail()
                self.mesgbox.show()

    def image_onclick1(self):
        self.select_fruits_status(self.image_1, self.fruits[self.index * 6])
        self.confirm_fruit(self.fruits[self.index * 6])

    def image_onclick2(self):
        self.select_fruits_status(self.image_2, self.fruits[self.index * 6 + 1])
        self.confirm_fruit(self.fruits[self.index * 6 + 1])

    def image_onclick3(self):
        self.select_fruits_status(self.image_3, self.fruits[self.index * 6 + 2])
        self.confirm_fruit(self.fruits[self.index * 6 + 2])

    def image_onclick4(self):
        self.select_fruits_status(self.image_4, self.fruits[self.index * 6 + 3])
        self.confirm_fruit(self.fruits[self.index * 6 + 3])

    def image_onclick5(self):
        self.select_fruits_status(self.image_5, self.fruits[self.index * 6 + 4])
        self.confirm_fruit(self.fruits[self.index * 6 + 4])

    def image_onclick6(self):
        self.select_fruits_status(self.image_6, self.fruits[self.index * 6 + 5])
        self.confirm_fruit(self.fruits[self.index * 6 + 5])

    def clear_fruit_info(self):
        self.label_notice.setText(
            _translate(
                "RecognitionResult",
                '请选择商品种类',
                None))
        self.choice_name.setText(
            _translate(
                "RecognitionResult", '', None))
        self.weight.setText(
            _translate(
                "RecognitionResult", '', None))
        for image_name in self.image_name_list:
            image_name.setText(
            _translate(
                "RecognitionResult", '', None))
        self.index = 0

    def to_show_fruits_info(self, weight):
        self.weight.setText(
            _translate(
                "RecognitionResult", str(
                    weight), None))

    def page_next_onclick(self):
        self.index += 1
        next_fruits = self.fruits[self.index * 6:]
        for i in range(6):
            if i < len(next_fruits):
                self.scaredPixmap_button_image(self.image_list[i], next_fruits[i])
                self.image_name_list[i].show()
                self.unit_price_list[i].show()
                self.image_name_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        next_fruits[i].goodsName,
                        None))
                self.unit_price_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        next_fruits[i].price,
                        None))
            else:
                self.image_list[i].hide()
                self.unit_price_list[i].hide()
                self.image_name_list[i].hide()
        if len(next_fruits) > 6:
            self.page_next.show()
        else:
            self.page_next.hide()
        self.page_last.show()

    def page_last_onclick(self):
        self.index -= 1
        if self.index == 0:
            self.page_last.hide()
        last_fruits = self.fruits[self.index * 6:]
        for i in range(6):
            if i < len(last_fruits):
                self.image_list[i].show()
                self.image_name_list[i].show()
                self.unit_price_list[i].show()
                self.scaredPixmap_button_image(self.image_list[i], last_fruits[i])
                self.image_name_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        last_fruits[i].goodsName,
                        None))
                self.unit_price_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        last_fruits[i].price,
                        None))
        self.page_next.show()

    def update(self, weight):
        self.clear_fruit_info()
        self.show()
        self.next_dialog.hide()
        task_id = self.db_api.get_device_task_id()
        fruits = self.db_api.get_fruits_by_task_id(task_id)
        self.fruits = fruits
        self.to_show_fruits_info(weight)
        self.set_imagebutton_enable()
        for i in range(6):
            if i < len(fruits):
                self.image_list[i].show()
                self.image_name_list[i].show()
                self.unit_price_list[i].show()
                self.scaredPixmap_button_image(self.image_list[i], self.fruits[i])
                self.image_name_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        fruits[i].goodsName,
                        None))
                self.unit_price_list[i].setText(
                    _translate(
                        "RecognitionResult",
                        fruits[i].price
                        ,
                        None))
            else:
                self.image_list[i].hide()
                self.unit_price_list[i].hide()
                self.image_name_list[i].hide()
        # 缓存选中图片
        self.cache_select_fruit_image(self.fruits)
        if len(fruits) > 6:
            self.page_next.show()
            self.page_last.hide()
        else:
            self.page_next.hide()
            self.page_last.hide()

        self.db_api.update_task_status(task_id, 'confirming')
        logger.info('set task %s status to confirming.' % task_id)
        # self.timeout_timer.start(self.wait_confirm_timeout*1000)

    def scaredPixmap_button_image(self, image_button, fruit):
        local_img = utils.set_cache_fruits_image_path(
            fruit.goodsId, fruit.imgUrl, self.cache_fruit_images_path)
        image_button.setStyleSheet("QPushButton{background-image: url(%s)}" % local_img)

        # icon = QtGui.QIcon()
        # pixmap = QtGui.QPixmap(local_img)
        # scaredPixmap = pixmap.scaled(279, 279, QtCore.Qt.IgnoreAspectRatio)
        # icon.addPixmap(scaredPixmap, QtGui.QIcon.Normal,
        #                QtGui.QIcon.Off)
        # image_button.setIcon(icon)
        # image_button.setIconSize(QtCore.QSize(279, 279))

    @utils.func_timer
    def select_fruits_status(self, image_button, fruit):
        path = self.cache_fruit_images_path + str(fruit.goodsId) + '.png'
        if os.path.exists(path):
            pass
        else:
            local_img = utils.set_cache_fruits_image_path(
                fruit.goodsId, fruit.imgUrl, self.cache_fruit_images_path)
            pil_img = utils.blend_image(local_img, self.confirm_fruit_path)
            pil_img.save(path)
        image_button.setStyleSheet("QPushButton{border-image: url(%s)}" % path)
        # icon = QtGui.QIcon()
        # fruit_img = ImageQt.ImageQt(new_img)
        # qimg = QtGui.QImage(fruit_img)
        # fruit_img = QtGui.QPixmap.fromImage(qimg)
        # pixmap = QtGui.QPixmap(fruit_img)
        # scaredPixmap = pixmap.scaled(279, 279, QtCore.Qt.IgnoreAspectRatio)
        # icon.addPixmap(scaredPixmap, QtGui.QIcon.Normal,
        #                QtGui.QIcon.On)
        # image_button.setIcon(icon)
        # image_button.setIconSize(QtCore.QSize(279, 279))

    @utils.func_timer
    def cache_select_fruit_image(self, fruits):
        for fruit in fruits:
            local_img = utils.set_cache_fruits_image_path(
                fruit.goodsId, fruit.imgUrl, self.cache_fruit_images_path)
            pil_img = utils.blend_image(local_img, self.confirm_fruit_path)
            path =self.cache_fruit_images_path + str(fruit.goodsId) + '.png'
            pil_img.save(path)

