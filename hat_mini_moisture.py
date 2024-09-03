import automationhat
from PIL import Image, ImageDraw
import st7735

print("""input.py
This Automation HAT Mini example displays the status of
the three 24V-tolerant digital inputs.
Press CTRL+C to exit.
""")

# Create ST7735 LCD display class.
disp = st7735.ST7735(
    port=0,
    cs=st7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=25,
    rotation=270,
    spi_speed_hz=1000000
)


# Initialize display.
disp.begin()


def convert_to_humidity(analog_value):
    min_value = 1.05  # value when the sensor is fully submerged
    max_value = 2.09  # value when the sensor is fully unsubmerged and dry
    # We invert the output here 
    return 100 - ((analog_value - min_value) / (max_value - min_value)) * 100.0


while True:
    adc_value = automationhat.analog.one.read()
    humidity = int(convert_to_humidity(adc_value))
