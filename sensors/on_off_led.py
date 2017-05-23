import RPi.GPIO as GPIO
from pins import ON_OFF_LED
LED1 = ON_OFF_LED

def setup(*leds):
    GPIO.setmode(GPIO.BCM)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)


def switch(*leds):
    for led in leds:
        GPIO.output(led, GPIO.HIGH)

if __name__ == '__main__':
    setup(LED1)
    try:
        while True:
            switch(LED1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
    
