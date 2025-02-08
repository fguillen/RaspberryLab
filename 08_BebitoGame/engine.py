import time
import random

import board
import neopixel
import RPi.GPIO as GPIO
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

# from neopixel_mock.neopixel_mock import NeoPixelMock
# from neopixel_mock.board_mock import BoardMock

from vector_2d import Vector2D
from wanderer import Wanderer
from button import Button
from color import Color
from canvas import Canvas

print("GPIO.getmode():", GPIO.getmode(), GPIO.BCM, GPIO.BOARD)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

class Engine:
  def __init__(self, limit):
    self.limit = limit
    self.wanderers = []
    self.buttons = []

    self.board = board
    self.leds = neopixel.NeoPixel(self.board.D10, 64, brightness=0.2, auto_write=False)
    self.pixel_grid = PixelGrid(self.leds, 8, 8, orientation=HORIZONTAL, alternating=True)
    self.fps = 0
    self.fade_out_factor = 0.95
    self.canvas = Canvas(8, 8)

    self.last_updated_at = time.time()

    self._init_buttons()

  def add_wanderer(self, speed=10):
    wanderer = Wanderer(Color.random(), self.limit, speed)
    self.wanderers.append(wanderer)

  def update(self):
    delta = self._delta()

    for wanderer in self.wanderers:
      wanderer.update(self._delta())

    if delta > 0:
      self.fps = 1 / delta

    self.last_updated_at = time.time()
    # print("                          Delta: ", delta, "FPS: ", self.fps)

    for button in self.buttons:
      print(button)

  def draw(self):
    self.canvas.fade_out(self.fade_out_factor)

    for wanderer in self.wanderers:
      wanderer.draw(self.canvas)

    # render Canvas to PixelGrid
    for x in range(self.pixel_grid.width):
      for y in range(self.pixel_grid.height):
        color = self.canvas[x, y]
        self.pixel_grid[x, y] = color.rgb_rounded()

    self.pixel_grid.show()

  def _delta(self):
    now = time.time()
    delta = now - self.last_updated_at
    return delta

  def _init_buttons(self):
    pinsButtons = {
      "red": 33,
      "green": 35,
      "blue": 37,
      "white": 31
    }

    for key in pinsButtons:
      button = Button(name=key, pin_on_board=pinsButtons[key])
      self.buttons.append(button)


# create a new Engine and call draw
engine = Engine(Vector2D(7, 7))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))
# engine.add_wanderer(speed=random.randint(5, 15))
# engine.add_wanderer(speed=random.randint(5, 15))

try:
  while True:
    engine.update()
    engine.draw()
    time.sleep(0.01)

except KeyboardInterrupt:
  for button in self.buttons:
    button.on_destroy()

  print("bye!")
