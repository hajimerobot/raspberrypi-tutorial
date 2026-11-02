from gpiozero import MCP3008

ad_ch0 = MCP3008(0)
print(ad_ch0.value * 3.3)
