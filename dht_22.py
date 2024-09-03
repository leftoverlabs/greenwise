import time
import automationhat
from PIL import Image, ImageDraw
import st7735
import Adafruit_DHT  # Import the DHT library

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
    spi_speed_hz=4000000,
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height
img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

disp.display(img)

# Define the sensor type and the pin connected to the sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Change to the pin number you have connected the DHT-22 sensor to

while True:
    # Reading the DHT22 sensor
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # Check if data is received from the sensor
    if humidity is not None and temperature is not None:
        # Clear the screen
        draw.rectangle((0, 0, WIDTH, HEIGHT), (0, 0, 0))

        # Display the temperature and humidity values
        draw.text((10, 10), f"Temp: {temperature:.1f}C", fill=(255, 255, 255))
        draw.text((10, 30), f"Humidity: {humidity:.1f}%", fill=(255, 255, 255))

        # Update the display
        disp.display(img)

    else:
        print("Failed to retrieve data from the sensor")

    time.sleep(1)
