import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from explosion import Explosion
from vector_2d import Vector2D

class Rocket(Updatable):
  def __init__(self, color, position, canvas):
    self.color = color
    self.position = position
    self.canvas = canvas
    self.direction = self._calculate_direction()
    self.speed = random.randint(5, 15)
    self.explosion_position = self._calculate_explosion_position()

    self.moving_box = MovingBox(self.color, self.position, self.direction, self.speed, self.canvas)

    super().__init__()

  def update(self, delta = 1.0):
    if self.moving_box.position.round() == self.explosion_position:
      Explosion(self.color, self.moving_box.position, self.speed, self.canvas)
      self.moving_box.destroy()
      Updatable.destroy(self)


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

  def _calculate_explosion_position(self):
    steps = random.randint(1, 7) # 1 to 6
    result = self.position + (self.direction * steps)
    return result
