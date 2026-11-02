from gpiozero import MCP3008
import time

ad_ch0 = MCP3008(0)

try:
    while True:
        print(ad_ch0.value * 100)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
