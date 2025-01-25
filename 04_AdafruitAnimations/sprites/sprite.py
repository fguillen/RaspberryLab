from colour import Color

# Class that contents a matrix of pixels
# Each pixel is a color object
# The matrix is a 2D array of pixels
# The constructor receives the width and height of the matrix
# The matrix is filled with black pixels by default
# The matrix can be filled with a color by calling the `set_pixel` method with the x, y and color arguments
# A pixel color can be retrieved by calling the `get_pixel` method with the x and y arguments

class Sprite:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.matrix = [[Color(rgb=(0, 0, 0)) for _ in range(width)] for _ in range(height)]

  def set_pixel(self, x, y, color):
    self.matrix[y][x] = color

  def get_pixel(self, x, y):
    return self.matrix[y][x]

  def print(self):
    for row in range(self.height):
      for col in range(self.width):
        pixel = self.matrix[row][col]
        print(f'\033[48;2;{int(pixel.red * 255)};{int(pixel.green * 255)};{int(pixel.blue * 255)}m \033[0m', end='')
      print()
