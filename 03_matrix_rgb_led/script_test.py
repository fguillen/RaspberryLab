from image_to_frames import extract_frames
from frame_to_neopixel_sequence import frame_to_neopixel_sequence

image_path = "heart.png"
pixels_per_column = 8
pixels_per_row = 8

frames = extract_frames(image_path, pixels_per_column, pixels_per_row)
