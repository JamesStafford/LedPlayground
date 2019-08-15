import RPi.GPIO as GPIO
import time

redLedOut = 17
yellowLedOut = 27
buttonIn = 22

activeLED = yellowLedOut


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(redLedOut, GPIO.OUT)
    GPIO.setup(yellowLedOut, GPIO.OUT)

    GPIO.setup(buttonIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def console_button_press(buttonIn):
    global activeLED
    print("Button Pressed")
    GPIO.output(activeLED, False)
    if activeLED == yellowLedOut:
        activeLED = redLedOut
    else:
        activeLED = yellowLedOut


def main():
    try:
        setup()
        GPIO.add_event_detect(buttonIn, GPIO.FALLING, callback=console_button_press, bouncetime=500)
        light_on = True
        while True:
            GPIO.output(activeLED, light_on)
            time.sleep(.25)
            light_on = not light_on
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
