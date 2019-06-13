import RPi.GPIO as GPIO


class Led(object):
    def __init__(self, RED_pin, GREEN_pin, BLUE_pin):
        self.red_pin = RED_pin
        self.green_pin = GREEN_pin
        self.blue_pin = BLUE_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(RED_pin,   GPIO.OUT)
        GPIO.setup(GREEN_pin, GPIO.OUT)
        GPIO.setup(BLUE_pin,  GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def red(self, stat):
        if stat:
            GPIO.output(self.red_pin, GPIO.HIGH)
        else:
            GPIO.output(self.red_pin, GPIO.LOW)

    def green(self, stat):
        if stat:
            GPIO.output(self.green_pin, GPIO.HIGH)
        else:
            GPIO.output(self.green_pin, GPIO.LOW)

    def blue(self, stat):
        if stat:
            GPIO.output(self.blue_pin, GPIO.HIGH)
        else:
            GPIO.output(self.blue_pin, GPIO.LOW)

    def all(self, stat):
        if stat:
            GPIO.output(self.red_pin, GPIO.HIGH)
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.blue_pin, GPIO.HIGH)
        else:
            GPIO.output(self.red_pin, GPIO.LOW)
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.blue_pin, GPIO.LOW)


#import time
#led = Led(16,18,12)
#led.blue(True)
#time.sleep(3)
#led.blue(False)

