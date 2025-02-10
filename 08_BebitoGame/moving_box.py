import time

from updatable import Updatable
from drawable import Drawable
from vector_2d import Vector2D
from canvas import Canvas
from color import Color

class MovingBox(Updatable, Drawable):
  def __init__(self, color, position, direction, speed, canvas, on_collision=None):
    self.color = color
    self.position = position
    self.direction = direction
    self.speed = speed
    self.canvas = canvas
    self.on_collision = on_collision

    Updatable.__init__(self)
    Drawable.__init__(self)

  def set_on_collision(self, callback):
    self.on_collision = callback

  def update(self, delta = 1.0):
    self.position += self.direction * (self.speed * delta)

    collision_detected = False

    if self.position.x < 0:
      self.position.x = 0
      collision_detected = True

    if self.position.x > self.canvas.width - 1:
      self.position.x = self.canvas.width - 1
      collision_detected = True

    if self.position.y < 0:
      self.position.y = 0
      collision_detected = True

    if self.position.y > self.canvas.height - 1:
      self.position.y = self.canvas.height - 1
      collision_detected = True

    if collision_detected and self.on_collision:
      self.on_collision()

  """
  Draws the object on the given canvas.

  Args:
    canvas (Canvas): The canvas to draw on.
  """
  def draw(self):
    # color_before = canvas[position_rounded]
    # canvas[position_rounded] = canvas[position_rounded].mix_color_burn(self.color, 0.5)
    # color_after = canvas[position_rounded]
    # print("color_before: ", color_before, "color_after: ", color_after)

    self.canvas[self.position.round()] = self.color

  def destroy(self):
    Updatable.destroy(self)
    Drawable.destroy(self)
