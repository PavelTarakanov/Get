import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.00 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(dac_bits, GPIO.OUT)
dynamic_range = 3.3


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах:  "))
            number = voltage_to_number(voltage)
            for i in range (8):
                GPIO.output(dac_bits[i], number_to_dac(number)[i])
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз.")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()