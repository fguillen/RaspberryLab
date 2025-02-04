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
    self.fps = 0

    self.last_updated_at = time.time()

  def add_wanderer(self, speed=10):
    wanderer = Wanderer(self._random_color(), self.limit, speed)
    self.wanderers.append(wanderer)

  def update(self):
    for wanderer in self.wanderers:
      wanderer.update(self._delta())

    delta = self._delta()

    if delta > 0:
      self.fps = 1 / delta

    self.last_updated_at = time.time()
    print("                          Delta: ", delta, "FPS: ", self.fps)

  def draw(self):
    self._fade_out_pixels()

    for wanderer in self.wanderers:
      wanderer.draw(self.pixel_grid)

    self.pixel_grid.show()

  def _delta(self):
    now = time.time()
    delta = now - self.last_updated_at
    return delta

  def _random_color(self):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

  def _fade_out_pixels(self):
    for x in range(self.pixel_grid.width):
      for y in range(self.pixel_grid.height):
        color = self.pixel_grid[x][y]
        faded_color = tuple([int(c * 0.9) for c in color])
        self.pixel_grid[x, y] = faded_color

# create a new Engine and call draw
engine = Engine(Vector2D(7, 7))
engine.add_wanderer(speed=20)

while True:
  engine.update()
  engine.draw()
  time.sleep(0.1)
