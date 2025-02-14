import time

from button import Button
from led import Led
from color import Color
from color_names import ColorNames
from updatable import Updatable
from drawable import Drawable

from config import pins_buttons, pins_leds

class CheckElements(Updatable, Drawable):
  def __init__(self, canvas, test_screen_seconds=1, on_complete=None):
    self.canvas = canvas
    self.buttons = self._init_buttons()
    self.leds = self._init_leds()
    self.color_names_iterator = iter(pins_buttons)
    self.test_screen_started_at = None
    self.test_screen_seconds = test_screen_seconds
    self.on_complete = on_complete

    Updatable.__init__(self)
    Drawable.__init__(self)

    self._next_color()


  def _next_color(self):
    next_color_name = next(self.color_names_iterator, None)

    if next_color_name == None:
      self._test_screen()
      return

    self.elments[next_color_name]["led"].pulsate(1.0)
    self.elments[next_color_name]["button"].set_on_button_pressed(lambda: self._next_color())


  def _test_screen(self):
    self.test_screen_started_at = time.time()


  def update(self, delta):
    if self.test_screen_started_at == None:
      return

    if time.time() > self.test_screen_started_at + self.test_screen_seconds:
      self.on_complete()


  def draw(self):
    if self.test_screen_started_at == None:
      return

    self.canvas.fill(Color.from_name(ColorNames.magenta))


  def _init_buttons(self):
    buttons = {}

    for color_name in pins_buttons:
      button = Button(
        name=self.color_name,
        bcm_pin_num=pins_buttons[color_name]
      )

      buttons.setdefault(color_name, {})
      buttons[color_name]["button"] = button

    return buttons


  def _init_leds(self):
    leds = {}

    for color_name in pins_leds:
      led = Led(
        name=self.color_name,
        bcm_pin_num=pins_leds[color_name]
      )

      leds.setdefault(color_name, {})
      leds[color_name]["led"] = led

    return leds
