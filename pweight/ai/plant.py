# encoding:utf-8
import base64
import urllib
import urllib2

import access
from pweight import utils

base_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"


@utils.func_timer
def image_classify(image_path):
    # 二进制方式打开图片文件
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    params = urllib.urlencode(params)

    access_token = access.get_token()

    request_url = base_url + "?access_token=" + access_token
    request = urllib2.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        return content
    else:
        print("conten is empty or none.")
        return content


