#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtCore import QTime, QTimer
from pweight import printer
from pweight.qt_gui.ui.pay_ui import Ui_Pay
from pweight import utils
from pweight.dbs import api as db_api
from pweight import http_client
# from pweight.http_client import Raw_print
import logging
import os
logger = logging.getLogger('pweight')

ALI_PAY = 1
WECHAT_PAY = 2

WAITING_PAYMENT = 1
DELAYED_TO_GUIDE = 2
DELAYED_TO_HIDE = 3

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


class Pay_way(QtGui.QWidget, Ui_Pay):
    def __init__(self, conf_path, procedure_dialog, mesgbox):
        QtGui.QWidget.__init__(self)
        Ui_Pay.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.procedure_dialog = procedure_dialog
        # self.qrcode_str_qthread = GetInputQrcodeStr()
        # self.qrcode_str_qthread.signal_qrcodestr_resp.connect(self.get_qrcode_str_fun)
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))
        self.status = 0
        self.pay_way = 0
        self.order_info = { }
        self.mesgbox = mesgbox
        self.label_title.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_title_name'))
        self.button_home.setStyleSheet(
            "QPushButton{background-image: url(%s)}" %
            utils.get_static_images_path(conf_path, 'image_home_name'))
        self.image_success_path = utils.get_static_images_path(conf_path, 'image_success_name')
        self.pay_notice_bg.setStyleSheet("QLabel{border-image: url(%s)}" %
             utils.get_static_images_path(conf_path, 'pay_tip_name'))
        self.pay_notice_bg.show()
        self.image_fail_path = utils.get_static_images_path(conf_path, 'image_fail_name')
        self.image_wechat_background_path = utils.get_static_images_path(conf_path, 'image_wechat_background_name')
        # self.image_alipay_background_path = utils.get_static_images_path(conf_path, 'image_alipay_background_name')
        self.label_success.hide()
        self.conf_path = conf_path
        self.pay_timeout = int(utils.get_conf_value(conf_path, 'pay', 'timeout'))
        self.delayed_to_guide_timeout = int(utils.get_conf_value(conf_path, 'pay', 'delayed_to_guide_timeout'))
        self.time_count = 0
        self.timer_print = QTimer()
        self.timer_print.timeout.connect(self.print_goods)
        self.timer_task = WAITING_PAYMENT
        self.label_time.setAlignment(QtCore.Qt.AlignRight)
        self.printer = printer.ReceiptPrinter()
        self.qrcode_str = ''
        logger.info("Printer initialization finished.")
        # 获取二维码字符串
        self.timer_qrcode = QTimer()
        self.timer_qrcode.timeout.connect(self.get_qrcode)
        self.lineEdit.textChanged.connect(self.onChanged)
        self.label_time.hide()

    def onChanged(self):  #
        self.qrcode_str = str(unicode(self.lineEdit.text()).encode('utf-8'))
        if len(self.qrcode_str)>=18:
            self.timer_qrcode.start(300)

    def get_qrcode(self):
        self.lineEdit.clearFocus()
        self.timer_qrcode.stop()
        qrcode_str_type = utils.judge_qr_code(self.qrcode_str)
        self.order_info = self.create_order(qrcode_type=qrcode_str_type)
        if self.order_info is None:
            return 1
        self.time_count = 0
        self.timer_task = WAITING_PAYMENT
        # self.timer.start(1000)
        self.timer_handler()


    def create_order(self, qrcode_type):
        # 0 error  1 ali 2 Wechat
        device_req_id = self.db_api.get_device_req_id()
        selected_fruits_list = self.db_api.get_selected_fruits_by_req_id(device_req_id)
        fruits_record_id = [selected_fruit.recordId for selected_fruit in selected_fruits_list]
        order_info = http_client.create_order(fruits_record_id)
        if order_info:
            order_info['id'] = order_info['orderNo']
            order_info['reqId'] = device_req_id
            order_info['pay_way'] = str(qrcode_type)
            self.db_api.insert_order(order_info)
            self.label_time.setText(_translate("Dialog", "", None))
            # self.label_code.show()
            # self.label_bg.show()

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
        return order_info

    def wechat_pay_update(self):
        self.label_success.hide()
        self.pay_notice_bg.show()
        self.show()
        self.qrcode_str = ''
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        task_id = self.db_api.get_device_task_id()
        self.db_api.update_task_status(task_id, 'paying')
        logger.info('waiting user to pay.')
        # self.qrcode_str_qthread.start()

    def get_payment_status(self):
        if self.order_info:
            # 查询订单状态
            status = http_client.get_order_info(self.order_info['orderNo'], self.qrcode_str)
            # 订单状态更新到数据库
            self.db_api.update_order_status(self.order_info['orderNo'], status)
            logger.info('Order %(orderNo)s status is %(status)s',
                         {'orderNo': self.order_info['orderNo'], 'status': status})
            # 如果订单支付成功
            if status == 1:
                self.success_pay()
                self.timer_print.start(300)
                self.timer_task = DELAYED_TO_GUIDE
                self.order_info = None
                self.time_count = 0
            else:
                self.timeout_pay()
                self.timer_task = DELAYED_TO_GUIDE
                self.order_info = None
                self.time_count = 0

    def timer_handler(self):
        # self.time_count += 1
        self.get_payment_status()
        # if self.timer_task == WAITING_PAYMENT:
        #     self.label_time.setText(_translate("Dialog", str(self.pay_timeout - self.time_count) + 's', None))
        #     self.label_time.show()
        # if self.timer_task == DELAYED_TO_GUIDE:
        #     if self.time_count >= self.delayed_to_guide_timeout:
        #         logger.info('DELAYED_TO_GUIDE finished.')
        #         # self.timer.stop()
        #         self.timer_task = DELAYED_TO_HIDE
        #         self.timer.start(300)
        #         self.procedure_dialog.show_guide_ui()
        # elif self.timer_task == DELAYED_TO_HIDE:
        #         logger.info('Hide pat_paw dialog finished.')
        #         # self.timer.stop()
        #         self.hide()


    def print_goods(self):
        self.timer_print.stop()
        req_id = self.db_api.get_device_req_id()
        selected_fruits = self.db_api.get_selected_fruits_by_req_id(req_id)
        # get order info
        order = self.db_api.get_order_by_req_id(req_id)
        self.printer.print_order(order, selected_fruits)
        logger.info("Print receipt page finished.")
        new_req_id = utils.generate_uuid()
        self.db_api.update_device_req_id(new_req_id)
        logger.info("New req id generate %s" % new_req_id)
        self.db_api.update_device_status('idle')
        logger.info('User has payed, change device status to idle.')

    def success_pay(self):
        self.pay_notice_bg.hide()
        # self.label_time.hide()
        self.label_success.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            self.image_success_path)
        self.label_success.show()

    def timeout_pay(self):
        # 支付超时
        # self.label_time.hide()
        self.pay_notice_bg.hide()
        # self.label_code.hide()
        # self.label_bg.hide()
        self.label_success.setStyleSheet(
            "QLabel{border-image: url(%s)}" %
            self.image_fail_path)
        self.label_success.show()
        task_id = self.db_api.get_device_task_id()
        self.db_api.update_task_status(task_id, 'payment_timeout')

        req_id = utils.generate_uuid()
        logger.info("new req id generate %s" % req_id)
        self.db_api.update_device_req_id(req_id)

        self.db_api.update_device_status('idle')
        logger.info('timeout waiting user pay, change device status to idle.')

