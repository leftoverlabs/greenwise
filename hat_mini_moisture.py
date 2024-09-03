import time
import automationhat
from PIL import Image, ImageDraw
import st7735

print(
"""
    Press CTRL+C to exit.
"""
)

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

WIDTH = disp.width
HEIGHT = disp.height
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

disp.display(img)

def convert_to_humidity(analog_value):
    min_value = 1.05 
    max_value = 2.09 
    return 100 - ((analog_value - min_value) / (max_value - min_value)) * 100.0

while True:
    adc_value = automationhat.analog.one.read()
    humidity = int(convert_to_humidity(adc_value))
    draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))  # Clear the screen
    draw.text((10, 10), f'Humidity: {humidity}%', fill=(255, 255, 255))
    disp.display(img)
    time.sleep(1)
