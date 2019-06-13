#!/usr/bin/python
# -*- coding: utf-8 -*-
# Auther: WQM
# Time: 2019/1/4 10:14
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui, Qt
from pweight.qt_gui.ui.mesgbox import Ui_MesgBox
from PIL import Image, ImageFont, ImageDraw, ImageQt
from pweight import utils
import pdb
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
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

class MesgBox(QtGui.QWidget, Ui_MesgBox):

    def __init__(self, conf_path):
        # QtGui.QWidget.__init__(self)
        # Ui_MesgBox.__init__(self)
        # self.setupUi(self)
        # self.conf_path = conf_path
        # self.img_path = utils.get_static_images_path(conf_path, 'message_name')
        # self.size_font_path = utils.get_conf_value(conf_path, 'size_font', 'size_font_path')
        # self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.background_button.clicked.connect(self.hide_button)
        QtGui.QWidget.__init__(self)
        Ui_MesgBox.__init__(self)
        self.setupUi(self)
        self.conf_path = conf_path
        self.img_path = utils.get_static_images_path(conf_path, 'image_message_name')
        self.size_font_path = utils.get_conf_value(conf_path, 'size_font', 'size_font_path')
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.hide_button.clicked.connect(self.close_message_box)
        #self.center()

    # def close_message_box(self):
    #     self.hide()

    def network_fail(self):
        # pdb.set_trace()
        im = Image.open(self.img_path)
        im = im.convert('RGBA')
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.size_font_path, size=60)
        text1 = "SORRY当前网络连接失败"
        text2 = "请联系管理员操作"
        draw.text((600, 590), text1.decode('utf-8'), fill=(0, 0, 0), font=font)
        draw.text((600, 650), text2.decode('utf-8'), fill=(0, 0, 0), font=font)
        #im.resize((1920, 1080))
        fruit_img = ImageQt.ImageQt(im)
        qimg = QtGui.QImage(fruit_img)
        fruit_img = QtGui.QPixmap.fromImage(qimg)
        pixmap = QtGui.QPixmap(fruit_img)
        scaredPixmap = pixmap.scaled(1920, 1080, QtCore.Qt.IgnoreAspectRatio)
        self.background_img.setPixmap(scaredPixmap)
        # icon = QtGui.QIcon()
        # icon.addPixmap(scaredPixmap, QtGui.QIcon.Normal,
        #                QtGui.QIcon.On)
        # self.background_img.setIcon(icon)
        # self.background_img.setIconSize(QtCore.QSize(1920, 1080))

    def create_order_fail(self):
        im = Image.open(self.img_path)
        im = im.convert('RGBA')
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.size_font_path, size=60, index=0)
        text1 = "SORRY当前订单创建失败"
        text2 = "请您稍后重试"
        draw.text((600, 590), text1.decode('utf-8'), fill=(0, 0, 0), font=font)
        draw.text((600, 650), text2.decode('utf-8'), fill=(0, 0, 0), font=font)
        # im.resize((1920, 1080))
        fruit_img = ImageQt.ImageQt(im)
        qimg = QtGui.QImage(fruit_img)
        fruit_img = QtGui.QPixmap.fromImage(qimg)
        pixmap = QtGui.QPixmap(fruit_img)
        scaredPixmap = pixmap.scaled(1920, 1080, QtCore.Qt.IgnoreAspectRatio)
        self.background_img.setPixmap(scaredPixmap)
        # icon.addPixmap(scaredPixmap, QtGui.QIcon.Normal,
        #                QtGui.QIcon.On)
        # self.background_img.setIcon(icon)
        # self.background_img.setIconSize(QtCore.QSize(1920, 1080))

    # def center(self):  # 实现窗体在屏幕中央
    #     screen = QtGui.QDesktopWidget().screenGeometry()  # QDesktopWidget为一个类，调用screenGeometry函数获得屏幕的尺寸
    #     size = self.geometry()  # 同上
    #     self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
