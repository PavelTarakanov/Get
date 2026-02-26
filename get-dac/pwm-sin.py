import pwm_dac
import math
import time

amplitude = 1.5
freq = 10
sampling_freq = 10000

dac = pwm_dac.PWM_DAC(12, 3.3)

try:
    while(True):
        t = time.time_ns()/1000000000
        dac.setvoltage(dac.vmax/2 + amplitude * math.sin(2*math.pi*freq*t))
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()
