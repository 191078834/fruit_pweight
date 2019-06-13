#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auther: WQM
# Time: 2019/1/4 10:14

from PyQt4 import QtCore
from PyQt4 import QtGui, Qt
from PyQt4.QtCore import QTimer
from pweight.qt_gui.ui.shopping_cart_ui import Ui_ShoppingCart
from pweight import utils
from pweight.dbs import api as db_api
import logging
from PyQt4.QtGui import QPixmap
from decimal import *
getcontext().prec = 4

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


class ShoppingCart(QtGui.QWidget, Ui_ShoppingCart):
    def __init__(self, conf_path, procedure_dialog, pay_way_dialog):
        QtGui.QWidget.__init__(self)
        Ui_ShoppingCart.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))
        self.procedure_dialog = procedure_dialog
        self.pay_way_dialog = pay_way_dialog

        self.label_title.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_title_name'))
        self.button_home.setStyleSheet(
            "QPushButton{background-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_home_name'))
        self.puchase_logo.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_shopping_cart_logo_name'))
        # self.to_recognition_button.setStyleSheet(
        #     "QPushButton{border-image: url(%s)}" %
        #     utils.get_static_images_path(conf_path, 'image_to_recognition_name'))
        # self.wechat_pay_button.setStyleSheet(
        #     "QPushButton{border-image: url(%s)}" %
        #     utils.get_static_images_path(conf_path, 'image_wechatpay_name'))
        # self.alipay_button.setStyleSheet(
        #     "QPushButton{border-image: url(%s)}" %
        #     utils.get_static_images_path(conf_path, 'image_Alipay_name'))
        self.to_recognition_image_path = utils.get_static_images_path(conf_path, 'image_to_recognition_name')
        self.set_button_icon(self.to_recognition_button, self.to_recognition_image_path)
        self.wechat_image_path = utils.get_static_images_path(conf_path, 'image_wechatpay_name')
        self.set_button_icon(self.wechat_pay_button, self.wechat_image_path)
        # self.alipay_image_path = utils.get_static_images_path(conf_path, 'image_Alipay_name')
        # self.set_button_icon(self.alipay_button, self.alipay_image_path)
        
        self.wechat_pay_button.setCheckable(False)
        # self.alipay_button.setCheckable(False)
        self.to_recognition_button.setCheckable(False)
        self.to_recognition_button.setStyleSheet("QPushButton{border:none}")
        # self.alipay_button.setDefault(False)
        self.wechat_pay_button.setDefault(False)
        # self.wechat_pay_button.setStyleSheet("QPushbutton{outline: none}")
        # self.to_recognition_button.setStyleSheet("QPushbutton{outline: none}")
        # self.to_recognition_button.setStyleSheet("QPushbutton{outline: none}")
        self.blue_background_img = utils.get_static_images_path(conf_path, 'image_blue_back')
        self.image_unselected = utils.get_static_images_path(conf_path, 'image_unselected_name')
        self.image_selected = utils.get_static_images_path(conf_path, 'image_selected_name')
        self.cache_fruit_images_path = utils.get_conf_value(conf_path, 'cache_fruits_images', 'cache_fruit_images_path')

        self.index = 0
        self.Total_price = 0.0
        self.fruits = []
        self.selected_button_list = []
        self.selected_button_list.append(self.selected_button1)
        self.selected_button_list.append(self.selected_button2)
        self.selected_button_list.append(self.selected_button3)
        self.selected_button_list.append(self.selected_button4)
        self.selected_button_list.append(self.selected_button5)
        for butt in self.selected_button_list:
            butt.setStyleSheet(
                "QPushButton{border-image: url(%s)}" %
                self.image_selected)
            butt.setCheckable(True)

        self.fruit_info_names_list = []
        self.fruit_info_names_list.append(self.fruit_name_1)
        self.fruit_info_names_list.append(self.fruit_name_2)
        self.fruit_info_names_list.append(self.fruit_name_3)
        self.fruit_info_names_list.append(self.fruit_name_4)
        self.fruit_info_names_list.append(self.fruit_name_5)

        self.fruit_info_unit_price_list = []
        self.fruit_info_unit_price_list.append(self.fruit_unit_price_1)
        self.fruit_info_unit_price_list.append(self.fruit_unit_price_2)
        self.fruit_info_unit_price_list.append(self.fruit_unit_price_3)
        self.fruit_info_unit_price_list.append(self.fruit_unit_price_4)
        self.fruit_info_unit_price_list.append(self.fruit_unit_price_5)

        self.fruit_info_weight_list = []
        self.fruit_info_weight_list.append(self.fruit_weight_1)
        self.fruit_info_weight_list.append(self.fruit_weight_2)
        self.fruit_info_weight_list.append(self.fruit_weight_3)
        self.fruit_info_weight_list.append(self.fruit_weight_4)
        self.fruit_info_weight_list.append(self.fruit_weight_5)

        self.coin_list = []
        self.coin_list.append(self.coin_1)
        self.coin_list.append(self.coin_2)
        self.coin_list.append(self.coin_3)
        self.coin_list.append(self.coin_4)
        self.coin_list.append(self.coin_5)

        self.fruit_info_total_price_list = []
        self.fruit_info_total_price_list.append(self.fruit_total_price_1)
        self.fruit_info_total_price_list.append(self.fruit_total_price_2)
        self.fruit_info_total_price_list.append(self.fruit_total_price_3)
        self.fruit_info_total_price_list.append(self.fruit_total_price_4)
        self.fruit_info_total_price_list.append(self.fruit_total_price_5)

        self.fruit_image_list = []
        self.fruit_image_list.append(self.fruit_image1)
        self.fruit_image_list.append(self.fruit_image2)
        self.fruit_image_list.append(self.fruit_image3)
        self.fruit_image_list.append(self.fruit_image4)
        self.fruit_image_list.append(self.fruit_image5)
        self.selected_button1.clicked.connect(self.selected_onclick1)
        self.selected_button2.clicked.connect(self.selected_onclick2)
        self.selected_button3.clicked.connect(self.selected_onclick3)
        self.selected_button4.clicked.connect(self.selected_onclick4)
        self.selected_button5.clicked.connect(self.selected_onclick5)

        self.background_select_list = []
        self.background_select_list.append(self.label_background_1)
        self.background_select_list.append(self.label_background_2)
        self.background_select_list.append(self.label_background_3)
        self.background_select_list.append(self.label_background_4)
        self.background_select_list.append(self.label_background_5)
        self.label_background_1.clicked.connect(self.selected_onclick1)
        self.label_background_2.clicked.connect(self.selected_onclick2)
        self.label_background_3.clicked.connect(self.selected_onclick3)
        self.label_background_4.clicked.connect(self.selected_onclick4)
        self.label_background_5.clicked.connect(self.selected_onclick5)

        self.page_next.clicked.connect(self.page_next_onclick)
        self.page_last.clicked.connect(self.page_last_onclick)
        self.to_recognition_button.clicked.connect(self.to_guide_ui)
        self.wechat_pay_button.clicked.connect(self.wechat_pay)
        # self.alipay_button.clicked.connect(self.ali_pay)
        # self.dialog_delay = ''
        self.timeout_timer = QTimer()
        self.timeout_timer.timeout.connect(self.timeout_handler)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_handler)
        self.set_background_select_img()
        self.setStyleSheet("QPushButton{outline: none}")

    def set_background_select_img(self):
        for butt in  self.background_select_list:
            butt.setStyleSheet("QPushButton{border-image: url(%s)}" % self.blue_background_img)

    def timer_handler(self):
        self.timer.stop()
        self.hide()

    def timeout_handler(self):
        self.timeout_timer.stop()
        task_id = self.db_api.get_device_task_id()
        self.db_api.update_task_status(task_id, 'select_timeout')
        logger.warning('timeout waiting user select, return guide dialog now.')

        new_req_id = utils.generate_uuid()
        self.db_api.update_device_req_id(new_req_id)
        logger.info("new req id generate %s" % new_req_id)

        self.db_api.update_device_status('idle')
        logger.warning('update device status to idle.')

        self.procedure_dialog.show_guide_ui()
        self.timer.start(300)

    def to_guide_ui(self):
        # self.dialog_delay = 'guide_ui'
        logger.info('user want to continue weight fruits.')
        for fruit in self.fruits:
            self.db_api.update_fruit_info(fruit)
        logger.info('update fruits info to database finished.')
        self.db_api.update_device_status('continue_weight')
        logger.info('update device status to continue_weight.')
        self.timeout_timer.stop()
        self.procedure_dialog.show_guide_ui()
        self.timer.start(300)


    def wechat_pay(self):
        # self.dialog_delay = 'pay_way_ui'
        for fruit in self.fruits:
            self.db_api.update_fruit_info(fruit)
        self.pay_way_dialog.wechat_pay_update()
        # self.pay_way_dialog.show()
        # self.timeout_timer.stop()
        self.timer.start(300)

    # def ali_pay(self):
    #     # self.dialog_delay = 'pay_way_ui'
    #     for fruit in self.fruits:
    #         self.db_api.update_fruit_info(fruit)
    #     self.pay_way_dialog.ali_pay_update()
    #     # self.pay_way_dialog.show()
    #     # self.timeout_timer.stop()
    #     self.timer.start(300)

    def selected_onclick1(self):
        self.judging_choice(self.selected_button1, self.label_background_1, self.index * 5)

    def selected_onclick2(self):
        self.judging_choice(self.selected_button2, self.label_background_2, self.index * 5 + 1)

    def selected_onclick3(self):
        self.judging_choice(self.selected_button3, self.label_background_3, self.index * 5 + 2)

    def selected_onclick4(self):
        self.judging_choice(self.selected_button4, self.label_background_4, self.index * 5 + 3)

    def selected_onclick5(self):
        self.judging_choice(self.selected_button5, self.label_background_5, self.index * 5 + 4)

    def show_fruit_all_info(self, fruit, i):
        name = fruit.goodsName
        unit_price = fruit.price
        weight = str(fruit.weight) + 'g'
        total_price = str(float(fruit.total)/100)
        if len(name) > 18:
            name = name[:18] + '..'
        self.show_fruit_info(i)

        self.fruit_info_names_list[i].setText(_translate("Dialog", name, None))
        self.fruit_info_unit_price_list[i].setText(_translate("Dialog", unit_price, None))
        self.fruit_info_weight_list[i].setText(_translate("Dialog", weight, None))
        self.fruit_info_total_price_list[i].setText(_translate("Dialog", total_price, None))

    def hide_fruit_info(self, i):
        self.fruit_info_names_list[i].hide()
        self.fruit_info_unit_price_list[i].hide()
        self.fruit_info_weight_list[i].hide()
        self.coin_list[i].hide()
        self.fruit_info_total_price_list[i].hide()

    def show_fruit_info(self, i):
        self.fruit_info_names_list[i].show()
        self.fruit_info_unit_price_list[i].show()
        self.fruit_info_weight_list[i].show()
        self.coin_list[i].show()
        self.fruit_info_total_price_list[i].show()

    def show_total_price(self):
        self.label_total_price.setText(_translate(
            "Dialog", ' ' + str(self.Total_price/100), None))

    def update(self):
        self.index = 0
        req_id = self.db_api.get_device_req_id()
        task_id = self.db_api.get_device_task_id()
        self.fruits = self.db_api.get_confirmed_fruits_by_req_id(req_id)
        # self.alipay_button.setEnabled(True)
        self.wechat_pay_button.setEnabled(True)
        self.Total_price = 0
        for fruit in self.fruits:
            if fruit.selected:
                self.Total_price = Decimal(str(self.Total_price))+ Decimal(str(fruit.total))
        self.show_total_price()

        for i in range(5):
            if i < len(self.fruits):
                self.show_fruit_all_info(self.fruits[i], i)
                self.selected_button_list[i].show()
                self.fruit_image_list[i].show()
                self.judged_choice(
                    self.fruits[i], self.selected_button_list[i])
                self.set_fruit_image_path(self.fruits, i)
                # self.fruit_image_list[i].setStyleSheet("QPushButton{border-image: url(%s)}" % fruits[i]['imgUrl'])
            else:
                self.background_select_list[i].setEnabled(False)
                self.selected_button_list[i].hide()
                self.fruit_image_list[i].hide()
                self.hide_fruit_info(i)
        self.db_api.update_task_status(task_id, 'waiting_select')
        logger.info('screen update finished, waiting user select.')
        if len(self.fruits) > 5:
            self.page_next.show()
            self.page_last.hide()
        else:
            self.page_next.hide()
            self.page_last.hide()

    def page_next_onclick(self):
        self.index += 1
        next_fruits = self.fruits[self.index * 5:]
        for i in range(5):
            if i < len(next_fruits):
                self.selected_button_list[i].show()
                self.fruit_image_list[i].show()
                self.background_select_list[i].setEnabled(True)
                self.show_fruit_all_info(next_fruits[i], i)
                self.judged_choice(
                    next_fruits[i], self.selected_button_list[i])
                self.set_fruit_image_path(next_fruits, i)
            else:
                self.background_select_list[i].setEnabled(False)
                self.selected_button_list[i].hide()
                self.fruit_image_list[i].hide()
                self.hide_fruit_info(i)
        if len(next_fruits) > 5:
            self.page_next.show()
        else:
            self.page_next.hide()
        self.page_last.show()

    def page_last_onclick(self):
        self.index -= 1
        if self.index == 0:
            self.page_last.hide()
        last_fruits = self.fruits[self.index * 5:]
        for i in range(5):
            if i < len(last_fruits):
                self.judged_choice(
                    last_fruits[i], self.selected_button_list[i])
                self.background_select_list[i].setEnabled(True)
                self.selected_button_list[i].show()
                self.fruit_image_list[i].show()
                self.show_fruit_all_info(last_fruits[i], i)
                self.set_fruit_image_path(last_fruits, i)
        self.page_next.show()

    def judged_choice(self, fruit, button):
        if fruit.selected:
            button.setStyleSheet(
                "QPushButton{border-image: url(%s)}" %
                self.image_selected)
        else:
            button.setStyleSheet(
                "QPushButton{border-image: url(%s)}" %
                self.image_unselected)

    def judging_choice(self, button, button_label, fruit_index):
        if button.isChecked() or button_label.isChecked():
            if self.fruits[fruit_index].selected:
                self.fruits[fruit_index].selected = False
                button.setStyleSheet(
                    "QPushButton{border-image: url(%s)}" %
                    self.image_unselected)
                self.Total_price = Decimal(str(self.Total_price)) - Decimal(str(self.fruits[fruit_index].total))

            else:
                self.fruits[fruit_index].selected = True
                button.setStyleSheet(
                    "QPushButton{border-image: url(%s)}" %
                    self.image_selected)
                self.Total_price = Decimal(str(self.Total_price)) + Decimal(str(self.fruits[fruit_index].total))
        else:
            if not self.fruits[fruit_index].selected:
                self.fruits[fruit_index].selected = True
                button.setStyleSheet(
                    "QPushButton{border-image: url(%s)}" %
                    self.image_selected)
                self.Total_price = Decimal(str(self.Total_price)) + Decimal(str(self.fruits[fruit_index].total))
            else:
                self.fruits[fruit_index].selected = False
                button.setStyleSheet(
                    "QPushButton{border-image: url(%s)}" %
                    self.image_unselected)
                self.Total_price = Decimal(str(self.Total_price)) - Decimal(str(self.fruits[fruit_index].total))
        is_exist = []
        for fruit in self.fruits:
            is_exist.append(fruit.selected)
        if not True in is_exist:
            self.wechat_pay_button.setEnabled(False)
            # self.alipay_button.setEnabled(False)
        else:
            self.wechat_pay_button.setEnabled(True)
            # self.alipay_button.setEnabled(True)

        self.show_total_price()

    def set_fruit_image_path(self, fruits, i):
        pixmap = QPixmap(
            utils.set_cache_fruits_image_path(
                fruits[i].id,fruits[i].imgUrl, self.cache_fruit_images_path))
        scaredPixmap = pixmap.scaled(65, 65, QtCore.Qt.KeepAspectRatio)
        self.fruit_image_list[i].setScaledContents(True)
        self.fruit_image_list[i].setPixmap(scaredPixmap)

    def set_button_icon(self, button_name, image_path):
        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap(image_path)
        scaredPixmap = pixmap.scaled(677, 161, QtCore.Qt.IgnoreAspectRatio)
        icon.addPixmap(scaredPixmap, QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        button_name.setIcon(icon)
        button_name.setIconSize(QtCore.QSize(677, 161))


