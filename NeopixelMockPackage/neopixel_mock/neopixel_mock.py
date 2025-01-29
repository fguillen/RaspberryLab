import adafruit_pixelbuf

# Pixel color order constants
RGB = "RGB"
"""Red Green Blue"""
GRB = "GRB"
"""Green Red Blue"""
RGBW = "RGBW"
"""Red Green Blue White"""
GRBW = "GRBW"
"""Green Red Blue White"""

class NeoPixelMock(adafruit_pixelbuf.PixelBuf):
    def __init__(
        self,
        pin: int,
        n: int,
        *,
        bpp: int = 3,
        brightness: float = 1.0,
        auto_write: bool = True,
        pixel_order: str = None,
        rows: int = 8, # custom
    ):
        if not pixel_order:
            pixel_order = GRB if bpp == 3 else GRBW
        elif isinstance(pixel_order, tuple):
            order_list = [RGBW[order] for order in pixel_order]
            pixel_order = "".join(order_list)

        self.rows = rows
        self.cols = n // rows

        super().__init__(
            n, brightness=brightness, byteorder=pixel_order, auto_write=auto_write
        )

    def deinit(self) -> None:
        self.fill(0)
        self.show()

    def _transmit(self, buffer: bytearray) -> None:
        # Extract a list of tuples of 3 bytes from the buffer
        pixels = [(buffer[i+1], buffer[i], buffer[i+2]) for i in range(0, len(buffer), 3)]
        # print("pixel_data: ", pixel_data)
        # print("buffer: ", buffer)

        # print("pixels: ", pixels)

        print(f"\r\033[{self.rows}A", end="")
        for y in range(self.rows):
          for x in range(self.cols):
            pixel = pixels[(self.cols * y) + x]
            # print("final pixel", x, y, pixel)
            print(f'\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m', end='')
          print()
