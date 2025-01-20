from PIL import Image

# heart_image = Image.open("heart.png")
# heart_image_rgb = heart_image.convert("RGB")
# rgb_pixel_value = heart_image_rgb.getpixel((0, 0))
# print(rgb_pixel_value) #Prints (255, 0, 0)

def extract_frames(image_path, pixels_per_column, pixels_per_row):
  image = Image.open(image_path)
  image_rgb = image.convert("RGB")

  frames_per_row = image.width / pixels_per_row
  frames_per_col = image.height / pixels_per_column

  if not frames_per_row.is_integer() or not frames_per_col.is_integer():
    print("Image dimensions must be divisible by ", pixels_per_column, pixels_per_row)
    exit()

  frames_per_row = int(frames_per_row)
  frames_per_col = int(frames_per_col)

  frames = []

  for frame_row in range(frames_per_col):
    for frame_col in range(frames_per_row):
      frame = []

      for row in range(pixels_per_row):
        row_pixels = []
        for col in range(pixels_per_column):
          pixel_x = frame_col * pixels_per_column + col
          pixel_y = frame_row * pixels_per_row + row
          rgb_pixel_value = image_rgb.getpixel((pixel_x, pixel_y))
          row_pixels.append(rgb_pixel_value)
        frame.append(row_pixels)

      frames.append(frame)

  return frames

# cols = 8
# rows = 8

# frames_per_row = heart_image.width / rows
# frames_per_col = heart_image.height / cols

# if not frames_per_row.is_integer() or not frames_per_col.is_integer():
#   print("Image dimensions must be divisible by ", cols, rows)
#   exit()

# frames_per_row = int(frames_per_row)
# frames_per_col = int(frames_per_col)
# total_number_of_frames = frames_per_row * frames_per_col
# frames = []

# print("Frames per row: ", frames_per_row)
# print("Frames per col: ", frames_per_col)

# for frame_row in range(frames_per_col):
#   for frame_col in range(frames_per_row):
#     frame = []
#     print("Frame: ", frame_col, frame_row)

#     for row in range(rows):
#       row_pixels = []
#       for col in range(cols):
#         pixel_x = frame_col * cols + col
#         pixel_y = frame_row * rows + row
#         print("Pixel: ", pixel_x, pixel_y)
#         rgb_pixel_value = heart_image_rgb.getpixel((pixel_x, pixel_y))
#         print(rgb_pixel_value)
#         row_pixels.append(rgb_pixel_value)
#       frame.append(row_pixels)

#     frames.append(frame)

frames = extract_frames("heart.png", 8, 8)

for frame in frames:
  print("Frame")
  for row in frame:
    for pixel in row:
      print(f'\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m', end='')
    print()
