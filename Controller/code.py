# Hat originally made by Tony Baston of 3206
# Re-wired and re-programmed by Blue S of 3206

#open a file containing a list of colors and set each pixel to that color

import board
import neopixel

pixel_pin = board.D0
num_pixels = 296

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

file = open('HAT_ART_LIST.txt','r')
pixelList = list()
pixelList = file.readlines()

#Convert list of strings to list of ints
pixelList = list(map(int, pixelList))

pixelList2D = [ pixelList[i:i+3] for i in range(0, len(pixelList), 3) ]

print(pixelList2D)

for i in range(9):
    pixelList2D[37*i-37:37*i] = pixelList2D[37*i-37:37*i][::-1]

print(pixelList2D)

for i in range(len(pixelList2D)):
    pixels[i]=pixelList2D[i]
pixels.show()
