import RPi.GPIO as GPIO
from time import sleep

inbutton = 13
outpin = 7
z = 1


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(outpin, GPIO.OUT)
    GPIO.setup(inbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global z
    z = 1


def zest(channel):
    global z
    if z == 1:
        z = 2
        while z == 2:
            GPIO.output(outpin, 1)
            print("led on")
            sleep(1)

            GPIO.output(outpin, 0)
            print("led off")
            sleep(1)

    elif z == 2:
        z = 1
        while z == 1:
            GPIO.output(outpin, 1)
            print("led on")
            sleep(2)

            GPIO.output(outpin, 0)
            print("led off")
            sleep(2)


def loop():
    GPIO.add_event_detect(inbutton, GPIO.FALLING, callback=zest, bouncetime=1000)


if __name__ == '__main__':
    init()
    try:
        while True:
            loop()

    except KeyboardInterrupt:
        GPIO.output(outpin, 0)
        GPIO.cleanup()