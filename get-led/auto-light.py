import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

photores = 6
state = 1

GPIO.setup(photores, GPIO.IN)

while True:
    state = not GPIO.input(photores)
    GPIO.output(led, state)