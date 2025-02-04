import random

from vector_2d import Vector2D
from moving_box import MovingBox

class Wanderer(MovingBox):
  def __init__(self, color, limit, speed=10):
    position = self._random_position(limit)
    direction = self._random_direction(position, limit)
    speed = speed

    super().__init__(color, position, direction, speed, limit)

  def _random_position(self, limit):
    border_positions = self._border_positions(limit)
    position = random.choice(border_positions)
    return position

  def _random_direction(self, position, limit):
    if position.y == 0 or position.y == limit.y:
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
        next_position.x <= self.limit.x and
        next_position.y >= 0 and
        next_position.y <= self.limit.y)

  def _border_positions(self, limit):
    border_positions = []
    for row in [0, limit.y]:
      for col in range(0, limit.x + 1):
        border_positions.append(Vector2D(col, row))

    for row in range(0, limit.y + 1):
      for col in [0, limit.x]:
        border_positions.append(Vector2D(col, row))

    border_positions = list(set(border_positions)) # remove duplicates
    return border_positions
