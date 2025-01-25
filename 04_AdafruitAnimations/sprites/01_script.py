import board
import neopixel
from sprites_animation import SpritesAnimation

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

demo_anim = SpritesAnimation(pixels, speed=0.2, image_path="creatures.png", num_columns=10, num_rows=15, sprite_ini=128, sprite_end=137)

while True:
	demo_anim.animate()
