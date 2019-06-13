# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pay_ui.ui'
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

class Ui_Pay(object):
    def setupUi(self, Pay):
        Pay.setObjectName(_fromUtf8("Pay"))
        Pay.resize(1920, 1080)
        Pay.setLayoutDirection(QtCore.Qt.RightToLeft)
        Pay.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_title = QtGui.QLabel(Pay)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 1920, 96))
        self.label_title.setText(_fromUtf8(""))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.label_time = QtGui.QLabel(Pay)
        self.label_time.setGeometry(QtCore.QRect(730, 868, 331, 190))
        self.label_time.setStyleSheet(_fromUtf8("color: rgb(171, 171, 171);\n"
"font: 115pt \"微软雅黑\";"))
        self.label_time.setText(_fromUtf8(""))
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.button_home = QtGui.QPushButton(Pay)
        self.button_home.setGeometry(QtCore.QRect(1668, 13, 215, 70))
        self.button_home.setText(_fromUtf8(""))
        self.button_home.setFlat(True)
        self.button_home.setObjectName(_fromUtf8("button_home"))
        self.pay_notice_bg = QtGui.QLabel(Pay)
        self.pay_notice_bg.setGeometry(QtCore.QRect(527, 234, 914, 846))
        self.pay_notice_bg.setStyleSheet(_fromUtf8(""))
        self.pay_notice_bg.setText(_fromUtf8(""))
        self.pay_notice_bg.setObjectName(_fromUtf8("pay_notice_bg"))
        self.label_success = QtGui.QLabel(Pay)
        self.label_success.setGeometry(QtCore.QRect(780, 230, 422, 482))
        self.label_success.setStyleSheet(_fromUtf8(""))
        self.label_success.setText(_fromUtf8(""))
        self.label_success.setObjectName(_fromUtf8("label_success"))
        self.lineEdit = QtGui.QLineEdit(Pay)
        self.lineEdit.setGeometry(QtCore.QRect(420, 40, 351, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.raise_()
        self.label_title.raise_()
        self.label_time.raise_()
        self.button_home.raise_()
        self.pay_notice_bg.raise_()
        self.label_success.raise_()

        self.retranslateUi(Pay)
        QtCore.QMetaObject.connectSlotsByName(Pay)

    def retranslateUi(self, Pay):
        Pay.setWindowTitle(_translate("Pay", "Dialog", None))

