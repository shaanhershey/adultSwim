from PIL import Image

im = Image.open("../logo.jpeg")
pix = im.load()
width, length = im.size

center_x = 100
center_y = 100

coords = []

for x in range(width):
    for y in range(length):
        if(pix[x,y][0] <= 200):
            pix[x,y] = (0,0,0)
        else :
            pix[x,y] = (255,255,255)
            coords.append(((x-center_x)/27, (y-center_y)/27))

im.save('../processed.jpeg', 'JPEG')

# /execute as @a at @s run summon minecraft:tnt ~ ~-90 ~ {Fuse:40,Motion[x,1.0,y]}
# f.write("execute as @a at @s run summon minecraft:tnt ~ ~-90 ~ {Fuse:40, Motion:[%s,1.0,%s]}" % coords[0])
for i in range(8):
    f = open("../tntPicture/data/picture/functions/picture%s.mcfunction" % (i), "w")
    for j in range(56):
        if(j == 55 and (i >= 12)):
            break
        f.write("execute as @a at @s run summon minecraft:tnt ~ 12 ~ {Fuse:40, Motion:[%s,1.0,%s]}\n" % coords[j*128+i*8])