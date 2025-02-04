from vector_2d import Vector2D
from color import Color

class Canvas:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.pixels = []
    self.clear()

  """
  Retrieve the pixel value at the given position.

  Args:
    position (Vector2D): The (x, y) coordinates of the pixel to retrieve.

  Returns:
    The value of the pixel at the specified position.
  """
  def __getitem__(self, position):
    if isinstance(position, int):
      return self.pixels[position]
    if isinstance(position, tuple):
      return self.pixels[position[0] + position[1] * self.width]
    if isinstance(position, Vector2D):
      return self.pixels[position.x + position.y * self.width]
    else:
      raise TypeError("Invalid argument type in 'position': " + str(type(position)))

  """
  Sets the color of a pixel at the given position.

  Args:
    position (Vector2D): The (x, y) coordinates of the pixel.
    color (Color): The color to set the pixel to.
  """
  def __setitem__(self, position, color):
    print("Canvas.__setitem__", position, color)
    if not isinstance(color, Color):
      raise TypeError("Invalid argument type in 'color': " + str(type(color)))

    self.pixels[position.x + position.y * self.width] = color

  def clear(self):
    self.pixels = [Color(0, 0, 0) for _ in range(self.width * self.height)]

  def fill(self, color):
    self.pixels = [color for _ in range(self.width * self.height)]
