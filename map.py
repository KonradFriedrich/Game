from PIL import Image
from screenclass import *
import math
import pygame

# this concludes functons which cuts, draws and only draw special tiles of the map

pygame.init

global \
    twidth, theight





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
            # the cutout
            tile = im.crop((i * twidth, j * theight, (i + 1) * twidth, (j + 1) * theight))
            x += 1
            # save the image
            tile.save(f"img/tile#{i + 1}#{j + 1}#.png")


    global RENDERX, RENDERY
    RENDERX = math.ceil(screenX / twidth) + 1
    RENDERY = math.ceil(screenY / theight) + 1






def MapDraw(bgx, bgy):

    # get the upper left tile
    xfirst = math.trunc(abs((bgx + startposX) / twidth))
    yfirst = math.trunc(abs((bgy + startposY) / theight))

    # draw enough adjacent tiles to fill screen
    for i in range(0, RENDERX):
        for j in range(0, RENDERY):

            # check if the tile exists
            if xfirst + i > 0 and yfirst + j > 0:

                # draw the tile
                square = pygame.image.load(f"img/tile#{xfirst + i}#{yfirst + j}#.png")
                screen.blit(square, (int(xfirst + i) * twidth + bgx + startposX, int(yfirst + j) * theight + bgy + startposY))



