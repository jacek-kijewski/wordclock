import board
import neopixel

NUM_PIXELS_STRIP1 = 91
NUM_PIXELS_STRIP2 = 137
COLOR =  (255,197,80)

strip1 =neopixel.NeoPixel(
    board.D10, NUM_PIXELS_STRIP2 , brightness=0.5, auto_write=False
)

strip2 =neopixel.NeoPixel(
    board.D12, NUM_PIXELS_STRIP2 , brightness=0.1, auto_write=False
)

pixels2 =neopixel.NeoPixel(
   board.D10, NUM_PIXELS_STRIP2 , brightness=0.5, auto_write=False
)


strip1[1] = COLOR
strip2[1] = COLOR
strip1.write()
strip2.write()