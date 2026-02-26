import mcp4725_driver
import math
import time

amplitude = 1.5
freq = 100
sampling_freq = 10000

dac = mcp4725_driver.MCP4725(4.2)

try:
    while(True):
        t = time.time_ns()/1000000000
        dac.set_voltage(dac.dynamic_range/2 + amplitude * math.sin(2*math.pi*freq*t))
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()
