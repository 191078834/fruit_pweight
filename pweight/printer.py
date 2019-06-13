#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import re
import serial
import time
import logging

logger = logging.getLogger('pweight')

SERIAL_ID = 'usb-1a86_USB2.0-Serial-if00-port0'

CHAR_SET_12X24 = 0
CHAR_SET_9X17 = 1
CHAR_ON_TOP = 1
CHAR_ON_BOTTOM = 2
BAR_NO_CHAR = 0
BAR_CODE_EAN13 = 67
BAR_CODE_SIZE = 12

CODE_EAN13 = 2

PAGE_START_X = 0
PAGE_START_Y = 0
PAGE_WIDTH = 384
PAGE_HEIGHT = 218


class LabelPrinter(object):
    def __init__(self, dev_name='/dev/serial/by-id/'+SERIAL_ID, bond_rate=115200):
        self.serial = serial.Serial(dev_name, bond_rate)
        logger.info('serial port opened.')
        self.bar_width = 2
        self.bar_height = 60
        self.bar_charset = CHAR_SET_9X17
        self.bar_char_pos = CHAR_ON_BOTTOM
        self.bar_code_type = BAR_CODE_EAN13
        self.bar_code_size = BAR_CODE_SIZE
        self.command = []

    def serial_write(self, command):
        if not self.serial.isOpen():
            self.serial.open()
        self.serial.write(command)
        self.serial.close()

    def clear(self):
        command = [0x1B, 0x40]
        self.serial_write(command)
        logger.info("Printer clear finished.")

    def bar_code(self, code_str, white_rows=1):
        self.command.append(0x1d)
        self.command.append(0x77)
        self.command.append(self.bar_width)
        self.command.append(0x1d)
        self.command.append(0x68)
        self.command.append(self.bar_height)
        self.command.append(0x1d)
        self.command.append(0x66)
        self.command.append(CHAR_SET_9X17)
        self.command.append(0x1d)
        self.command.append(0x48)
        self.command.append(CHAR_ON_BOTTOM)
        self.command.append(0x1d)
        self.command.append(0x6B)
        self.command.append(BAR_CODE_EAN13)
        self.command.append(BAR_CODE_SIZE)
        for code in code_str:
            self.command.append(code)
        self.command.append(0x1B)
        self.command.append(0x64)
        self.command.append(white_rows)

        self.serial_write(self.command)
        
    def page_text(self, x, y,
                  text_string,
                  font_height=32,
                  bold=False,
                  under_line=False,
                  anti_white=False,
                  delete_line=False,
                  font_inc=0):
        self.command.append(0x1a)
        self.command.append(0x54)
        self.command.append(0x01)
        
        self.command.append(x&0x00ff)
        self.command.append((x&0xff00)>>8)
        self.command.append(y&0x00ff)
        self.command.append((y&0xff00)>>8)
        
        self.command.append(font_height&0x00ff)
        self.command.append((font_height&0xff00)>>8)
        
        font_type = bold
        font_type |= under_line<<1
        font_type |= anti_white<<2
        font_type |= delete_line<<3
        font_type |= font_inc<<8
        font_type |= font_inc<<12
        
        self.command.append(font_type&0x00ff)
        self.command.append((font_type&0xff00)>>8)
        
        for code in text_string.encode('gbk'):
            self.command.append(ord(code))
        
        self.command.append(0x00)
        
    def page_bar_code(self, x, y, code_string, code_type=CODE_EAN13, code_height=60, unit_width=2, rotate=0):
        self.command.append(0x1A)
        self.command.append(0x30)
        self.command.append(0x00)
        
        self.command.append(x&0x00ff)
        self.command.append((x&0xff00)>>8)
        
        self.command.append(y&0x00ff)
        self.command.append((y&0xff00)>>8)
        
        self.command.append(code_type)
        self.command.append(code_height)
        self.command.append(unit_width)
        self.command.append(rotate)
        
        for code in code_string:
            self.command.append(ord(code))
            
        self.command.append(0x00)
        
    def page_line(self, start_x, start_y, end_x, end_y, width, color=1):
        # color=1 black, color=0 white
        self.command.append(0x1A)
        self.command.append(0x5C)
        self.command.append(0x00)
        
        self.command.append(start_x&0x00ff)
        self.command.append((start_x&0xff00)>>8)
        
        self.command.append(start_y&0x00ff)
        self.command.append((start_y&0xff00)>>8)
        
        self.command.append(end_x&0x00ff)
        self.command.append((end_x&0xff00)>>8)
        
        self.command.append(end_y&0x00ff)
        self.command.append((end_y&0xff00)>>8)
        
        self.command.append(width&0x00ff)
        self.command.append((width&0xff00)>>8)
        
        self.command.append(color)
    
    def page_rectangle(self, left, top, right, bottom, width, color=1):
        self.command.append(0x1A)
        self.command.append(0x26)
        self.command.append(0x00)
        
        self.command.append(left&0x00ff)
        self.command.append((left&0xff00)>>8)
        
        self.command.append(top&0x00ff)
        self.command.append((top&0xff00)>>8)
        
        self.command.append(right&0x00ff)
        self.command.append((right&0xff00)>>8)
        
        self.command.append(bottom&0x00ff)
        self.command.append((bottom&0xff00)>>8)
        
        self.command.append(width&0x00ff)
        self.command.append((width&0xff00)>>8)
        
        self.command.append(color)
    
    def set_page_mode(self, start_x, start_y, width, height, rotate=0):
        self.command.append(0x1B)
        self.command.append(0x40)
        
        # PAGE START
        self.command.append(0x1A)
        self.command.append(0x5B)
        self.command.append(0x01)
        
        self.command.append(start_x&0x00ff)
        self.command.append((start_x&0xff00)>>8)
        
        self.command.append(start_y&0x00ff)
        self.command.append((start_y&0xff00)>>8)
        
        self.command.append(width&0x00ff)
        self.command.append((width&0xff00)>>8)
        
        self.command.append(height&0x00ff)
        self.command.append((height&0xff00)>>8)
        
        self.command.append(rotate)
    
    def page_end(self):
        # page end
        self.command.append(0x1A)
        self.command.append(0x5D)
        self.command.append(0x00)
        

    def page_print(self):
        # page print
        self.command.append(0x1A)
        self.command.append(0x4F)
        self.command.append(0x00)
    
    def set_frame(self):
        #                      |         
        #     _________________|         
        #     _________________|         
        #                      |_________
        #                      |_________
        #                      |_________
        # width=384 height=218
         
        self.page_line(  0,  89, 212,  89, 5)
        self.page_line(  0, 109, 212, 109, 5)
        self.page_line(212,   0, 212, 218, 5)
        self.page_line(212,  99, 384,  99, 5)
        self.page_line(212, 160, 384, 160, 5)
        self.page_line(212, 211, 384, 211, 5)

    def calculate_check_bit(self, bar_code):
        int_bar_code = [int(code) for code in bar_code]
        sum_even = sum(int_bar_code[::2])
        sum_odd = sum(int_bar_code[1::2])
        total_sum = sum_even + sum_odd*3
        check_bit = (10 - total_sum%10)%10
        return check_bit    

    def print_label(self, friute_name, goods_id, unit_price, weight, total_price):
        # self.clear()
        # Set printer with page mode
        self.set_page_mode(PAGE_START_X, PAGE_START_Y, PAGE_WIDTH, PAGE_HEIGHT)
        # Draw lines to split modules
        self.set_frame()

        # Print friute name
        if len(friute_name) == 1:
            self.page_text(70, 25, friute_name, font_inc=2)
        elif len(friute_name) == 2:
            self.page_text(50, 25, friute_name, font_inc=2)
        elif len(friute_name) == 3:
            self.page_text(30, 25, friute_name, font_inc=2)
        elif len(friute_name) == 4:
            self.page_text(10, 25, friute_name, font_inc=2)
        elif len(friute_name) == 5:
            self.page_text(30, 35, friute_name, font_inc=1)
        elif len(friute_name) == 6:
            self.page_text(25, 35, friute_name, font_inc=1)
        elif len(friute_name) == 7:
            self.page_text(20, 35, friute_name, font_inc=1)
        else:
            self.page_text(10, 35, friute_name, font_inc=1)

        c_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.page_text(20, 91, c_time, font_height=16)

        bar_code = str(goods_id) + '%05d'%int(total_price*100)
        check_bit = str(self.calculate_check_bit(bar_code))

        self.page_bar_code(3, 120, bar_code+check_bit)
        self.page_text(6, 185, str(goods_id)+' '+'%05d'%(total_price*100)+' '+check_bit)

        self.page_text(215, 20, u'总价：', font_height=24)
        self.page_text(180, 50, u" % 5.2f "%total_price, bold=True, font_height=24, font_inc=2)
        self.page_text(350, 75, u"元", font_height=24)

        self.page_text(215, 110, u'重量：', font_height=24)
        self.page_text(240, 137, u" % 6.3f kg"%(float(weight)/1000), bold=True, font_height=24)

        self.page_text(215, 162, u'单价：', font_height=24)
        self.page_text(220, 187, u' % 6.2f 元/kg'%float(unit_price), bold=True, font_height=24)

        self.page_end()
        self.page_print()

        logger.debug(self.command)

        self.serial_write(self.command)
        self.command = []


class ReceiptPrinter(object):
    def __init__(self, dev_name='/dev/serial/by-id/'+SERIAL_ID, bond_rate=115200):
        self.serial = serial.Serial(dev_name, bond_rate)

    def serial_write(self, command):
        if not self.serial.isOpen():
            self.serial.open()
        self.serial.write(command)
        self.serial.close()

    @staticmethod
    def font_size(inc=0):
        if inc > 7:
            inc = 7
        return [0x1D, 0x21, inc*17]

    @staticmethod
    def bold(bold=False):
        if bold:
            bold = 0x01
        else:
            bold = 0x00
        return [0x1B, 0x45, bold]

    @staticmethod
    def encode_mode(mode='gbk'):
        command = [0x1B, 0x39]
        if mode == 'gbk':
            command.append(0x00)
        elif mode == 'uft-8':
            command.append(0x01)
        else:
            # 繁体编码
            command.append(0x03)
        return command

    def text(self, words, font_inc=0, bold=False, input_lines=0):
        # 设置汉字模式（两个字节处理）
        command = [0x1C, 0x26]
        # 选择gbk编码
        command += self.encode_mode('gbk')
        # 设置字体大小，0-7有效
        command += self.font_size(font_inc)
        command += self.bold(bold)
        for word in words.encode('gbk'):
            command.append(ord(word))
        # 打印并进纸n行
        command += self.print_and_input_paper(input_lines)
        return command

    @staticmethod
    def line(start_x, end_x, lines=1):
        command = [0x1D, 0x27, lines]
        command.append(start_x & 0x00ff)
        command.append((start_x & 0xff00) >> 8)
        command.append(end_x & 0x00ff)
        command.append((end_x & 0xff00) >> 8)
        return command

    @staticmethod
    def print_and_input_paper(input_lines=0):
        command = list()
        command.append(0x1B)
        command.append(0x64)
        command.append(input_lines)
        return command

    @staticmethod
    def cut(mode='FULL', input_lines=0):
        command = list()
        command.append(0x1D)
        command.append(0x56)
        if input_lines != 0:
            command.append(0x42)
            command.append(input_lines)
            return command
        if mode == 'FULL':
            command.append(0x00)
        else:
            command.append(0x01)
        return command

    @staticmethod
    def format_text(text, length):
        chinese_regex = re.compile(u"[\u4E00-\uFFA5]")
        chinese_count = len(chinese_regex.findall(text))
        return text.center(length-chinese_count)

    def print_order(self, order, fruits):
        total = 0
        command = self.text(self.format_text(u"某某水果店", 24), font_inc=1)
        c_time = time.strftime(self.format_text(u"%Y-%m-%d %H:%M:%S", 46))
        command += self.text(c_time, font_inc=0)
        order_info = u"订单编号：%s" % order.id
        command += self.text(self.format_text(order_info, 46))
        command += self.print_and_input_paper(1)
        title_info = self.format_text(u"名称", 16)
        title_info += self.format_text(u"单价", 10)
        title_info += self.format_text(u"重量", 10)
        title_info += self.format_text(u"小计", 10)
        command += self.text(title_info, bold=True)
        for fruit in fruits:
            fruit_info = self.format_text(fruit.goodsName, 16)
            fruit_info = fruit_info + self.format_text(fruit.price, 10)
            fruit_info = fruit_info + self.format_text(str(fruit.weight)+u'g', 10)
            fruit_info = fruit_info + self.format_text(str(float(fruit.total)/100)+u'元', 10)
            command += self.text(fruit_info)
            total += fruit.total
        command += self.print_and_input_paper(1)
        command += self.text(self.format_text(u"总价：%s" % (float(total)/100), 23), font_inc=1)
        command += self.text(self.format_text(u"实际付款：%s" % (float(order.total)/100), 23),
                             font_inc=1, input_lines=5)
        # 选择切纸模式
        command += self.cut('HALF')
        self.serial_write(command)


class Fruit(object):
    def __init__(self, goodsName, priceUnit, weight, total):
        self.goodsName = goodsName
        self.priceUnit = priceUnit
        self.weight = weight
        self.total = total


class Order(object):
    def __init__(self, id, total):
        self.id = id
        self.total =total


#fruits = [Fruit(u'苹果', 100, 120, 200), Fruit(u'苹果2', 200, 220, 400)]
#p = ReceiptPrinter(dev_name='COM3')
# p.text(u'你好', font_inc=1)
#p.print_order(Order("1234456", 345), fruits)

