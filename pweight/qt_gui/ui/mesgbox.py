# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesgbox.ui'
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

class Ui_MesgBox(object):
    def setupUi(self, MesgBox):
        MesgBox.setObjectName(_fromUtf8("MesgBox"))
        MesgBox.resize(1920, 1080)
        self.hide_button = QtGui.QPushButton(MesgBox)
        self.hide_button.setGeometry(QtCore.QRect(800, 775, 400, 100))
        self.hide_button.setStyleSheet(_fromUtf8("font: 75 22pt \"微软雅黑\";\n"
"background-color: rgb(255, 170, 24);"))
        self.hide_button.setObjectName(_fromUtf8("hide_button"))
        self.background_img = QtGui.QLabel(MesgBox)
        self.background_img.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.background_img.setText(_fromUtf8(""))
        self.background_img.setObjectName(_fromUtf8("background_img"))
        self.background_img.raise_()
        self.hide_button.raise_()

        self.retranslateUi(MesgBox)
        QtCore.QMetaObject.connectSlotsByName(MesgBox)

    def retranslateUi(self, MesgBox):
        MesgBox.setWindowTitle(_translate("MesgBox", "Dialog", None))
        self.hide_button.setText(_translate("MesgBox", "我知道了", None))

