import random

from vector_2d import Vector2D
from moving_box import MovingBox

class Wanderer(MovingBox):
  def __init__(self, color, canvas, speed=10):
    position = self._random_position(canvas)
    direction = self._random_direction(position, canvas)
    speed = speed

    self.canvas = canvas

    super().__init__(color, position, direction, speed, canvas=self.canvas)

  def _random_position(self, canvas):
    border_positions = self._border_positions(canvas)
    position = random.choice(border_positions)
    return position

  def _random_direction(self, position, canvas):
    if position.y == 0 or position.y == canvas.height:
      return random.choice([Vector2D(1, 0), Vector2D(-1, 0)])
    else:
      return random.choice([Vector2D(0, 1), Vector2D(0, -1)])

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
    for row in [0, canvas.height]:
      for col in range(0, canvas.width):
        border_positions.append(Vector2D(col, row))

    for row in range(0, canvas.height):
      for col in [0, canvas.width]:
        border_positions.append(Vector2D(col, row))

    border_positions = list(set(border_positions)) # remove duplicates
    return border_positions
