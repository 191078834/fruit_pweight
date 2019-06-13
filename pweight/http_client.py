# coding=utf8

import os
import json
import logging
import time
import urllib
import urllib2
from PyQt4.QtCore import QThread, pyqtSignal
from pweight import utils
import shutil
import json
from pweight import printer
logger = logging.getLogger('pweight')
import pdb
DEVICE_NUMBER = 'T00001'
IDENTITY_URL = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/identifyGoods"
CONFIRM_URL = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/confirmGoods"
CREATEORDER_URL = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/createOrder"
MICROPAY_URL = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/micropay"
REFRESHORDER_URL = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/refreshOrder"
DATATYPEREG = "http://scale.infiniticloud.cn/ai-balance-server/device/v1.0/common/dataTypeReg"
#IDENTITY_URL = "http://172.28.217.66:8080/ai-balance-server/device/v1.0/common/identifyGoods"
#CONFIRM_URL = "http://172.28.217.66:8080/ai-balance-server/device/v1.0/common/confirmGoods"
#CONFIRM_URL = "http://172.18.118.81:8080/ai-balance-server/device/v1.0/common/confirmGoods"


class Fruit(object):
    def __init__(self, result):
        self.id = result.get('goodsId')
        self.no = result.get('goodsNo')
        self.name = result.get('goodsName')
        self.type_name = result.get('typeName')
        self.price = result.get('price')
        self.goods_price = result.get('goodsPrice')
        if self.goods_price:
            self.goods_price = float(self.goods_price) / 100
        self.price_unit = result.get('priceUnit')
        self.calculate_type = result.get('calculateType')

        # confirm resp
        self.record_id = result.get('recordId')
        self.weight = result.get('weight')
        self.num = result.get('num')
        self.total = result.get('total')
        if self.total:
            self.total = float(self.total) / 100
        self.discount = result.get('discount')
        self.fact = result.get('fact')
        if self.fact:
            self.fact = float(self.fact) / 100
        self.image_url = result.get('imgUrl')

        # discard keys
        self.type_id = result.get('typeId')
        self.status = result.get('status')
        self.remark = result.get('remark')
        self.create_time = result.get('createTime')
        self.group_id = result.get('groupId')

        logger.info("+------------------------------------------------+")
        logger.info("+ id: %s" % self.id)
        logger.info("+ no: %s" % self.no)
        logger.info("+ name: %s" % self.name)
        logger.info("+ type_name: %s" % self.type_name)
        logger.info("+ price: %s" % self.price)
        logger.info("+ goods price: %s" % self.goods_price)
        logger.info("+ price unit: %s" % self.price_unit)
        logger.info("+ calculate_type: %s" % self.calculate_type)

        logger.info("+ record_id: %s" % self.record_id)
        logger.info("+ weight: %s" % self.weight)
        logger.info("+ num: %s" % self.num)
        logger.info("+ total: %s" % self.total)
        logger.info("+ discount: %s" % self.discount)
        logger.info("+ fact: %s" % self.fact)
        logger.info("+ image_url: %s" % self.image_url)
        logger.info("+------------------------------------------------+")


class IdentifyResp(object):
    def __init__(self, resp):
        self.msg = resp.get('msg')
        self.record_id = resp.get('recordId')
        self.code = resp.get('code')

        logger.info("+++ Identify Resp info start +++")
        logger.info("++ msg: %s" % self.msg)
        logger.info("++ record_id: %s" % self.record_id)
        logger.info("++ code: %s" % self.code)

        if resp.get('data'):
            # self.results = [Fruit(result) for result in resp.get('data')]
            self.results = resp.get('data')
        else:
            self.results = None

        logger.info("+++ Identify Resp info end +++")


class ConfirmResp(object):
    def __init__(self, resp):
        self.msg = resp.get('msg')
        self.code = resp.get('code')

        logger.info("+++ Confirm Resp info start +++")
        logger.info("++ msg: %s" % self.msg)
        logger.info("++ code: %s" % self.code)

        if resp.get('data'):
            # self.results = Fruit(resp.get('data'))
            self.results = resp.get('data')
        else:
            logger.warn("data is None")
            self.results = None

        logger.info("+++ Confirm Resp info end +++")


class HttpClient(QThread):
    signal_identify_goods_resp = pyqtSignal(IdentifyResp, int)

    def __init__(self):
        super(HttpClient, self).__init__()
        self.images = []
        self.weight = 0

    def set_info(self, images, weight):
        self.images = images
        self.weight = weight

    @utils.func_timer
    def identify_goods(self, images, weight):
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data = []
        data.append('--%s' % boundary)
        data.append(
            'Content-Disposition: form-data; name="%s"\r\n' %
            'deviceNo')
        data.append(DEVICE_NUMBER)

        data.append('--%s' % boundary)

        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'weight')
        data.append(str(weight))

        for image in images:
            data.append('--%s' % boundary)
            data.append(
                'Content-Disposition: form-data; name="%s"; filename="b.jpg"' %
                'files')
            data.append('Content-Type: %s\r\n' % 'image/jpg')
            data.append(image)
            data.append('--%s' % boundary)

        http_body = '\r\n'.join(data)

        req = urllib2.Request(IDENTITY_URL, data=http_body)
        req.add_header(
            'Content-Type',
            'multipart/form-data; boundary=%s' %
            boundary)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Referer', 'http://remotserver.com/')
        resp = urllib2.urlopen(req, timeout=30)
        resp_json = json.loads(resp.read())
        if resp_json is not None:
            return IdentifyResp(resp_json)
        else:
            return None

    def run(self):
        self.signal_identify_goods_resp.emit(
            self.identify_goods(self.images, self.weight), self.weight)


@utils.func_timer
def confirm_goods(record_id, goods_id):
    try:
        # 将user_agent写入头信息
        user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'recordId': record_id, 'goodsId': goods_id}  # post数据
        headers = {'User-Agent': user_agent}
        data = urllib.urlencode(values)  # 对post数据进行url编码
        logger.info(data)
        req = urllib2.Request(CONFIRM_URL, data, headers)
        resp = urllib2.urlopen(req, timeout=30)
        resp_json = json.loads(resp.read())
        if resp_json is not None:
            return ConfirmResp(resp_json)
        else:
            return None
            # logger.debug('Confirm result: %s'%result)
    except Exception as e:
        logger.error(e)


# @utils._retry
def create_order(recordids_list):
    headers = {'Content-Type': 'application/json'}
    dict_info = {
        "deviceNo": DEVICE_NUMBER,
        "recordIds": recordids_list}
    data = json.dumps(dict_info)
    response_json = utils.get_json_by_requests(
        url=CREATEORDER_URL, data=data, headers=headers)
    if response_json.get('code') == 0:
        logger.debug('Order craete success.')
        return response_json['data']
    else:
        logger.error('Create order failed, response code is not 0, retry now.')
        return None


def get_order_info(orderNo, qrcode_str):
    dict_info = {"deviceNo": DEVICE_NUMBER, "orderNo": orderNo, "authCode":qrcode_str}
    data = json.dumps(dict_info)
    response_json = utils.get_json_by_requests(
        url=MICROPAY_URL, data=data, headers={'Content-Type':'application/json'})
    if response_json.get('code') == 0:
        logger.debug('Get order info success.')
        return response_json['data']['status']
    else:
        logger.error('Get order info failed, response code is not 0.')
    return None



#@utils._retry
def refresh_order(orderNo):
    dict_info = {"deviceNo": DEVICE_NUMBER, "orderNo": orderNo}
    response_json = utils.get_json_by_requests(
        url=REFRESHORDER_URL, data=dict_info)
    if response_json.get('code') == 0:
        logger.debug('Get order info success.')
        return response_json['data']['status']
    else:
        logger.error('Refresh order info failed, response code is not 0.')
    return None
# with open('images/20181115132215.jpg', 'rb') as image_file:
#    img = image_file.read()
#    identify_goods([img], 120)

#c = HttpClient()

#c.confirm_goods("9df1e1ad2212463c92eb3013561db8f1", 1)
class UploadImage(QThread):
    signal_upload_resp = pyqtSignal(int)

    def __init__(self, save_image_folder_path):
        super(UploadImage, self).__init__()
        self.save_image_base_path = save_image_folder_path
        self.folder_name = ''

    def set_folder_name(self, folder_name):
        self.folder_name = folder_name

    def upload_image(self,folder_name):
        image_names = os.listdir(self.save_image_base_path + folder_name)
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data = []
        for image_name in image_names:
            data.append('--%s' % boundary)
            data.append(
                'Content-Disposition: form-data; name="%s"; filename="b.png' %
                'imgFile')
            data.append('Content-Type: %s\r\n' % 'image/jpg')
            with open(os.path.join(self.save_image_base_path + folder_name, image_name) , 'rb') as file:
                data.append(file.read())
            data.append('--%s' % boundary)
        http_body = '\r\n'.join(data)
        req = urllib2.Request(DATATYPEREG, data=http_body)
        req.add_header(
            'Content-Type',
            'multipart/form-data; boundary=%s' %
            boundary)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Referer', 'http://remotserver.com/')
        resp = urllib2.urlopen(req, timeout=30)
        info = json.loads(resp.read())
        if info.get('msg') == 'success':
            logger.info("upload success:%s" % os.path.join(self.save_image_base_path , folder_name))
            shutil.rmtree(os.path.join(self.save_image_base_path, folder_name))
            return 1
        else:
            logger.info("upload fail:%s" % os.path.join(self.save_image_base_path , folder_name))
            return 0

    def run(self):
        self.signal_upload_resp.emit(self.upload_image(self.folder_name))

class Raw_print(QThread):
    signal_qrcodestr_resp = pyqtSignal(str)

    def __init__(self):
        super(Raw_print, self).__init__()
        self.printer = printer.ReceiptPrinter()
        self.order = ''
        self.selected_fruits = ''

    def set_data(self, order, selected_fruits):
        self.order = order
        self.selected_fruits = selected_fruits
    def run(self):
        self.printer.print_order(self.order, self.selected_fruits)



# boundary = '----------%s' % hex(int(time.time() * 1000))
# save_image_base_path = 'E:/images/'
# data = []
# image_names = os.listdir(save_image_base_path)
#
# for image_name in image_names:
#     data.append('--%s' % boundary)
#     data.append(
#         'Content-Disposition: form-data; name="%s"; filename="b.png' %
#         'imgFile')
#     data.append('Content-Type: %s\r\n' % 'image/jpg')
#     with open(save_image_base_path + image_name, 'rb') as file:
#         data.append(file.read())
#     data.append('--%s' % boundary)
# http_body = '\r\n'.join(data)
# req = urllib2.Request(DATATYPEREG, data=http_body)
# req.add_header(
#     'Content-Type',
#     'multipart/form-data; boundary=%s' %
#     boundary)
# req.add_header('User-Agent', 'Mozilla/5.0')
# req.add_header('Referer', 'http://remotserver.com/')
# resp = urllib2.urlopen(req, timeout=30)
# print resp.read
# import json
# res = json.loads(resp.read())



