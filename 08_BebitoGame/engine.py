import time
# import board
# import neopixel
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

from neopixel_mock.neopixel_mock import NeoPixelMock
from neopixel_mock.board_mock import BoardMock

from vector_2d import Vector2D
from wanderer import Wanderer
import random


class Engine:
  def __init__(self, limit):
    self.limit = limit
    self.wanderers = []

    self.board = BoardMock()
    self.pixels = NeoPixelMock(self.board.D10, 64, auto_write=False, rows=8)
    self.pixel_grid = PixelGrid(self.pixels, 8, 8, orientation=HORIZONTAL, alternating=False)

    self.last_updated_at = time.time()

  def add_wanderer(self):
    wanderer = Wanderer(self._random_color(), self.limit)
    self.wanderers.append(wanderer)

  def update(self):
    for wanderer in self.wanderers:
      wanderer.update(self._delta())

    self.last_updated_at = time.time()

  def draw(self):
    for wanderer in self.wanderers:
      wanderer.draw(self.pixel_grid)

    self.pixel_grid.show()

  def _delta(self):
    now = time.time()
    delta = now - self.last_updated_at
    return delta

  def _random_color(self):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# create a new Engine and call draw
engine = Engine(Vector2D(7, 7))
engine.add_wanderer()

while True:
  engine.update()
  engine.draw()
  time.sleep(0.1)
