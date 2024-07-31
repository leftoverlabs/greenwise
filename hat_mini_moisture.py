#!/usr/bin/env python3

import sys
import time

import automationhat
from PIL import Image, ImageDraw
import st7735
import Adafruit_DHT

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

# Define the sensor type and the connected pin
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the DHT22 is connected


def convert_to_humidity(analog_value):
    min_value = 1.05  # value when the sensor is fully submerged
    max_value = 2.09  # value when the sensor is fully unsubmerged and dry
    # We invert the output here
    return 100 - ((analog_value - min_value) / (max_value - min_value)) * 100.0


while True:
    # Read the analog humidity sensor
    adc_value = automationhat.analog.one.read()
    humidity = int(convert_to_humidity(adc_value))

    # Read the DHT22 sensor
    dht_humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if dht_humidity is not None and temperature is not None:
        dht_humidity = int(dht_humidity)
        temperature = int(temperature)
    else:
        dht_humidity = "Error"
        temperature = "Error"

    # Create a blank image with a white background
    image = Image.new("RGB", (disp.width, disp.height), "white")
    draw = ImageDraw.Draw(image)

    # Draw values
    draw.text((10, 10), f"Humidity: {humidity}%", fill="black")
    draw.text((10, 30), f"Temp: {temperature}C", fill="black")
    draw.text((10, 50), f"DHT Humidity: {dht_humidity}%", fill="black")

    # Draw the image to the display
    disp.display(image)

    time.sleep(0.25)
