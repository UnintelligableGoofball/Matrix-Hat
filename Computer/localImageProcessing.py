#This code is to be run on a computer
#This code uses the PIL library, to install run:
#   python3 -m pip install --upgrade pip
#   python3 -m pip install --upgrade Pillow


import numpy as np
from PIL import Image
import matplotlib.colors

img = Image.open('./HAT_ART.png')
img = np.array(img).reshape(888)
print(img)
for i in range(8):
    print((img[3*i], img[3*i+1], img[3*i+2]))
imgArr = np.chararray(296, itemsize=6)
for i in range(296):
    print(i)
    imgArr[i] = '%02x%02x%02x' % (img[3*i], img[3*i+1], img[3*i+2])
    print(imgArr[i])
imgArr.resize((8,37))
print(imgArr)
arr = np.save('./Pico/Art/HAT_ART_ARRAY', imgArr) # 37x8 array
checkarr = np.load('./Pico/Art/HAT_ART_ARRAY.npy')
print(checkarr)
