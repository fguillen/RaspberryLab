def frame_to_neopixel_sequence(frame, pixels_per_row, pixels_per_column):
  neopixel_sequence = []

  for row in range(pixels_per_row):
    for col in range(pixels_per_column):
      pixel = frame[row][col]
      neopixel_sequence.append(pixel)

  return neopixel_sequence
