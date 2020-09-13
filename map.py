from PIL import Image
from screenclass import *
import math
import pygame

# this concludes functons which cuts, draws and only draw special tiles of the map

pygame.init

global \
    twidth, theight

World = {}
SeeWorld = []






startposx = 600
startposy = 600

# map drawing function
def MapDraw(cbgx, cbgy, WorldDict, cFX, cFY):

    global FX, FY, bgx, bgy

    # player fov box rounded too hundreds, +100 bcs rounded up
    # change the ranges so they work!
    FX += cFX
    FY += cFY

    bgx += cbgx
    bgy += cbgy

    #print(FX)
    #print(bgx)

    PlayerFovX = range(int(math.ceil(FX / 100.0)) * 100, int(math.ceil((FX + screenX + 200) / 100.0)) * 100, 100)
    PlayerFovY = range(int(math.ceil(FY / 100.0)) * 100, int(math.ceil((FY + screenY + 200) / 100.0)) * 100, 100)


    z = 0
    # loop through tiles
    for i in WorldDict:
        for j in WorldDict[i]["corners"]:
            if j[0] in PlayerFovY and j[1] in PlayerFovX:
                tileX = WorldDict[i]["loc"].split("#")[1]
                tileY = WorldDict[i]["loc"].split("#")[2]
                square = pygame.image.load(WorldDict[i]["loc"])


                screen.blit(square, ((int(tileX) - 1) * twidth + bgx + startposx, (int(tileY) - 1) * theight + bgy + startposy))
                z += 1
                break
    print(z)










def MapSlicer(Map, screenW, screenH):

    x = 0

    # getting the sizes
    im = Image.open(Map)
    imgwidth, imgheight = im.size


    rows = imgwidth / screenW / 4
    columns = imgheight / screenH / 4
    global theight, twidth
    theight = imgheight // math.ceil(columns)
    twidth = imgwidth // math.ceil(rows)


    # cutting it small
    for i in range(0, math.ceil(rows)):
        for j in range(0, math.ceil(columns)):
            tile = im.crop((i * twidth, j * theight, (i + 1) * twidth, (j + 1) * theight))
            x += 1
            # save the image
            tile.save(f"img/tile{x}#{i + 1}#{j + 1}#.png")
            # tile corners for loading points (and round up to hundreds for easier calc)
            topl = [int(math.ceil(twidth * j / 100.0)) * 100, int(math.ceil(theight * i / 100.0)) * 100]
            topr = [int(math.ceil(twidth * (j + 1) / 100.0)) * 100, int(math.ceil(theight * i / 100.0)) * 100]
            botl = [int(math.ceil(twidth * j / 100.0)) * 100, int(math.ceil(theight * (i + 1) / 100.0)) * 100]
            botr = [int(math.ceil(twidth * (j + 1) / 100.0)) * 100, int(math.ceil(theight * (i + 1) / 100.0)) * 100]

            # create world dict
            World["Tile" + str(x)] = {}
            World["Tile" + str(x)]["loc"] = f"img/tile{x}#{i + 1}#{j + 1}#.png"
                # ("img/tile-" + x + "-" + str(i) + "#" + str(j) + "-" + ".png")
            World["Tile" + str(x)]["corners"] = [topl, topr, botl, botr]
    print(World)



