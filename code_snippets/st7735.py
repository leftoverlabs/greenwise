from PIL import Image, ImageDraw
import st7735

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

# Initialise display Width and Height defaults
WIDTH = disp.width 
HEIGHT = disp.height

# We create an Image using the Pillow library
# https://www.rapidtables.com/web/color/RGB_Color.html
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

disp.display(img)
