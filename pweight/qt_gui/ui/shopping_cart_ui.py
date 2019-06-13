# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shopping_cart_ui.ui'
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

class Ui_ShoppingCart(object):
    def setupUi(self, ShoppingCart):
        ShoppingCart.setObjectName(_fromUtf8("ShoppingCart"))
        ShoppingCart.resize(1920, 1080)
        ShoppingCart.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.to_recognition_button = QtGui.QPushButton(ShoppingCart)
        self.to_recognition_button.setGeometry(QtCore.QRect(166, 920, 677, 161))
        self.to_recognition_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.to_recognition_button.setText(_fromUtf8(""))
        self.to_recognition_button.setCheckable(True)
        self.to_recognition_button.setAutoDefault(False)
        self.to_recognition_button.setFlat(True)
        self.to_recognition_button.setObjectName(_fromUtf8("to_recognition_button"))
        self.page_last = QtGui.QPushButton(ShoppingCart)
        self.page_last.setGeometry(QtCore.QRect(511, 126, 206, 67))
        self.page_last.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 73, 255);"))
        self.page_last.setObjectName(_fromUtf8("page_last"))
        self.page_next = QtGui.QPushButton(ShoppingCart)
        self.page_next.setGeometry(QtCore.QRect(738, 126, 206, 67))
        self.page_next.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
"background-color: rgb(23, 73, 255);\n"
"color: rgb(255, 255, 255);"))
        self.page_next.setObjectName(_fromUtf8("page_next"))
        self.fruit_image1 = QtGui.QLabel(ShoppingCart)
        self.fruit_image1.setGeometry(QtCore.QRect(215, 247, 77, 77))
        self.fruit_image1.setText(_fromUtf8(""))
        self.fruit_image1.setObjectName(_fromUtf8("fruit_image1"))
        self.fruit_weight_1 = QtGui.QLabel(ShoppingCart)
        self.fruit_weight_1.setGeometry(QtCore.QRect(576, 269, 83, 37))
        self.fruit_weight_1.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 17pt \"楷体\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_weight_1.setText(_fromUtf8(""))
        self.fruit_weight_1.setObjectName(_fromUtf8("fruit_weight_1"))
        self.label_ma = QtGui.QLabel(ShoppingCart)
        self.label_ma.setGeometry(QtCore.QRect(972, 220, 885, 684))
        self.label_ma.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
""))
        self.label_ma.setText(_fromUtf8(""))
        self.label_ma.setObjectName(_fromUtf8("label_ma"))
        self.label_title = QtGui.QLabel(ShoppingCart)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 1920, 96))
        self.label_title.setText(_fromUtf8(""))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.fruit_image2 = QtGui.QLabel(ShoppingCart)
        self.fruit_image2.setGeometry(QtCore.QRect(215, 386, 77, 77))
        self.fruit_image2.setText(_fromUtf8(""))
        self.fruit_image2.setObjectName(_fromUtf8("fruit_image2"))
        self.fruit_image3 = QtGui.QLabel(ShoppingCart)
        self.fruit_image3.setGeometry(QtCore.QRect(215, 525, 77, 77))
        self.fruit_image3.setText(_fromUtf8(""))
        self.fruit_image3.setObjectName(_fromUtf8("fruit_image3"))
        self.fruit_image4 = QtGui.QLabel(ShoppingCart)
        self.fruit_image4.setGeometry(QtCore.QRect(215, 664, 77, 77))
        self.fruit_image4.setText(_fromUtf8(""))
        self.fruit_image4.setObjectName(_fromUtf8("fruit_image4"))
        self.label_heji = QtGui.QLabel(ShoppingCart)
        self.label_heji.setGeometry(QtCore.QRect(1343, 394, 171, 81))
        self.label_heji.setStyleSheet(_fromUtf8("font: 60pt \"微软雅黑\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.label_heji.setObjectName(_fromUtf8("label_heji"))
        self.label_total_price = QtGui.QLabel(ShoppingCart)
        self.label_total_price.setGeometry(QtCore.QRect(1320, 535, 471, 141))
        self.label_total_price.setStyleSheet(_fromUtf8("font: 108pt \"微软雅黑\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.label_total_price.setText(_fromUtf8(""))
        self.label_total_price.setObjectName(_fromUtf8("label_total_price"))
        self.label_6 = QtGui.QLabel(ShoppingCart)
        self.label_6.setGeometry(QtCore.QRect(1160, 580, 81, 76))
        self.label_6.setStyleSheet(_fromUtf8("\n"
"font: 68pt \"微软雅黑\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.fruit_image5 = QtGui.QLabel(ShoppingCart)
        self.fruit_image5.setGeometry(QtCore.QRect(215, 803, 77, 77))
        self.fruit_image5.setText(_fromUtf8(""))
        self.fruit_image5.setObjectName(_fromUtf8("fruit_image5"))
        self.wechat_pay_button = QtGui.QPushButton(ShoppingCart)
        self.wechat_pay_button.setGeometry(QtCore.QRect(1093, 920, 640, 161))
        self.wechat_pay_button.setStyleSheet(_fromUtf8("background-color: rgb(0, 56, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.wechat_pay_button.setText(_fromUtf8(""))
        self.wechat_pay_button.setCheckable(True)
        self.wechat_pay_button.setAutoDefault(False)
        self.wechat_pay_button.setFlat(True)
        self.wechat_pay_button.setObjectName(_fromUtf8("wechat_pay_button"))
        self.button_home = QtGui.QPushButton(ShoppingCart)
        self.button_home.setGeometry(QtCore.QRect(1668, 13, 215, 70))
        self.button_home.setText(_fromUtf8(""))
        self.button_home.setFlat(True)
        self.button_home.setObjectName(_fromUtf8("button_home"))
        self.puchase_logo = QtGui.QLabel(ShoppingCart)
        self.puchase_logo.setGeometry(QtCore.QRect(60, 128, 58, 55))
        self.puchase_logo.setText(_fromUtf8(""))
        self.puchase_logo.setObjectName(_fromUtf8("puchase_logo"))
        self.label_text = QtGui.QLabel(ShoppingCart)
        self.label_text.setGeometry(QtCore.QRect(141, 126, 191, 71))
        self.label_text.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 48pt \"微软雅黑\";\n"
"color: rgb(62, 62, 62);"))
        self.label_text.setObjectName(_fromUtf8("label_text"))
        self.selected_button1 = QtGui.QPushButton(ShoppingCart)
        self.selected_button1.setGeometry(QtCore.QRect(110, 261, 49, 49))
        self.selected_button1.setText(_fromUtf8(""))
        self.selected_button1.setObjectName(_fromUtf8("selected_button1"))
        self.selected_button2 = QtGui.QPushButton(ShoppingCart)
        self.selected_button2.setGeometry(QtCore.QRect(110, 400, 49, 49))
        self.selected_button2.setText(_fromUtf8(""))
        self.selected_button2.setObjectName(_fromUtf8("selected_button2"))
        self.selected_button3 = QtGui.QPushButton(ShoppingCart)
        self.selected_button3.setGeometry(QtCore.QRect(110, 539, 49, 49))
        self.selected_button3.setText(_fromUtf8(""))
        self.selected_button3.setObjectName(_fromUtf8("selected_button3"))
        self.selected_button4 = QtGui.QPushButton(ShoppingCart)
        self.selected_button4.setGeometry(QtCore.QRect(110, 678, 49, 49))
        self.selected_button4.setText(_fromUtf8(""))
        self.selected_button4.setObjectName(_fromUtf8("selected_button4"))
        self.selected_button5 = QtGui.QPushButton(ShoppingCart)
        self.selected_button5.setGeometry(QtCore.QRect(110, 817, 49, 49))
        self.selected_button5.setText(_fromUtf8(""))
        self.selected_button5.setObjectName(_fromUtf8("selected_button5"))
        self.fruit_name_1 = QtGui.QLabel(ShoppingCart)
        self.fruit_name_1.setGeometry(QtCore.QRect(323, 250, 220, 38))
        self.fruit_name_1.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"\n"
"font: 24pt \"微软雅黑\";"))
        self.fruit_name_1.setText(_fromUtf8(""))
        self.fruit_name_1.setObjectName(_fromUtf8("fruit_name_1"))
        self.fruit_unit_price_1 = QtGui.QLabel(ShoppingCart)
        self.fruit_unit_price_1.setGeometry(QtCore.QRect(324, 300, 150, 27))
        self.fruit_unit_price_1.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"color: rgb(153, 153, 153);\n"
"font: 14pt \"微软雅黑\";"))
        self.fruit_unit_price_1.setText(_fromUtf8(""))
        self.fruit_unit_price_1.setObjectName(_fromUtf8("fruit_unit_price_1"))
        self.fruit_total_price_1 = QtGui.QLabel(ShoppingCart)
        self.fruit_total_price_1.setGeometry(QtCore.QRect(770, 270, 142, 36))
        self.fruit_total_price_1.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 28pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_total_price_1.setText(_fromUtf8(""))
        self.fruit_total_price_1.setObjectName(_fromUtf8("fruit_total_price_1"))
        self.fruit_name_2 = QtGui.QLabel(ShoppingCart)
        self.fruit_name_2.setGeometry(QtCore.QRect(323, 389, 220, 38))
        self.fruit_name_2.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"font: 24pt \"微软雅黑\";"))
        self.fruit_name_2.setText(_fromUtf8(""))
        self.fruit_name_2.setObjectName(_fromUtf8("fruit_name_2"))
        self.fruit_name_3 = QtGui.QLabel(ShoppingCart)
        self.fruit_name_3.setGeometry(QtCore.QRect(323, 528, 220, 38))
        self.fruit_name_3.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"font: 24pt \"微软雅黑\";"))
        self.fruit_name_3.setText(_fromUtf8(""))
        self.fruit_name_3.setObjectName(_fromUtf8("fruit_name_3"))
        self.fruit_name_4 = QtGui.QLabel(ShoppingCart)
        self.fruit_name_4.setGeometry(QtCore.QRect(323, 667, 220, 38))
        self.fruit_name_4.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"font: 24pt \"微软雅黑\";"))
        self.fruit_name_4.setText(_fromUtf8(""))
        self.fruit_name_4.setObjectName(_fromUtf8("fruit_name_4"))
        self.fruit_name_5 = QtGui.QLabel(ShoppingCart)
        self.fruit_name_5.setGeometry(QtCore.QRect(323, 806, 220, 38))
        self.fruit_name_5.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"font: 24pt \"微软雅黑\";"))
        self.fruit_name_5.setText(_fromUtf8(""))
        self.fruit_name_5.setObjectName(_fromUtf8("fruit_name_5"))
        self.fruit_unit_price_2 = QtGui.QLabel(ShoppingCart)
        self.fruit_unit_price_2.setGeometry(QtCore.QRect(324, 439, 150, 27))
        self.fruit_unit_price_2.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"color: rgb(153, 153, 153);\n"
"font: 14pt \"微软雅黑\";"))
        self.fruit_unit_price_2.setText(_fromUtf8(""))
        self.fruit_unit_price_2.setObjectName(_fromUtf8("fruit_unit_price_2"))
        self.fruit_unit_price_3 = QtGui.QLabel(ShoppingCart)
        self.fruit_unit_price_3.setGeometry(QtCore.QRect(324, 578, 150, 27))
        self.fruit_unit_price_3.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"color: rgb(153, 153, 153);\n"
"font: 14pt \"微软雅黑\";"))
        self.fruit_unit_price_3.setText(_fromUtf8(""))
        self.fruit_unit_price_3.setObjectName(_fromUtf8("fruit_unit_price_3"))
        self.fruit_unit_price_4 = QtGui.QLabel(ShoppingCart)
        self.fruit_unit_price_4.setGeometry(QtCore.QRect(324, 717, 150, 27))
        self.fruit_unit_price_4.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"color: rgb(153, 153, 153);\n"
"font: 14pt \"微软雅黑\";"))
        self.fruit_unit_price_4.setText(_fromUtf8(""))
        self.fruit_unit_price_4.setObjectName(_fromUtf8("fruit_unit_price_4"))
        self.fruit_unit_price_5 = QtGui.QLabel(ShoppingCart)
        self.fruit_unit_price_5.setGeometry(QtCore.QRect(324, 856, 150, 27))
        self.fruit_unit_price_5.setStyleSheet(_fromUtf8("background-color: rgb(174, 220, 246);\n"
"color: rgb(153, 153, 153);\n"
"font: 14pt \"微软雅黑\";"))
        self.fruit_unit_price_5.setText(_fromUtf8(""))
        self.fruit_unit_price_5.setObjectName(_fromUtf8("fruit_unit_price_5"))
        self.fruit_weight_2 = QtGui.QLabel(ShoppingCart)
        self.fruit_weight_2.setGeometry(QtCore.QRect(576, 408, 83, 37))
        self.fruit_weight_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 17pt \"楷体\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_weight_2.setText(_fromUtf8(""))
        self.fruit_weight_2.setObjectName(_fromUtf8("fruit_weight_2"))
        self.fruit_weight_3 = QtGui.QLabel(ShoppingCart)
        self.fruit_weight_3.setGeometry(QtCore.QRect(576, 547, 83, 37))
        self.fruit_weight_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 17pt \"楷体\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_weight_3.setText(_fromUtf8(""))
        self.fruit_weight_3.setObjectName(_fromUtf8("fruit_weight_3"))
        self.fruit_weight_4 = QtGui.QLabel(ShoppingCart)
        self.fruit_weight_4.setGeometry(QtCore.QRect(576, 686, 83, 37))
        self.fruit_weight_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 17pt \"楷体\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_weight_4.setText(_fromUtf8(""))
        self.fruit_weight_4.setObjectName(_fromUtf8("fruit_weight_4"))
        self.fruit_weight_5 = QtGui.QLabel(ShoppingCart)
        self.fruit_weight_5.setGeometry(QtCore.QRect(576, 825, 83, 37))
        self.fruit_weight_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 75 17pt \"楷体\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_weight_5.setText(_fromUtf8(""))
        self.fruit_weight_5.setObjectName(_fromUtf8("fruit_weight_5"))
        self.fruit_total_price_2 = QtGui.QLabel(ShoppingCart)
        self.fruit_total_price_2.setGeometry(QtCore.QRect(770, 406, 142, 36))
        self.fruit_total_price_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 28pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_total_price_2.setText(_fromUtf8(""))
        self.fruit_total_price_2.setObjectName(_fromUtf8("fruit_total_price_2"))
        self.fruit_total_price_3 = QtGui.QLabel(ShoppingCart)
        self.fruit_total_price_3.setGeometry(QtCore.QRect(770, 545, 142, 36))
        self.fruit_total_price_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 28pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_total_price_3.setText(_fromUtf8(""))
        self.fruit_total_price_3.setObjectName(_fromUtf8("fruit_total_price_3"))
        self.fruit_total_price_4 = QtGui.QLabel(ShoppingCart)
        self.fruit_total_price_4.setGeometry(QtCore.QRect(770, 684, 142, 36))
        self.fruit_total_price_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 28pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_total_price_4.setText(_fromUtf8(""))
        self.fruit_total_price_4.setObjectName(_fromUtf8("fruit_total_price_4"))
        self.fruit_total_price_5 = QtGui.QLabel(ShoppingCart)
        self.fruit_total_price_5.setGeometry(QtCore.QRect(770, 823, 142, 36))
        self.fruit_total_price_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 28pt \"微软雅黑\";\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.fruit_total_price_5.setText(_fromUtf8(""))
        self.fruit_total_price_5.setObjectName(_fromUtf8("fruit_total_price_5"))
        self.coin_1 = QtGui.QLabel(ShoppingCart)
        self.coin_1.setGeometry(QtCore.QRect(745, 274, 21, 36))
        self.coin_1.setStyleSheet(_fromUtf8("font: 18pt \"楷体\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
""))
        self.coin_1.setObjectName(_fromUtf8("coin_1"))
        self.coin_2 = QtGui.QLabel(ShoppingCart)
        self.coin_2.setGeometry(QtCore.QRect(745, 410, 21, 36))
        self.coin_2.setStyleSheet(_fromUtf8("font: 18pt \"楷体\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.coin_2.setObjectName(_fromUtf8("coin_2"))
        self.coin_3 = QtGui.QLabel(ShoppingCart)
        self.coin_3.setGeometry(QtCore.QRect(745, 549, 21, 36))
        self.coin_3.setStyleSheet(_fromUtf8("font: 18pt \"楷体\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.coin_3.setObjectName(_fromUtf8("coin_3"))
        self.coin_4 = QtGui.QLabel(ShoppingCart)
        self.coin_4.setGeometry(QtCore.QRect(745, 688, 21, 36))
        self.coin_4.setStyleSheet(_fromUtf8("font: 18pt \"楷体\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.coin_4.setObjectName(_fromUtf8("coin_4"))
        self.coin_5 = QtGui.QLabel(ShoppingCart)
        self.coin_5.setGeometry(QtCore.QRect(745, 827, 21, 36))
        self.coin_5.setStyleSheet(_fromUtf8("font: 18pt \"楷体\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(174, 220, 246);\n"
"\n"
"\n"
""))
        self.coin_5.setObjectName(_fromUtf8("coin_5"))
        self.label_background_1 = QtGui.QPushButton(ShoppingCart)
        self.label_background_1.setGeometry(QtCore.QRect(60, 222, 885, 128))
        self.label_background_1.setText(_fromUtf8(""))
        self.label_background_1.setFlat(True)
        self.label_background_1.setObjectName(_fromUtf8("label_background_1"))
        self.label_background_2 = QtGui.QPushButton(ShoppingCart)
        self.label_background_2.setGeometry(QtCore.QRect(60, 360, 885, 128))
        self.label_background_2.setText(_fromUtf8(""))
        self.label_background_2.setFlat(True)
        self.label_background_2.setObjectName(_fromUtf8("label_background_2"))
        self.label_background_3 = QtGui.QPushButton(ShoppingCart)
        self.label_background_3.setGeometry(QtCore.QRect(60, 498, 885, 128))
        self.label_background_3.setText(_fromUtf8(""))
        self.label_background_3.setFlat(True)
        self.label_background_3.setObjectName(_fromUtf8("label_background_3"))
        self.label_background_4 = QtGui.QPushButton(ShoppingCart)
        self.label_background_4.setGeometry(QtCore.QRect(60, 637, 885, 128))
        self.label_background_4.setText(_fromUtf8(""))
        self.label_background_4.setFlat(True)
        self.label_background_4.setObjectName(_fromUtf8("label_background_4"))
        self.label_background_5 = QtGui.QPushButton(ShoppingCart)
        self.label_background_5.setGeometry(QtCore.QRect(60, 776, 885, 128))
        self.label_background_5.setText(_fromUtf8(""))
        self.label_background_5.setFlat(True)
        self.label_background_5.setObjectName(_fromUtf8("label_background_5"))
        self.label_background_5.raise_()
        self.label_background_4.raise_()
        self.label_background_3.raise_()
        self.label_background_2.raise_()
        self.label_background_1.raise_()
        self.to_recognition_button.raise_()
        self.page_last.raise_()
        self.page_next.raise_()
        self.fruit_image1.raise_()
        self.fruit_weight_1.raise_()
        self.label_ma.raise_()
        self.label_title.raise_()
        self.fruit_image2.raise_()
        self.fruit_image3.raise_()
        self.fruit_image4.raise_()
        self.label_heji.raise_()
        self.label_total_price.raise_()
        self.label_6.raise_()
        self.fruit_image5.raise_()
        self.wechat_pay_button.raise_()
        self.button_home.raise_()
        self.puchase_logo.raise_()
        self.label_text.raise_()
        self.selected_button1.raise_()
        self.selected_button2.raise_()
        self.selected_button3.raise_()
        self.selected_button4.raise_()
        self.selected_button5.raise_()
        self.fruit_name_1.raise_()
        self.fruit_unit_price_1.raise_()
        self.fruit_total_price_1.raise_()
        self.fruit_name_2.raise_()
        self.fruit_name_3.raise_()
        self.fruit_name_4.raise_()
        self.fruit_name_5.raise_()
        self.fruit_unit_price_2.raise_()
        self.fruit_unit_price_3.raise_()
        self.fruit_unit_price_4.raise_()
        self.fruit_unit_price_5.raise_()
        self.fruit_weight_2.raise_()
        self.fruit_weight_3.raise_()
        self.fruit_weight_4.raise_()
        self.fruit_weight_5.raise_()
        self.fruit_total_price_2.raise_()
        self.fruit_total_price_3.raise_()
        self.fruit_total_price_4.raise_()
        self.fruit_total_price_5.raise_()
        self.coin_1.raise_()
        self.coin_2.raise_()
        self.coin_3.raise_()
        self.coin_4.raise_()
        self.coin_5.raise_()

        self.retranslateUi(ShoppingCart)
        QtCore.QMetaObject.connectSlotsByName(ShoppingCart)

    def retranslateUi(self, ShoppingCart):
        ShoppingCart.setWindowTitle(_translate("ShoppingCart", "Dialog", None))
        self.page_last.setText(_translate("ShoppingCart", "上一页", None))
        self.page_next.setText(_translate("ShoppingCart", "下一页", None))
        self.label_heji.setText(_translate("ShoppingCart", "总价", None))
        self.label_6.setText(_translate("ShoppingCart", " ¥", None))
        self.label_text.setText(_translate("ShoppingCart", "购物车", None))
        self.coin_1.setText(_translate("ShoppingCart", "¥", None))
        self.coin_2.setText(_translate("ShoppingCart", "¥", None))
        self.coin_3.setText(_translate("ShoppingCart", "¥", None))
        self.coin_4.setText(_translate("ShoppingCart", "¥", None))
        self.coin_5.setText(_translate("ShoppingCart", "¥", None))

