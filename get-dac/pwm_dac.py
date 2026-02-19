import RPi.GPIO as GPIO

dynamic_range = 3.3
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.00 В")
        return 0
    return int(voltage / dynamic_range * 255)

class RWM_DAC:
    def __init__(self, gpio_pin, pwm_frequensy, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequensy = pwm_frequensy
        self.dynamic_range = dynamic_range
        self.verbose = verbose
    def deinit(self):
        GPIO.cleanup()
    def set_voltage(self, voltage):
        p = GPIO.PWM(self.gpio_pin, self.pwm_frequensy)
        p.start(voltage/self.dynamic_range*100)
        input("Нажмите Enter чтобы прекратить")
        p.stop()
        
if __name__ == "__main__":
    try:
        dac = RWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз.")
        
    finally:
        dac.deinit()