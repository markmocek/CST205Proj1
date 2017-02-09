#Mark Mocek, Project 1, 2/9/17
#https://github.com/markmocek/CST205Proj1.git
from PIL import Image

#find median function
def medianOdd(myList):
    #Store list length in the variable listLength
    listLength = len(myList)
    #Store the list
    sortedValues = sorted(myList)
    #Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength +1)/2)-1
    #return the object located at that index
    return sortedValues[middleIndex]

#create x, y variables
x=0
y=0

#load images
im1 = Image.open("imgs/1.png")
im2 = Image.open("imgs/2.png")
im3 = Image.open("imgs/3.png")
im4 = Image.open("imgs/4.png")
im5 = Image.open("imgs/5.png")
im6 = Image.open("imgs/6.png")
im7 = Image.open("imgs/7.png")
im8 = Image.open("imgs/8.png")
im9 = Image.open("imgs/9.png")

#set values for width, hight
width = im1.size[0]
hight = im1.size[1]

#load images
pix1 = im1.load()
pix2 = im2.load()
pix3 = im3.load()
pix4 = im4.load()
pix5 = im5.load()
pix6 = im6.load()
pix7 = im7.load()
pix8 = im8.load()
pix9 = im9.load()

#create empty list for each color value
redList = []
greenList = []
blueList = []

#empty char array
data = ""

#loop cof y values
for y in range(0, hight):
    x = 0
    #loop for x values
    for x in range(0, width):
        #hardcode appends for red
        redList.append(pix1[x,y][0])
        redList.append(pix2[x,y][0])
        redList.append(pix3[x,y][0])
        redList.append(pix4[x,y][0])
        redList.append(pix5[x,y][0])
        redList.append(pix6[x,y][0])
        redList.append(pix7[x,y][0])
        redList.append(pix8[x,y][0])
        redList.append(pix9[x,y][0])
        #hardcode appends for green
        greenList.append(pix1[x,y][1])
        greenList.append(pix2[x,y][1])
        greenList.append(pix3[x,y][1])
        greenList.append(pix4[x,y][1])
        greenList.append(pix5[x,y][1])
        greenList.append(pix6[x,y][1])
        greenList.append(pix7[x,y][1])
        greenList.append(pix8[x,y][1])
        greenList.append(pix9[x,y][1])
        #hardcode appends for blue
        blueList.append(pix1[x,y][2])
        blueList.append(pix2[x,y][2])
        blueList.append(pix3[x,y][2])
        blueList.append(pix4[x,y][2])
        blueList.append(pix5[x,y][2])
        blueList.append(pix6[x,y][2])
        blueList.append(pix7[x,y][2])
        blueList.append(pix8[x,y][2])
        blueList.append(pix9[x,y][2])
        #run median method for colors
        newRed = medianOdd(redList)
        newGreen = medianOdd(greenList)
        newBlue = medianOdd(blueList)
        #add color values to char array
        data += chr(newRed) + chr(newGreen) + chr(newBlue)
        #reset lists
        redList = []
        greenList = []
        blueList = []
        #increment X
        x += 1
    #increment Y
    y += 1

#create new image with median values
im = Image.fromstring("RGB", (width, hight), data)
im.save("10.png")
