import threading
import RPi.GPIO as GPIO
import time
import signal

blueLedOut = 17
redLedOut = 27
buttonIn = 22

redLedBlinking = True


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(blueLedOut, GPIO.OUT)
    GPIO.setup(redLedOut, GPIO.OUT)

    GPIO.setup(buttonIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def blink(pin, light_on):
    GPIO.output(pin, light_on)
    time.sleep(.1)


def blink_red_light():
    light_on = True
    while True:
        if redLedBlinking:
            blink(redLedOut, light_on)
            light_on = not light_on
        else:
            GPIO.output(redLedOut, False)


def blink_blue_light():
    light_on = True
    while True:
        if not redLedBlinking:
            blink(blueLedOut, light_on)
            light_on = not light_on
        else:
            GPIO.output(blueLedOut, False)


def blinking():
    """
    Red and Blue LED will both blinking
    :return:
    """
    red_led_thread = threading.Thread(target=blink_red_light)
    blue_led_thread = threading.Thread(target=blink_blue_light)
    red_led_thread.start(); blue_led_thread.start()


def console_button_press(buttonIn):
    """
    When button is pressed, "Button Pressed" will be print the console
    """
    print("Button Pressed")
    global redLedBlinking
    redLedBlinking = not redLedBlinking


def main():
    try:
        print("Starting LED show")

        setup()
        GPIO.add_event_detect(buttonIn, GPIO.FALLING, callback=console_button_press, bouncetime=500)
        blinking()
        while True:
            signal.pause()

        print("End of LED Show")
    finally:
        GPIO.cleanup()


main()
