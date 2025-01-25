# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Uses NeoPixel Featherwing connected to D10 and
Dotstar Featherwing connected to D13, and D11.
Update pins as needed for your connections.
"""
import board
import neopixel
from snake_animation import SnakeAnimation

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D10
# Update to match the number of NeoPixels you have connected
pixel_num = 64

# initialize the neopixels featherwing
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

# initial live cells for conways
initial_cells = [
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
]

snake = SnakeAnimation(pixels, speed=0.1, color=0xff00ff, width=8, height=8)

while True:
    # call animate to show the next animation frames
    snake.animate()
