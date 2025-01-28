from PIL import Image
from colour import Color
from sprite import Sprite

# heart_image = Image.open("heart.png")
# heart_image_pixels = heart_image.convert("RGB")
# rgb_pixel_value = heart_image_pixels.getpixel((0, 0))
# print(rgb_pixel_value) #Prints (255, 0, 0)

def image_to_sprites(image_path, cols, rows):
  image = Image.open(image_path)
  image_pixels = image.convert("RGB")

  sprite_width = image.width / cols
  sprite_height = image.height / rows

  print("sprite_width: ", sprite_width)
  print("sprite_height: ", sprite_height)

  if not sprite_width.is_integer() or not sprite_height.is_integer():
    raise Exception("Image dimensions must be divisible by ", cols, rows, "Image size: ", image.width, image.height)

  sprite_width = int(sprite_width)
  sprite_height = int(sprite_height)

  sprites = []

  for row in range(rows):
    for col in range(cols):
      sprite = Sprite(sprite_width, sprite_height)

      for sprite_pixel_y in range(sprite_height):
        for sprite_pixel_x in range(sprite_width):
          image_pixel_x = col * sprite_width + sprite_pixel_x
          image_pixel_y = row * sprite_height + sprite_pixel_y
          rgb_pixel_values = image_pixels.getpixel((image_pixel_x, image_pixel_y))
          rgb_pixel_values_normalized = tuple(value / 255 for value in rgb_pixel_values)
          print(f"{image_pixel_x}, {image_pixel_y}:", rgb_pixel_values_normalized)
          sprite.set_pixel(sprite_pixel_x, sprite_pixel_y, Color(rgb=(rgb_pixel_values_normalized)))

      sprites.append(sprite)

  return sprites

# cols = 8
# rows = 8

# sprites_per_row = heart_image.width / rows
# sprites_per_col = heart_image.height / cols

# if not sprites_per_row.is_integer() or not sprites_per_col.is_integer():
#   print("Image dimensions must be divisible by ", cols, rows)
#   exit()

# sprites_per_row = int(sprites_per_row)
# sprites_per_col = int(sprites_per_col)
# total_number_of_sprites = sprites_per_row * sprites_per_col
# sprites = []

# print("sprites per row: ", sprites_per_row)
# print("sprites per col: ", sprites_per_col)

# for sprite_row in range(sprites_per_col):
#   for sprite_col in range(sprites_per_row):
#     sprite = []
#     print("sprite: ", sprite_col, sprite_row)

#     for row in range(rows):
#       row_pixels = []
#       for col in range(cols):
#         pixel_x = sprite_col * cols + col
#         pixel_y = sprite_row * rows + row
#         print("Pixel: ", pixel_x, pixel_y)
#         rgb_pixel_value = heart_image_pixels.getpixel((pixel_x, pixel_y))
#         print(rgb_pixel_value)
#         row_pixels.append(rgb_pixel_value)
#       sprite.append(row_pixels)

#     sprites.append(sprite)

# sprites = image_to_sprites("heart.png", 8, 8)

# for sprite in sprites:
#   print("sprite")
#   sprite.print()
