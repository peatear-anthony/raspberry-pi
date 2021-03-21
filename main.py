import RPi.GPIO as GPIO
import time


led_green_pin = 20
led_red_pin = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_green_pin, GPIO.OUT)
    GPIO.output(led_green_pin, GPIO.LOW)
    GPIO.setup(led_red_pin, GPIO.OUT)
    GPIO.output(led_red_pin, GPIO.LOW)


def loop():
    while True:
        GPIO.output(led_green_pin, GPIO.HIGH)
        GPIO.output(led_red_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(led_red_pin, GPIO.HIGH)
        GPIO.output(led_green_pin, GPIO.LOW)
        time.sleep(1)

if  __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
