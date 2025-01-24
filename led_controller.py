import board
import neopixel
from time import sleep
# Define the number of pixels for each strip
NUM_PIXELS_STRIP1 = 102
NUM_PIXELS_STRIP2 = 137
COLOR = (255, 197, 80)  # Example color (R, G, B)

PINS = [board.D21, board.D18]
NUM_OF_PIXELS = [NUM_PIXELS_STRIP1,NUM_PIXELS_STRIP2]
# Initialize NeoPixel strips
strip1 = neopixel.NeoPixel(board.D21, NUM_PIXELS_STRIP1, brightness=1, auto_write=False)
strip2 = neopixel.NeoPixel(board.D18, NUM_PIXELS_STRIP2, brightness=1, auto_write=False)


def light_pixels(strip, pixels, color):
    """
    Light specific pixels on a NeoPixel strip.

    :param strip: The NeoPixel strip object.
    :param pixels: List of pixel indices to light up.
    :param color: Tuple representing the color (R, G, B).
    """
    for pixel in pixels:
        if 0 <= pixel < len(strip):
            strip[pixel] = color
    strip.show()  # Show changes on the strip


def control_leds(strip_pixels1, strip_pixels2, color=COLOR):
    """
    Control the LED strips by lighting specific pixels.

    :param strip1_pixels: List of pixel indices for strip 1.
    :param strip2_pixels: List of pixel indices for strip 2.
    :param color: Tuple representing the color (R, G, B).
    """
    light_pixels(strip1, strip_pixels1, color)
    light_pixels(strip2, strip_pixels2, color)
