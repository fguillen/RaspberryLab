import board
import neopixel
from sprites_animation import SpritesAnimation

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.02, auto_write=False)

demo_anim = SpritesAnimation(pixels, speed=0.4, image_path="heart.png", num_columns=2, num_rows=1, sprite_ini=0, sprite_end=1)

while True:
	demo_anim.animate()
