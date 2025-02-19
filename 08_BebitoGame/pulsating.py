import time

from updatable import Updatable
from drawable import Drawable
from vector_2d import Vector2D
# from button_mock import ButtonMock
from button import Button
from led import Led
from color import Color
from config import pins_leds, pins_buttons

class Pulsating(Updatable, Drawable):
  def __init__(self, name, canvas, on_completed=None, fps=2):
    self.name = name
    self.canvas = canvas
    self.color = Color.from_name(self.name)
    self.fps = fps

    self.button = self._init_button()
    self.led = self._init_led()

    self.on_completed = on_completed
    self.size = 2
    self.last_frame_at = time.time()

    self.button.set_on_button_pressed(lambda: self._completed())

    Updatable.__init__(self)
    Drawable.__init__(self)


  def set_on_completed(self, callback):
    self.on_completed = callback


  def update(self, delta = 1.0):
    if (self.last_frame_at + (1 / self.fps)) < time.time():
      self.last_frame_at = time.time()
      self.size -= 1
      if self.size < 0:
        self.size = 2


  def draw(self):
    for pixel in self._pixels_by_size():
      self.canvas[pixel] = self.color


  def destroy(self):
    self.led.destroy()
    self.button.destroy()
    Updatable.destroy(self)
    Drawable.destroy(self)


  def _completed(self):
    print(f">>>>>>>>>>>>>>>>>>>>> Pulsating.{self.name}._completed()")
    if self.on_completed:
      self.on_completed()

    self.destroy()


  def _init_button(self):
    button = Button(
      name=self.name,
      bcm_pin_num=pins_buttons[self.name],
      on_button_pressed=lambda: self._launch_rocket()
    )

    return button


  def _init_led(self):
    led = Led(
      name=self.name,
      bcm_pin_num=pins_leds[self.name]
    )
    led.start_pulsating(1)
    return led


  def _pixels_by_size(self):
    result = []

    if self.size == 0:
      return result

    range_block = range(3 - (self.size - 1), 4 + self.size)

    for x in range_block:
      for y in range_block:
        result.append(Vector2D(x, y))

    return result
