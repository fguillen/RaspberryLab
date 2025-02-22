from vector_2d import Vector2D
from color import Color

class Canvas:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.size = width * height
    self._pixels = []
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
      return self._pixels[position]
    elif isinstance(position, tuple):
      return self._pixels[position[0] + position[1] * self.width]
    elif isinstance(position, Vector2D):
      return self._pixels[position.x + position.y * self.width]
    else:
      raise TypeError("Invalid argument type in 'position': " + str(type(position)))

  """
  Sets the color of a pixel at the given position.

  Args:
    position (Vector2D): The (x, y) coordinates of the pixel.
    color (Color): The color to set the pixel to.
  """
  def __setitem__(self, position, color):
    if not isinstance(color, Color):
      raise TypeError("Invalid argument type in 'color': " + str(type(color)))

    if isinstance(position, int):
      self._pixels[position] = color
    elif isinstance(position, tuple):
      self._pixels[position[0] + position[1] * self.width] = color
    elif isinstance(position, Vector2D):
      self._pixels[position.x + position.y * self.width] = color
    else:
      raise TypeError("Invalid argument type in 'position': " + str(type(position)))


  def clear(self):
    self._pixels = [Color(0, 0, 0) for _ in range(self.width * self.height)]


  def fill(self, color):
    self._pixels = [color for _ in range(self.width * self.height)]


  def fade_out(self, factor):
    self._pixels = [color.fade_out(factor) for color in self._pixels]
