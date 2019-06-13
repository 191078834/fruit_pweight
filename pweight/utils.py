#!/usr/bin/python
# coding:utf-8
from PyQt4 import QtGui
import logging
from functools import wraps
import os
import ConfigParser
import qrcode
import time
import uuid
import urllib
import re
import ssl
import requests
from PIL import Image
ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger('pweight')

def func_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        logger.info("Time %s: %s s" % (function.func_name, str(t1 - t0)))
        return result
    return function_timer

def get_conf_value(config_file, section, key):
    cp = ConfigParser.SafeConfigParser(allow_no_value=True)
    cp.read(config_file)
    return cp.get(section, key)


def qc(code_url):
    # 创建qrcode对象
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=1,
    )
    # version为一个整数，范围1~40，作用表示二维码的大小
    # error_correction容错率，挡出部分二维码还能识别，越高可以挡住部分越多，但数据量增加
    # 四个等级：H,L,M,Q  Q最高，可以挡住25%
    # box_size 每个格子里像素大小
    # border 表示二维码距离图像外边框的距离
    qr.add_data(code_url)
    img = qr.make_image()  # 创建二维码图片
    img = img.resize((310,310))
    # img = img.convert("RGBA")  # 图片转换为RGBA格式
    # pil_img = img.get_image()
    # img_w,img_h=images.size #返回二维码图片的大小
    # path = "%s.png" % 'qr_code'
    # img.save(path)  # 保存图片
    return img

def get_pixmap_img(pil_img):
    data = pil_img.convert('RGBA').tobytes('raw', 'RGBA')
    qimg = QtGui.QImage(data, pil_img.size[0], pil_img.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qimg)
    return pixmap


def get_static_images_path(conf_path, image_parameter):
    static_images_path = get_conf_value(conf_path, 'static', 'images_path')
    image_name = get_conf_value(conf_path, 'static', image_parameter)
    image_path = os.path.join(static_images_path, image_name)
    return image_path


def generate_uuid():
    return str(uuid.uuid1())


def mkdir(path):
    if os.path.exists(path):
        return 0
    try:
        os.makedirs(path)
    except OSError as e:
        logger.error('Failed to create directory %s.' % path)
        # logger.exception(e)


def download_file(url, base_path, filename = ''):
    file_path = base_path + filename
    # directory = os.path.dirname(file_path)
    # mkdir(directory)
    if url:
        try:
            urllib.urlretrieve(url, file_path)
            return file_path
        except Exception as e:
            print e
            return 0
    else:
        return 0


def get_json_by_requests(url, params = None, headers = '', data = None):
    json = {}
    response = None
    try:
        #response = requests.get(url, params = params)
        if data:
            response = requests.post(url, headers = headers, data = data, params = params, timeout = 30, verify=False)
        else:
            response = requests.get(url, headers=headers, params = params, timeout=30, verify = False)
        response.encoding = 'utf-8'
        json = response.json()
    except Exception as e:
        logging.error(e)
    finally:
        response and response.close()
    return json


_regexs = {}
def get_info(html, regexs, allow_repeat = False, fetch_one = False, split = None):
    regexs = isinstance(regexs, str) and [regexs] or regexs

    infos = []
    for regex in regexs:
        if regex == '':
                continue

        if regex not in _regexs.keys():
            _regexs[regex] = re.compile(regex, re.S)

        if fetch_one:
                infos = _regexs[regex].search(html)
                if infos:
                    infos = infos.groups()
                else:
                    continue
        else:
            infos = _regexs[regex].findall(str(html))

        if len(infos) > 0:
            break

    if fetch_one:
        infos = infos if infos else ('',)
        return infos if len(infos) > 1 else infos[0]
    else:
        infos = allow_repeat and infos or sorted(set(infos),key = infos.index)
        infos = split.join(infos) if split else infos
        return infos


def set_cache_fruits_image_path(fruit_id, fruit_imgUrl, cache_images_path):
    mkdir(cache_images_path)
    goodsId = str(fruit_id)
    imgUrl = get_info(fruit_imgUrl, '.*/(.*)', fetch_one=True)
    image_path = goodsId + '_-_' + imgUrl
    cache_fruit_images_paths = os.listdir(cache_images_path)

    if image_path in cache_fruit_images_paths:
        return cache_images_path + image_path
    else:
        for image in cache_fruit_images_paths:
            if image.split('_-_')[0] == goodsId:
                os.remove(cache_images_path + image)
        image_path = download_file(url=fruit_imgUrl, base_path=cache_images_path, filename=image_path)

        if image_path:
            base_img = Image.open(image_path)
            base_img = base_img.convert("RGB")
            base_img = base_img.resize((299, 299))
            base_img.save(image_path)
            return image_path

def blend_image(img1, img2):
    base_img = Image.open(img1)
    base_img = base_img.convert("RGB")
    base_img = base_img.resize((299, 299))

    tmp_img = Image.open(img2)
    region = tmp_img
    region = region.convert("RGB")
    region = region.resize((299, 299))
    new_img = Image.blend(base_img, region, 0.7)
    new_img = new_img.resize((279, 279))
    return new_img


def _retry(function):
    @wraps(function)
    def function_retry(*args, **kwargs):
        for retry_count in range(2):
            result = function(*args, **kwargs)
            if result is not None:
                return result
            else:
                time.sleep(1)
                logger.info("Function %s return None, retry %s times." % (function.func_name, str(retry_count)))
        return None
    return function_retry

def judge_qr_code(s):
    '''
    0 error
    1 ali
    2 Wechat
    '''
    s = str(s)
    try:
        if int(s[:2])>24 and int(s[:2])<31:
            if len(s)>15 and len(s)<25:
                return 1
            else:
                logger.error('请出示正确二维码')
                return 0
        elif int(s[:2])>9 and int(s[:2])<16:
            if len(s)==18:
                return 2
            else:
                logger.error('请出示正确二维码')
                return 0
        else:
            logger.error('请出示正确二维码')
            return 0
    except Exception as e:
        logger.error('请出示正确二维码')
        return 0
judge_qr_code(134764025625498688)