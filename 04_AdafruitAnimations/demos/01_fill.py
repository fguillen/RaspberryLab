import board
import neopixel
from demo_animation import DemoAnimation

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

demo_anim = DemoAnimation(pixels, 0.5, (255, 0, 255))

while True:
	demo_anim.animate()
