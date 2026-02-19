import RPi.GPIO as GPIO

dynamic_range = 3.3

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.00 В")
        return 0
    return int(voltage / dynamic_range * 255)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        for i in range (8):
            GPIO.output(self.gpio_bits[i], number_to_dac(number)[i])
    def set_voltage(self, voltage):
        number = voltage_to_number(voltage)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз.")
        
    finally:
        dac.deinit()