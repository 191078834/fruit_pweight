# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recognition_result.ui'
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

class Ui_RecognitionResult(object):
    def setupUi(self, RecognitionResult):
        RecognitionResult.setObjectName(_fromUtf8("RecognitionResult"))
        RecognitionResult.setEnabled(True)
        RecognitionResult.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        RecognitionResult.setFont(font)
        RecognitionResult.setAutoFillBackground(False)
        RecognitionResult.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        RecognitionResult.setDocumentMode(True)
        RecognitionResult.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(RecognitionResult)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image_3 = QtGui.QPushButton(self.centralwidget)
        self.image_3.setEnabled(True)
        self.image_3.setGeometry(QtCore.QRect(716, 223, 279, 279))
        self.image_3.setText(_fromUtf8(""))
        self.image_3.setCheckable(True)
        self.image_3.setAutoDefault(True)
        self.image_3.setFlat(True)
        self.image_3.setObjectName(_fromUtf8("image_3"))
        self.image_4 = QtGui.QPushButton(self.centralwidget)
        self.image_4.setEnabled(True)
        self.image_4.setGeometry(QtCore.QRect(63, 579, 279, 279))
        self.image_4.setStyleSheet(_fromUtf8(""))
        self.image_4.setText(_fromUtf8(""))
        self.image_4.setCheckable(True)
        self.image_4.setAutoDefault(True)
        self.image_4.setFlat(True)
        self.image_4.setObjectName(_fromUtf8("image_4"))
        self.image_5 = QtGui.QPushButton(self.centralwidget)
        self.image_5.setEnabled(True)
        self.image_5.setGeometry(QtCore.QRect(390, 579, 279, 279))
        self.image_5.setText(_fromUtf8(""))
        self.image_5.setCheckable(True)
        self.image_5.setAutoDefault(True)
        self.image_5.setFlat(True)
        self.image_5.setObjectName(_fromUtf8("image_5"))
        self.image_6 = QtGui.QPushButton(self.centralwidget)
        self.image_6.setEnabled(True)
        self.image_6.setGeometry(QtCore.QRect(716, 579, 279, 279))
        self.image_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.image_6.setText(_fromUtf8(""))
        self.image_6.setCheckable(True)
        self.image_6.setAutoDefault(True)
        self.image_6.setFlat(True)
        self.image_6.setObjectName(_fromUtf8("image_6"))
        self.image_1_name = QtGui.QLabel(self.centralwidget)
        self.image_1_name.setGeometry(QtCore.QRect(63, 519, 279, 40))
        self.image_1_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_1_name.setText(_fromUtf8(""))
        self.image_1_name.setObjectName(_fromUtf8("image_1_name"))
        self.image_2_name = QtGui.QLabel(self.centralwidget)
        self.image_2_name.setGeometry(QtCore.QRect(387, 519, 279, 40))
        self.image_2_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_2_name.setText(_fromUtf8(""))
        self.image_2_name.setObjectName(_fromUtf8("image_2_name"))
        self.image_3_name = QtGui.QLabel(self.centralwidget)
        self.image_3_name.setGeometry(QtCore.QRect(716, 519, 279, 40))
        self.image_3_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_3_name.setText(_fromUtf8(""))
        self.image_3_name.setObjectName(_fromUtf8("image_3_name"))
        self.image_4_name = QtGui.QLabel(self.centralwidget)
        self.image_4_name.setGeometry(QtCore.QRect(63, 874, 279, 40))
        self.image_4_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_4_name.setText(_fromUtf8(""))
        self.image_4_name.setObjectName(_fromUtf8("image_4_name"))
        self.image_5_name = QtGui.QLabel(self.centralwidget)
        self.image_5_name.setGeometry(QtCore.QRect(390, 874, 279, 40))
        self.image_5_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_5_name.setText(_fromUtf8(""))
        self.image_5_name.setObjectName(_fromUtf8("image_5_name"))
        self.image_6_name = QtGui.QLabel(self.centralwidget)
        self.image_6_name.setGeometry(QtCore.QRect(716, 874, 279, 40))
        self.image_6_name.setStyleSheet(_fromUtf8("font: 21pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.image_6_name.setText(_fromUtf8(""))
        self.image_6_name.setObjectName(_fromUtf8("image_6_name"))
        self.page_last = QtGui.QPushButton(self.centralwidget)
        self.page_last.setEnabled(True)
        self.page_last.setGeometry(QtCore.QRect(61, 948, 228, 74))
        self.page_last.setStyleSheet(_fromUtf8("font: 25pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 255);"))
        self.page_last.setFlat(False)
        self.page_last.setObjectName(_fromUtf8("page_last"))
        self.page_next = QtGui.QPushButton(self.centralwidget)
        self.page_next.setEnabled(True)
        self.page_next.setGeometry(QtCore.QRect(769, 947, 228, 74))
        self.page_next.setAutoFillBackground(False)
        self.page_next.setStyleSheet(_fromUtf8("font: 25pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 255);"))
        self.page_next.setAutoDefault(False)
        self.page_next.setDefault(False)
        self.page_next.setFlat(False)
        self.page_next.setObjectName(_fromUtf8("page_next"))
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 1920, 96))
        self.label_title.setText(_fromUtf8(""))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.button_home = QtGui.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(1668, 13, 215, 70))
        self.button_home.setText(_fromUtf8(""))
        self.button_home.setFlat(True)
        self.button_home.setObjectName(_fromUtf8("button_home"))
        self.label_notice = QtGui.QLabel(self.centralwidget)
        self.label_notice.setGeometry(QtCore.QRect(62, 151, 500, 45))
        self.label_notice.setStyleSheet(_fromUtf8("font: 30pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.label_notice.setObjectName(_fromUtf8("label_notice"))
        self.choice_name = QtGui.QLabel(self.centralwidget)
        self.choice_name.setGeometry(QtCore.QRect(380, 151, 201, 45))
        self.choice_name.setStyleSheet(_fromUtf8("font: 30pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 62, 62);"))
        self.choice_name.setText(_fromUtf8(""))
        self.choice_name.setObjectName(_fromUtf8("choice_name"))
        self.image_1 = QtGui.QPushButton(self.centralwidget)
        self.image_1.setEnabled(True)
        self.image_1.setGeometry(QtCore.QRect(63, 223, 279, 279))
        self.image_1.setText(_fromUtf8(""))
        self.image_1.setCheckable(True)
        self.image_1.setAutoDefault(True)
        self.image_1.setFlat(True)
        self.image_1.setObjectName(_fromUtf8("image_1"))
        self.image_2 = QtGui.QPushButton(self.centralwidget)
        self.image_2.setEnabled(True)
        self.image_2.setGeometry(QtCore.QRect(387, 221, 279, 279))
        self.image_2.setText(_fromUtf8(""))
        self.image_2.setCheckable(True)
        self.image_2.setAutoDefault(True)
        self.image_2.setFlat(True)
        self.image_2.setObjectName(_fromUtf8("image_2"))
        self.background_label = QtGui.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(1032, 219, 820, 639))
        self.background_label.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"\n"
""))
        self.background_label.setText(_fromUtf8(""))
        self.background_label.setObjectName(_fromUtf8("background_label"))
        self.weight_text = QtGui.QLabel(self.centralwidget)
        self.weight_text.setGeometry(QtCore.QRect(1330, 358, 361, 111))
        self.weight_text.setStyleSheet(_fromUtf8("font: 60pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
"\n"
""))
        self.weight_text.setObjectName(_fromUtf8("weight_text"))
        self.weight = QtGui.QLabel(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(1121, 500, 651, 241))
        self.weight.setStyleSheet(_fromUtf8("font: 125pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
"\n"
""))
        self.weight.setText(_fromUtf8(""))
        self.weight.setObjectName(_fromUtf8("weight"))
        self.unit_price_1 = QtGui.QLabel(self.centralwidget)
        self.unit_price_1.setGeometry(QtCore.QRect(63, 223, 160, 33))
        self.unit_price_1.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_1.setText(_fromUtf8(""))
        self.unit_price_1.setObjectName(_fromUtf8("unit_price_1"))
        self.unit_price_2 = QtGui.QLabel(self.centralwidget)
        self.unit_price_2.setGeometry(QtCore.QRect(387, 221, 160, 33))
        self.unit_price_2.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_2.setText(_fromUtf8(""))
        self.unit_price_2.setObjectName(_fromUtf8("unit_price_2"))
        self.unit_price_3 = QtGui.QLabel(self.centralwidget)
        self.unit_price_3.setGeometry(QtCore.QRect(716, 223, 160, 33))
        self.unit_price_3.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_3.setText(_fromUtf8(""))
        self.unit_price_3.setObjectName(_fromUtf8("unit_price_3"))
        self.unit_price_4 = QtGui.QLabel(self.centralwidget)
        self.unit_price_4.setGeometry(QtCore.QRect(63, 579, 160, 33))
        self.unit_price_4.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_4.setText(_fromUtf8(""))
        self.unit_price_4.setObjectName(_fromUtf8("unit_price_4"))
        self.unit_price_5 = QtGui.QLabel(self.centralwidget)
        self.unit_price_5.setGeometry(QtCore.QRect(390, 579, 160, 33))
        self.unit_price_5.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_5.setText(_fromUtf8(""))
        self.unit_price_5.setObjectName(_fromUtf8("unit_price_5"))
        self.unit_price_6 = QtGui.QLabel(self.centralwidget)
        self.unit_price_6.setGeometry(QtCore.QRect(716, 579, 160, 33))
        self.unit_price_6.setStyleSheet(_fromUtf8("color: rgb(255, 252, 0);\n"
"background-color: rgb(208, 69, 0);\n"
"font: 19pt \"微软雅黑\";\n"
"border-bottom-right-radius: 25px"))
        self.unit_price_6.setText(_fromUtf8(""))
        self.unit_price_6.setObjectName(_fromUtf8("unit_price_6"))
        RecognitionResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecognitionResult)
        QtCore.QMetaObject.connectSlotsByName(RecognitionResult)

    def retranslateUi(self, RecognitionResult):
        RecognitionResult.setWindowTitle(_translate("RecognitionResult", "智能电子称", None))
        self.page_last.setText(_translate("RecognitionResult", "上一页", None))
        self.page_next.setText(_translate("RecognitionResult", "下一页", None))
        self.label_notice.setText(_translate("RecognitionResult", "请选择商品种类", None))
        self.weight_text.setText(_translate("RecognitionResult", "重量(g)", None))

