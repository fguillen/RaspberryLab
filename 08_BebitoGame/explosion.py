import random

from updatable import Updatable
from drawable import Drawable
from moving_box import MovingBox
from vector_2d import Vector2D

class Explosion(Updatable, Drawable):
  def __init__(self, color, position, speed, canvas):
    self.color = color
    self.position = position
    self.canvas = canvas
    self.speed = speed
    self.moving_boxes = self._create_moving_boxes()

    Updatable.__init__(self)
    Drawable.__init__(self)

    self.canvas.fill(self.color)

  def _create_moving_boxes(self):
    directions = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]

    moving_boxes = []

    for direction in directions:
      moving_box = MovingBox(
        self.color,
        self.position,
        Vector2D(direction[0], direction[1]),
        self.speed,
        self.canvas
      )
      moving_box.set_on_collision(lambda mb=moving_box: self._remove_moving_box(mb))
      moving_boxes.append(moving_box)

    return moving_boxes

  def _remove_moving_box(self, moving_box):
    self.moving_boxes.remove(moving_box)
    moving_box.destroy()

  def destroy(self):
    for moving_box in self.moving_boxes:
      moving_box.destroy()

    Updatable.destroy(self)
    Drawable.destroy(self)
