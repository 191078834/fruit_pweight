import os
import cv2
import time
import logging
from PyQt4.QtCore import QThread

logger = logging.getLogger('pweight')

PHOTO_WIDTH = 1920
PHOTO_HEIGHT = 1080
IMAGE_START_X = 440
IMAGE_END_X = 1440
IMAGE_START_Y = 115
IMAGE_END_Y = 915

IMAGES_DIR = '/home/pweight/images/'


class CaptureThread(QThread):

    def __init__(self, save_image_base_path):
        super(CaptureThread, self).__init__()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  PHOTO_WIDTH)
        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, PHOTO_HEIGHT)
        self.save_image_base_path = save_image_base_path
        self.cur_frame = None

    def save_image_to_file(self, image, file_name, current_timestamp, return_path=False):
        if not os.path.exists(self.save_image_base_path + current_timestamp):
            logger.info('Images path %s does not exists, create now.' % current_timestamp)
            os.makedirs(self.save_image_base_path + current_timestamp)
        file_path = os.path.join(self.save_image_base_path + current_timestamp, file_name)
        logger.info('Save image to %s' % file_path)
        cv2.imwrite(file_path,
                    image[IMAGE_START_Y:IMAGE_END_Y, IMAGE_START_X:IMAGE_END_X],
                    [int(cv2.IMWRITE_JPEG_QUALITY),
                     80])
#        file_path = '/home/pweight/pweight/resource/images/test_apple.jpg'
        if return_path:
            return file_path
        with open(file_path, 'rb') as f:
            return f.read()

    # @utils.func_timer
    def take_one_photo(self):
        cur_str_time = time.strftime("%Y%m%d%H%M%S")
        # cv2.imshow("AdjustCamera", self.cur_frame)
        # cv2.imwrite(image_path, self.cur_frame)
        return self.save_image_to_file(self.cur_frame, cur_str_time+'.jpg', '')

    def get_one_frame(self):
        return self.cur_frame

    def run(self):
        last_log_time = time.time()
        while True:
            if not self.cap.isOpened():
                logger.warn("Capture is not opened, retry after 1 sec.")
                self.sleep(1)
                self.cap = cv2.VideoCapture(0)
                self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, PHOTO_WIDTH)
                self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, PHOTO_HEIGHT)
                continue
            ret, frame = self.cap.read()
            if ret:
                self.cur_frame = frame
            else:
                if time.time()-last_log_time > 5:
                    logger.warn("Capture read failed, ret: %s" % ret)
                    last_log_time = time.time()
            self.msleep(30)
