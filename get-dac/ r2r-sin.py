import r2r_dac as r2r
import time
import math

amplitude = 3
freq = 100
sampling_freq = 10000

dac = r2r.R2R_DAC([22,27,17,26,25,21,20,16], 3.3)


try:
    while(True):
        t = time.time_ns()/1000000000
        dac.setvoltage(dac.vmax/2 + amplitude * math.sin(2*math.pi*freq*t))
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()
