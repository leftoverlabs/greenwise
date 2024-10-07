from PIL import Image, ImageDraw

# Initialize display.
disp.begin()
 
WIDTH = disp.width
HEIGHT = disp.height
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
 
disp.display(img)
