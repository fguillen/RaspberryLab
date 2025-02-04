import time
import random

# import board
# import neopixel
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

from neopixel_mock.neopixel_mock import NeoPixelMock
from neopixel_mock.board_mock import BoardMock

from vector_2d import Vector2D
from wanderer import Wanderer
from color import Color
from canvas import Canvas



class Engine:
  def __init__(self, limit):
    self.limit = limit
    self.wanderers = []

    self.board = BoardMock()
    self.leds = NeoPixelMock(self.board.D10, 64, auto_write=False, rows=8)
    self.pixel_grid = PixelGrid(self.leds, 8, 8, orientation=HORIZONTAL, alternating=False)
    self.fps = 0
    self.fade_out_factor = 0.95
    self.canvas = Canvas(8, 8)

    self.last_updated_at = time.time()

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

  def draw(self):
    self._fade_out_pixels()

    for wanderer in self.wanderers:
      wanderer.draw(self.canvas)

    # render Canvas to PixelGrid
    for x in range(self.pixel_grid.width):
      for y in range(self.pixel_grid.height):
        color = self.canvas[x, y]
        print("color: ", str(type(color)), color)
        self.pixel_grid[x, y] = color.rgb()

    self.pixel_grid.show()

  def _delta(self):
    now = time.time()
    delta = now - self.last_updated_at
    return delta

  def _fade_out_pixels(self):
    for i in range(len(self.canvas.pixels)):
      color = self.canvas.pixels[i]
      faded_color = Color.from_rgb([int(c * self.fade_out_factor) for c in color.rgb()])
      self.canvas.pixels[i] = faded_color

# create a new Engine and call draw
engine = Engine(Vector2D(7, 7))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))
engine.add_wanderer(speed=random.randint(5, 15))

while True:
  engine.update()
  engine.draw()
  time.sleep(0.01)
