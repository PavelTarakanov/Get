import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
bin = [0]*8
up = 9
down = 10
num = 0
sleep_time = 0.2

GPIO.setup(leds, GPIO.OUT)

print(dec2bin(5))

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

for led in leds:
    GPIO.output(led, 0)

while True:
    if (GPIO.input(up)):
        num += 1
        if (num > 127):
            num = 0
        time.sleep(sleep_time)
    if (GPIO.input(down)):
        num -= 1
        if (num < 0):
            num = 255
        time.sleep(sleep_time)
    print(num, dec2bin(num))
    for i in range(8):
        GPIO.output(leds[i], num%2)
        num = num //2



