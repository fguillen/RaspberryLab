class MockNeoPixel:
    def __init__(self, pin, num_pixels, cols=8, rows=8):
        self.num_pixels = num_pixels
        self.pixels = [(0, 0, 0)] * num_pixels
        self.rows = rows
        self.cols = cols

    def show(self):
        print(f"\r\033[{self.rows}A", end="")
        for row in range(self.rows):
          for col in range(self.cols):
            pixel = self.pixels[(self.cols * row) + col]
            print(f'\033[48;2;{int(pixel[0])};{int(pixel[1])};{int(pixel[2])}m \033[0m', end='')
          print()

    def fill(self, color):
        self.pixels = [color] * self.num_pixels

    def __getitem__(self, index):
        return self.pixels[index]


class MockBoard:
    D18 = "D18"

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
