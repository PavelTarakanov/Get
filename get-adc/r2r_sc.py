import RPi.GPIO as GPIO
import time
import adc_plot as plt

class R2R_ADC:
    def __init__ (self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        output = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range (8):
            GPIO.output(self.bits_gpio[i], output[i])
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)

            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                return number
        
        return 0
    def get_sc_voltage(self):
        number = self.sequential_counting_adc()

        print(f"Напряжение: {(number/256)*self.dynamic_range:.3f}В")
        return (number/256)*self.dynamic_range

if __name__ == "__main__":
    adc = R2R_ADC(3.3)

    voltage_values = []
    time_values = []
    duration = 10.0

    try:
        start_time = time.time()

        while(time.time() - start_time < duration):
            current_time = time.time() - start_time

            voltage = adc.get_sc_voltage()
            voltage_values.append(voltage)

            time_values.append(current_time)

        plt.plot_voltage_vs_time(time_values, voltage_values, 3.3)
        plt.plot_sampling_period_hist(time_values)
    finally:
        adc.deinit()
