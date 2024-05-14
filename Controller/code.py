# Hat originally made by Tony Baston of 3206
# Re-wired and re-programmed by Blue S of 3206

#open a file containing a list of colors and set each pixel to that color

import time
import board
import neopixel

brightness = 0.2
pixel_pin = board.D0
hight = 8
width = 37

pixels = neopixel.NeoPixel(pixel_pin, (hight*width), brightness=brightness, auto_write=False)

#reverse each width section but leave the height in the same order
def flip_horizontal(image):
    for i in range(hight+1):
        image[width*(i-1):width*i] = image[width*(i-1):width*i][::-1]

def disp_image(image):
    for i in range(hight*width):
        pixels[i] = image[i]
    pixels.show()

def scroll_horizontal(image, position):
    scrolled_image = list()
    for i in range(hight+1):
        scrolled_image[width*(i-1):width*i] = (image[position+(width*(i-1)):(width*i)] + image[width*(i-1):position+(width*(i-1))])
    return(scrolled_image)

file = open('HAT_ART_LIST.txt','r')
pixelList = list()
pixelList = file.readlines()

#Convert list of strings to list of ints
pixelList = list(map(int, pixelList))

#format the list of individual values into tuples with three values in each, to be read as rgb values easily
pixelList2D = [ pixelList[i:i+3] for i in range(0, len(pixelList), 3) ]

#flip the image horizontally, since tony wound the light strip clockwise and the images are read left to right
flip_horizontal(pixelList2D)

while True:
    for i in range(width):
        time.sleep(.25)
        disp_image(scroll_horizontal(pixelList2D, (width-i)))
