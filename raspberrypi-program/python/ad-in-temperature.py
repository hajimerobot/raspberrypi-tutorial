from gpiozero import MCP3008
import time

try:
    while True:
        ad_ch0 = MCP3008(0)
        ad_volt = ad_ch0.value * 3.3
        # LM61C
        temperature = (ad_volt - 0.6) / 0.01
        # MCP9700A
        # temperature = (ad_volt - 0.5) / 0.01
        print(temperature)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
