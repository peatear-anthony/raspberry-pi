import RPi.GPIO as GPIO
import time
import piir


MAX_DISTANCE = 220
TIME_OUT = MAX_DISTANCE*60

echo_pin = 12
trig_pin = 5

led_green_pin = 20
led_red_pin = 16
LIGHT_STATE = False

remote = piir.Remote('light.json', 17)

def pulse_in(pin, level, TIME_OUT):
    t_start = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t_start) > TIME_OUT*0.000001):
            return 0
    t_end = time.time()

    while(GPIO.input(pin) == level):
        if((time.time() - t_start) > TIME_OUT*0.000001):
            return 0  
    
    return (time.time() - t_end) * 1000000


def get_sonar():
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(trig_pin, GPIO.LOW)
    ping_time = pulse_in(echo_pin, GPIO.HIGH, TIME_OUT)
    return ping_time * 340 / 2.0 / 10000.0


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_green_pin, GPIO.OUT)
    GPIO.output(led_green_pin, GPIO.LOW)
    GPIO.setup(led_red_pin, GPIO.OUT)
    GPIO.output(led_red_pin, GPIO.LOW)
    GPIO.setup(echo_pin, GPIO.IN)    
    GPIO.setup(trig_pin, GPIO.OUT)  

def loop():
    while True:
        distance = get_sonar()
        print(distance)
        time.sleep(0.5)
        '''
        if GPIO.input(pir_sensor_pin) == GPIO.HIGH:
            GPIO.output(led_green_pin, GPIO.HIGH)
            GPIO.output(led_red_pin, GPIO.LOW)
            if not LIGHT_STATE:
                remote.send('off')
                LIGHT_STATE = True
        else:
            GPIO.output(led_red_pin, GPIO.HIGH)
            GPIO.output(led_green_pin, GPIO.LOW)
            LIGHT_STATE = False
        '''
      
if  __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
