import time
import board
import neopixel
# import colorsys
# import random
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

pixels = neopixel.NeoPixel(board.D10, 64, brightness=0.2, auto_write=False)
# pixels[0] = (10, 0, 0)
# pixels[8] = (10, 10, 0)
# pixels.show()

pixel_grid = PixelGrid(pixels, 8, 8, orientation=HORIZONTAL, alternating=True)
pixel_grid[7, 0] = (10, 0, 0)
pixel_grid[7, 1] = (0, 10, 0)
pixel_grid[7, 2] = (0, 0, 10)
pixels.show()

# while True:
#   time.sleep(10)
