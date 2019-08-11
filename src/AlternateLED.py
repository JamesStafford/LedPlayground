import RPi.GPIO as GPIO
import time

print("Starting LED show")

blueLedOut = 17
redLedOut = 27

buttonIn = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(blueLedOut, GPIO.OUT)
GPIO.setup(redLedOut, GPIO.OUT)

# GPIO.setup(buttonIn, GPIO.IN)

GPIO.output(redLedOut, True)
time.sleep(.5)

GPIO.output(redLedOut, False)
time.sleep(.5)

GPIO.output(redLedOut, True)
time.sleep(.5)

GPIO.output(redLedOut, False)
time.sleep(.5)

print("End of LED Show")

GPIO.cleanup()
