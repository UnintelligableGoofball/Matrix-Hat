#This code is to be run on a computer
#This code uses the PIL library, to install run:
#   python3 -m pip install --upgrade pip
#   python3 -m pip install --upgrade Pillow

from PIL import Image

imgnam = input('what image file would you like to open?\n')

#open image and make a list of tuples for each rgb value
img = Image.open(imgnam,'r')
img = list(img.getdata())

#convert list of tuple to list of integers
ImgList = []
for i in img:
    for j in i:
        ImgList.append(j)

filenam = input('What should the text list be called?\n')

#create file and write list of integers as strings, each item on a new line
imgFile = open(filenam,'w')
for i in ImgList:
    imgFile.write(str(i)+'\n')
imgFile.close()

#print file to confirm it was written correctly
#imgFile = open(filenam,'r')
#print(imgFile.read())

#print info on the new file created
print('New file '+filenam+' created, containing '+str(len(ImgList))+' items. Yahoo!')
