from gpiozero import MCP3008
import time

try:
    while True:
        ad_ch0 = MCP3008(0)
        print(ad_ch0.value * 100)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
