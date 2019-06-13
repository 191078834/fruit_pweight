from ctypes import *
import time

libweight = CDLL("./libweight.so")

ret = libweight.init_weight(16, 15)

print "coefficient:" + str(libweight.get_coefficient())
print "calibration:" + str(libweight.get_calibration())

while(True):
    if ret==0:
        weight = libweight.get_average_value(10)
        print "weight:" + str(weight)
        time.sleep(0.2)
    else:
        print "init ret:" + ret
   

