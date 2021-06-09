from PIL import Image

im = Image.open("../logo.jpeg")
pix = im.load()
width, length = im.size

for x in range(width):
    for y in range(length):
        if(pix[x,y][0] <= 150):
            pix[x,y] = (0,0,0)
        else :
            pix[x,y] = (255,255,255)
im.save('../processed.jpeg', 'JPEG')