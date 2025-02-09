import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox

class Rocket(Updatable, Drawable):
  def __init__(self, color, position, canvas):
    self.color = color
    self.position = position
    self.canvas = canvas

    moving_box_direction = self._calculate_direction(self.position)
    moving_box_speed = random.randint(5, 15)

    def _init_moving_box

    self.moving_box = MovingBox(self.color, self.position, direction, speed, limit)
