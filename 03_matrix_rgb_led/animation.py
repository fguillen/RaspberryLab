from image_to_sprites import image_to_sprites


# Create a class Animation that receives an
# `image_path`, `num_columns`, `num_rows`, `sprite_ini`, `sprite_end`
# The class uses the function `image_to_sprites.py` to get the image,
# generate the sprites and select the ones between `sprite_ini` and `sprite_end`
#
# The class has a method to get each sprite of the animation
# Example usage
class Animation:
  def __init__(self, image_path, num_columns, num_rows, sprite_ini, sprite_end):
    self.image_path = image_path
    self.num_columns = num_columns
    self.num_rows = num_rows
    self.sprite_ini = sprite_ini
    self.sprite_end = sprite_end
    self.sprites = self._generate_sprites()

  def _generate_sprites(self):
    sprites = image_to_sprites(self.image_path, self.num_columns, self.num_rows)
    return sprites[self.sprite_ini:self.sprite_end + 1]

  def get_sprite(self, index):
    if index < 0 or index >= len(self.sprites):
      raise IndexError("Sprite index out of range")
    return self.sprites[index]


if __name__ == "__main__":
  animation = Animation("creatures.png", 10, 15, 0, 9)
  try:
    for i in range(11):
      sprite = animation.get_sprite(i)
      print(f"Sprite {i}: {sprite}")
      sprite.print()
  except IndexError as e:
    print(e)
