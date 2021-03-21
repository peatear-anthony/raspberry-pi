import RPi.GPIO as GPIO
import time


led_green_pin = 20
led_red_pin = 16
pir_sensor_pin = 23

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_sensor_pin, GPIO.IN)
    GPIO.setup(led_green_pin, GPIO.OUT)
    GPIO.output(led_green_pin, GPIO.LOW)
    GPIO.setup(led_red_pin, GPIO.OUT)
    GPIO.output(led_red_pin, GPIO.LOW)


def loop():
    while True:
        if GPIO.input(pir_sensor_pin) == GPIO.HIGH:
            GPIO.output(led_green_pin, GPIO.HIGH)
            GPIO.output(led_red_pin, GPIO.LOW)
        else:
            GPIO.output(led_red_pin, GPIO.HIGH)
            GPIO.output(led_green_pin, GPIO.LOW)

if  __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
