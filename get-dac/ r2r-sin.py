import r2r_dac as r2r
import time
import math

amplitude = 3.2
freq = 10
sampling_freq = 1000

dac = r2r.R2R_DAC([22,27,17,26,25,21,20,16], 3.183)


try:
    while(True):
        t = time.time_ns()/1000000000
        dac.set_voltage(dac.dynamic_range/2 + amplitude * math.sin(2*math.pi*freq*t))
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()
