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
    self.color_names_iterator = iter(pins_buttons)
    self.test_screen_started_at = None
    self.test_screen_seconds = test_screen_seconds
    self.on_complete = on_complete
    self.elements = {}
    self.actual_color_name = None

    self._init_buttons()
    self._init_leds()

    Updatable.__init__(self)
    Drawable.__init__(self)

    self._next_color()


  def _next_color(self):
    if self.actual_color_name != None:
      self.elements[self.actual_color_name]["led"].destroy
      self.elements[self.actual_color_name]["button"].destroy

    self.actual_color_name = next(self.color_names_iterator, None)

    if self.actual_color_name == None:
      self._test_screen()
      return

    self.elements[self.actual_color_name]["led"].start_pulsating(1.0)
    self.elements[self.actual_color_name]["button"].set_on_button_pressed(lambda: self._next_color())


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

    self.canvas.fill(Color.from_name("magenta"))


  def _init_buttons(self):
    for color_name in pins_buttons:
      button = Button(
        name=color_name,
        bcm_pin_num=pins_buttons[color_name]
      )

      self.elements.setdefault(color_name, {})
      self.elements[color_name]["button"] = button



  def _init_leds(self):
    for color_name in pins_leds:
      led = Led(
        name=color_name,
        bcm_pin_num=pins_leds[color_name]
      )

      self.elements.setdefault(color_name, {})
      self.elements[color_name]["led"] = led
