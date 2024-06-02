#!/usr/bin/env python3

import sys
import time

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
    spi_speed_hz=4000000
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

    # Create a blank image with a white background
    image = Image.new("RGB", (disp.width, disp.height), "white")
    draw = ImageDraw.Draw(image)

    # Draw humidity value
    draw.text((10, 10), f"Humidity: {humidity}%", fill="black")

    # Draw the image to the display
    disp.display(image)

    time.sleep(0.25)
