#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auther: WQM
# Time: 2019/1/7 9:10
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
from pweight.qt_gui.pay_way import Pay_way
from pweight.qt_gui.recognitionResult import RecognitionResultWindow
from pweight.qt_gui.shopping_cart import ShoppingCart
from pweight.qt_gui.mesg_box import MesgBox
from pweight import utils
from pweight.qt_gui.procedure import Procedure
from pweight.dbs import api as db_api
import logging

logger = logging.getLogger('pweight')


class BalanceScreen(object):

    def __init__(self, conf_path):
        self.core_app = QtGui.QApplication(sys.argv)
        self.db_api = db_api.DBApi(utils.get_conf_value(conf_path, 'db', 'db_path'))
        self.procedure_dialog = Procedure(conf_path)
        self.mesg_box_dialog = MesgBox(conf_path)
        self.pay_way_dialog = Pay_way(conf_path, self.procedure_dialog, self.mesg_box_dialog)
        self.shopping_cart_dialog = ShoppingCart(conf_path, self.procedure_dialog, self.pay_way_dialog)
        self.recognition_result_win = RecognitionResultWindow(conf_path, self.shopping_cart_dialog,
                                                              self.procedure_dialog, self.mesg_box_dialog)

        self.recognition_result_win.button_home.clicked.connect(
            self.return_home)
        self.shopping_cart_dialog.button_home.clicked.connect(self.return_home)
        self.pay_way_dialog.button_home.clicked.connect(self.return_home)
        self.mesg_box_dialog.hide_button.clicked.connect(self.show_shopping_cart_hide_mesg)
        self.timeout_timer = QTimer()
        self.timeout_timer.timeout.connect(self.timeout_handler)

    def mainloop(self):
        sys.exit(self.core_app.exec_())

    def timeout_handler(self):
        self.timeout_timer.stop()
        self.recognition_result_win.hide()
        self.shopping_cart_dialog.hide()
        self.pay_way_dialog.hide()

    def show_shopping_cart_hide_mesg(self):
        self.shopping_cart_dialog.show()
        self.mesg_box_dialog.hide()

    def return_home(self):
        # self.hide_all_dialog()
        task_id = self.db_api.get_device_task_id()
        self.db_api.update_task_status(task_id, 'canceled')

        new_req_id = utils.generate_uuid()
        self.db_api.update_device_req_id(new_req_id)
        logger.info("new req id generate %s" % new_req_id)

        self.db_api.update_device_status('idle')

        self.procedure_dialog.show_guide_ui()
        self.recognition_result_win.timeout_timer.stop()
        self.pay_way_dialog.lineEdit.clearFocus()

        self.timeout_timer.start(300)

    def hide_all_dialog(self):
        self.procedure_dialog.hide()
        self.recognition_result_win.hide()
        self.shopping_cart_dialog.hide()
        self.pay_way_dialog.hide()
