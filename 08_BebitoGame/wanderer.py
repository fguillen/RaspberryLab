import random

from vector_2d import Vector2D
from moving_box import MovingBox
from button import Button
from color import Color
from rocket import Rocket
from blinking_led import BlinkingLed

from config import pins_buttons, pins_leds

class Wanderer(MovingBox):
  def __init__(self, name, canvas, speed):
    position = self._random_position(canvas)
    direction = self._random_direction(position, canvas)

    self.name = name
    self.button_bcm_pin_num = pins_buttons[name]
    self.led_bcm_pin_num = pins_leds[name]
    self.canvas = canvas
    self.button = self._init_button()
    self.color = Color.from_name(self.name)
    self.active = False

    super().__init__(self.color, position, direction, speed, canvas=self.canvas, on_collision=self.on_collision)


  def _random_position(self, canvas):
    border_positions = self._border_positions(canvas)
    position = random.choice(border_positions)
    return position


  def _random_direction(self, position, canvas):
    if position.y == 0 or position.y == canvas.height:
      return random.choice([Vector2D(1, 0), Vector2D(-1, 0)])
    else:
      return random.choice([Vector2D(0, 1), Vector2D(0, -1)])


  def set_active(self, value):
    self.canvas.fill(self.color)
    self.active = True


  def on_collision(self):
    new_direction = self.direction.rotate_90_degrees_clockwise()
    if self._is_valid_direction(new_direction):
      self.direction = new_direction
    else:
      self.direction = self.direction.rotate_90_degrees_counterclock()


  def _is_valid_direction(self, direction):
    next_position = self.position + direction
    return (next_position.x >= 0 and
        next_position.x < self.canvas.width and
        next_position.y >= 0 and
        next_position.y < self.canvas.height)


  def _border_positions(self, canvas):
    border_positions = []
    for row in [0, canvas.height - 1]:
      for col in range(0, canvas.width):
        border_positions.append(Vector2D(col, row))

    for row in range(0, canvas.height):
      for col in [0, canvas.width - 1]:
        border_positions.append(Vector2D(col, row))

    border_positions = list(set(border_positions)) # remove duplicates
    return border_positions


  def _init_button(self):
    print(f"Wanderer[{self.name}]._init_button()")
    button = Button(
        name=self.name,
        bcm_pin_num=self.button_bcm_pin_num,
        on_button_pressed=lambda: self._on_button_pressed()
    )

    return button


  def _on_button_pressed(self):
    if self.active:
      self._launch_rocket()
      self._blinking()


  def _launch_rocket(self):
    Rocket(self.color, self.position.round(), self.canvas)


  def _blinking(self):
    print(f"Wanderer[{self.name}]._blinking")
    BlinkingLed(
      bcm_pin_num=self.led_bcm_pin_num,
      cycle_duration=0.1,
      duration_seconds=1
    )
