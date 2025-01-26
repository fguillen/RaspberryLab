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

class MockNeoPixel(adafruit_pixelbuf.PixelBuf):
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
        pixels = [(buffer[i], buffer[i+1], buffer[i+2]) for i in range(0, len(buffer), 3)]
        # print("pixel_data: ", pixel_data)
        # print("buffer: ", buffer)

        # print("pixels: ", pixels)

        print(f"\r\033[{self.rows}A", end="")
        for row in range(self.rows):
          for col in range(self.cols):
            pixel = pixels[(self.cols * row) + col]
            print(f'\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m', end='')
          print()




class MockBoard:
    D18 = "D18"

board = MockBoard()


from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.customcolorchase import CustomColorChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE, MAGENTA, ORANGE

pixel_pin = board.D18
pixel_num = 1200
pixels = MockNeoPixel(pixel_pin, pixel_num, auto_write=False, rows=20)

blink = Blink(pixels, speed=0.5, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE])
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=WHITE)
pulse = Pulse(pixels, speed=0.1, period=3, color=AMBER)
sparkle = Sparkle(pixels, speed=0.1, color=PURPLE, num_sparkles=10)
solid = Solid(pixels, color=JADE)
rainbow = Rainbow(pixels, speed=0.1, period=2)
sparkle_pulse = SparklePulse(pixels, speed=0.1, period=3, color=JADE)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=3, spacing=2, step=8)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)
custom_color_chase = CustomColorChase(
    pixels, speed=0.1, size=2, spacing=3, colors=[ORANGE, WHITE, JADE]
)


animations = AnimationSequence(
    comet,
    blink,
    rainbow_sparkle,
    chase,
    pulse,
    sparkle,
    rainbow,
    solid,
    rainbow_comet,
    sparkle_pulse,
    rainbow_chase,
    custom_color_chase,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
