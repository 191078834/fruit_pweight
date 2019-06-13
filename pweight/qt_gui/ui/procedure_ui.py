# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'procedure_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Procedure(object):
    def setupUi(self, Procedure):
        Procedure.setObjectName(_fromUtf8("Procedure"))
        Procedure.resize(1920, 1080)
        self.change_status_label = QtGui.QLabel(Procedure)
        self.change_status_label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.change_status_label.setText(_fromUtf8(""))
        self.change_status_label.setObjectName(_fromUtf8("change_status_label"))
        self.advertisement_button = QtGui.QPushButton(Procedure)
        self.advertisement_button.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.advertisement_button.setText(_fromUtf8(""))
        self.advertisement_button.setFlat(False)
        self.advertisement_button.setObjectName(_fromUtf8("advertisement_button"))
        self.rec_button = QtGui.QPushButton(Procedure)
        self.rec_button.setGeometry(QtCore.QRect(988, 326, 820, 500))
        self.rec_button.setStyleSheet(_fromUtf8("background-color: rgb(253, 84, 0);\n"
"font: 36pt \"微软雅黑\";"))
        self.rec_button.setText(_fromUtf8(""))
        self.rec_button.setObjectName(_fromUtf8("rec_button"))
        self.pra_button = QtGui.QPushButton(Procedure)
        self.pra_button.setGeometry(QtCore.QRect(106, 326, 820, 499))
        self.pra_button.setStyleSheet(_fromUtf8("background-color: rgb(253, 84, 0);\n"
"font: 75 36pt \"微软雅黑\";"))
        self.pra_button.setText(_fromUtf8(""))
        self.pra_button.setObjectName(_fromUtf8("pra_button"))
        self.shop_image = QtGui.QLabel(Procedure)
        self.shop_image.setGeometry(QtCore.QRect(300, 200, 1000, 800))
        self.shop_image.setText(_fromUtf8(""))
        self.shop_image.setObjectName(_fromUtf8("shop_image"))
        self.change_shop_button = QtGui.QPushButton(Procedure)
        self.change_shop_button.setGeometry(QtCore.QRect(1440, 290, 371, 221))
        self.change_shop_button.setStyleSheet(_fromUtf8("background-color: rgb(253, 84, 0);\n"
"font: 75 36pt \"微软雅黑\";"))
        self.change_shop_button.setObjectName(_fromUtf8("change_shop_button"))
        self.return_choice_button = QtGui.QPushButton(Procedure)
        self.return_choice_button.setGeometry(QtCore.QRect(1440, 580, 371, 221))
        self.return_choice_button.setStyleSheet(_fromUtf8("background-color: rgb(253, 84, 0);\n"
"font: 75 36pt \"微软雅黑\";"))
        self.return_choice_button.setObjectName(_fromUtf8("return_choice_button"))
        self.if_success = QtGui.QLabel(Procedure)
        self.if_success.setGeometry(QtCore.QRect(1510, 900, 241, 111))
        self.if_success.setStyleSheet(_fromUtf8("font: 75 60pt \"微软雅黑\";\n"
""))
        self.if_success.setText(_fromUtf8(""))
        self.if_success.setObjectName(_fromUtf8("if_success"))

        self.retranslateUi(Procedure)
        QtCore.QMetaObject.connectSlotsByName(Procedure)

    def retranslateUi(self, Procedure):
        Procedure.setWindowTitle(_translate("Procedure", "Dialog", None))
        self.change_shop_button.setText(_translate("Procedure", "切换商品类型", None))
        self.return_choice_button.setText(_translate("Procedure", "返回识别界面", None))

