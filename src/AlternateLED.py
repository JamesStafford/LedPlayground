import threading
import RPi.GPIO as GPIO
import time

blueLedOut = 17
redLedOut = 27
buttonIn = 22


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(blueLedOut, GPIO.OUT)
    GPIO.setup(redLedOut, GPIO.OUT)

    # GPIO.setup(buttonIn, GPIO.IN)


def blink(pin, iteration):
    light_on = True

    for _ in range(iteration * 2):
        GPIO.output(pin, light_on)
        time.sleep(.5)
        light_on = not light_on


def main():
    try:
        print("Starting LED show")

        setup()

        red_led_thread = threading.Thread(target=blink, args=(redLedOut, 10))
        blue_led_thread = threading.Thread(target=blink, args=(blueLedOut, 10))

        red_led_thread.start()
        blue_led_thread.start()

        red_led_thread.join()
        blue_led_thread.join()

        print("End of LED Show")
    finally:
        GPIO.cleanup()


main()
