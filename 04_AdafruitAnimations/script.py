import board
import neopixel
from adafruit_led_animation.animation.blink import Blink
import adafruit_led_animation.color as color

# Works on Circuit Playground Express and Bluefruit.
# For other boards, change board.NEOPIXEL to match the pin to which the NeoPixels are attached.
pixel_pin = board.D10
# Change to match the number of pixels you have attached to your board.
num_pixels = 64

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
blink = Blink(pixels, 0.5, color.PURPLE)

while True:
    blink.animate()
