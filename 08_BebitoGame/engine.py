import time
import random

# import board
# import neopixel
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

from neopixel_mock.neopixel_mock import NeoPixelMock
from neopixel_mock.board_mock import BoardMock

from config import pins_buttons
from updatable import Updatable
from drawable import Drawable
from wanderer import Wanderer
from canvas import Canvas
from pulsating_sequence import PulsatingSequence

class Engine():
  def __init__(self):
    self.wanderers = []
    self.pulsatings = []

    self.board = BoardMock()
    self.leds = NeoPixelMock(self.board.D10, 64, brightness=0.5, auto_write=False, rows=8)
    self.pixel_grid = PixelGrid(self.leds, 8, 8, orientation=HORIZONTAL, alternating=False)
    self.fps = 0
    self.fade_out_factor = 0.95
    self.canvas = Canvas(8, 8)

    self.last_updated_at = time.time()




    # self._init_wanderers()
    self._init_pulsating_sequence()


  def update(self):
    delta = self._delta()

    for updatable in Updatable.all:
      updatable.update(self._delta())

    if delta > 0:
      self.fps = 1 / delta

    self.last_updated_at = time.time()

    # Debug
    # print("                          Delta: ", delta, "FPS: ", self.fps)

  def draw(self):
    self.canvas.fade_out(self.fade_out_factor)

    for drawable in Drawable.all:
      drawable.draw()

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

  def _init_wanderers(self):
    for key in pins_buttons:
      wanderer = Wanderer(key, self.canvas, speed=random.randint(5, 15), bcm_pin_num=pins_buttons[key])
      self.wanderers.append(wanderer)

  def _init_pulsating_sequence(self):
    pulsating = PulsatingSequence("green", self.canvas)

    # for key in self.pins_buttons:
    #   pulsating = Pulsating(key, self.canvas, bcm_pin_num=self.pins_buttons[key])
    #   self.pulsatings.append(pulsating)
