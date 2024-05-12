# Hat originally made by Tony Baston of 3206
# Re-wired and re-programmed (using vim like a *real* nerd) by Blue S of 3206

import time
import board
import neopixel

pixel_pin = board.D0
num_pixels = 296

#define pixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

RED = (255, 0, 0)
BLU = (0, 0, 255)
WHT = (85, 85, 85)
BLK = (0, 0, 0)

FRC_3206_PIXELART = [BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLK, BLU, WHT, BLK, BLU, BLU, BLU, BLK, BLU, BLU, BLU, BLK, BLU, BLU, BLU, BLK, BLU, BLU, BLU, BLK, BLU, WHT, BLK, BLK, BLK, BLK, BLU, BLK, BLK, WHT, WHT, WHT, BLK, RED, BLK, RED, BLK]

for i in range(FRC_3206_PIXELART):
    pixel[i] = FRC_3206_PIXELART[i]

pixels.show()
