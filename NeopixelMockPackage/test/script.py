from mock_board import MockBoard
from mock_neopixel import MockNeoPixel

board = MockBoard()

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import AMBER

pixel_pin = board.D18
pixel_num = 64
pixels = MockNeoPixel(pixel_pin, pixel_num)

pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)

while True:
    pulse.animate()
    # Add a small delay to simulate real-time behavior
    import time
    time.sleep(0.1)
