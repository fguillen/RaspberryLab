import time
import random

# import board
# import neopixel
from adafruit_led_animation.grid import PixelGrid, VERTICAL, HORIZONTAL

from neopixel_mock.neopixel_mock import NeoPixelMock
from neopixel_mock.board_mock import BoardMock

from updatable import Updatable
from drawable import Drawable
from vector_2d import Vector2D
from wanderer import Wanderer
# from button import Button
from button_mock import ButtonMock
from color import Color
from canvas import Canvas

delay = 0.01

class Engine:
  def __init__(self, limit):
    self.limit = limit
    self.wanderers = []
    self.buttons = []

    self.board = BoardMock()
    self.leds = NeoPixelMock(self.board.D10, 64, brightness=0.5, auto_write=False, rows=8)
    self.pixel_grid = PixelGrid(self.leds, 8, 8, orientation=HORIZONTAL, alternating=False)
    self.fps = 0
    self.fade_out_factor = 0.95
    self.canvas = Canvas(8, 8)

    self.last_updated_at = time.time()

    self._init_buttons()

  def add_wanderer(self, color, speed=10):
    wanderer = Wanderer(color, self.limit, speed)
    self.wanderers.append(wanderer)

  def update(self):
    delta = self._delta()

    for updatable in Updatable.all:
      updatable.update(self._delta())

    for button in self.buttons:
      if button.pressed_in_the_last_frame:
        print("button.pressend_in_the_last_frame")
        self.canvas.fill(Color.from_name(button.name))

    if delta > 0:
      self.fps = 1 / delta

    self.last_updated_at = time.time()

    # Debug
    # print("                          Delta: ", delta, "FPS: ", self.fps)
    # for button in self.buttons:
    #   print(button)

  def draw(self):
    self.canvas.fade_out(self.fade_out_factor)

    for drawable in Drawable.all:
      drawable.draw(self.canvas)

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
    # pinsButtons = {
    #     "maroon": 13,
    #     "green": 19,
    #     "teal": 26,
    #     "white": 6
    # }

    keysButtons = {
        "maroon": 14,
        "green": 1,
        "teal": 2,
        "white": 3
    }

    for key in keysButtons:
      button = ButtonMock(name=key, key=keysButtons[key])
      self.buttons.append(button)
      self.add_wanderer(Color.from_name(key), speed=random.randint(5, 15))


# create a new Engine and call draw
engine = Engine(Vector2D(7, 7))

try:
  while True:
    engine.update()
    engine.draw()
    time.sleep(delay)

except KeyboardInterrupt:
  for button in engine.buttons:
    button.on_destroy()

  print("bye!")
