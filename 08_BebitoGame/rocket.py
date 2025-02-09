import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from vector_2d import Vector2D

class Rocket(Updatable, Drawable):
  def __init__(self, color, position, canvas):
    self.color = color
    self.position = position
    self.canvas = canvas

    moving_box_direction = self._calculate_direction()
    moving_box_speed = random.randint(5, 15)

    self.moving_box = MovingBox(self.color, self.position, moving_box_direction, moving_box_speed, self.canvas)

  def _calculate_direction(self):
    if self.position.y == 0:
      return Vector2D(0, 1)

    if self.position.y == self.canvas.height - 1:
      return Vector2D(0, -1)

    if self.position.x == 0:
      return Vector2D(1, 0)

    if self.position.x == self.canvas.width - 1:
      return Vector2D(-1, 0)

    raise ValueError("Rocket position is not on the edge of the canvas:", str(self.position))
