from PIL import Image
from main import screen, screenX, screenY
import math
from itertools import islice

# this concludes functons which cuts, draws and only draw special tiles of the map


global \
    imwidth, imheight

World = {}
SeeWorld = []






# map drawing function
def MapDraw(bgx, bgy, WorldDict):


    # player fov box rounded too hundreds, +100 bcs rounded up
    PlayerFovX = range(int(math.ceil((bgx - screenX - 100) / 100.0)) * 100, int(math.ceil(bgx / 100.0)) * 100, 100)
    PlayerFovY = range(int(math.ceil((bgy - screenX - 100) / 100.0)) * 100, int(math.ceil(bgy / 100.0)) * 100, 100)
    print(PlayerFovX)
    print(PlayerFovY)



    # loop through tiles
    for i in WorldDict:
        #print(WorldDict[i])
        #print(WorldDict[i]["corners"])
        for j in WorldDict[i]["corners"]:
            #print(j)
            if j[0] in PlayerFovY and j[1] in PlayerFovX:
                #screen.blit(WorldDict[i["loc"]], (WorldDict[i]["corners"]["topl"][0], WorldDict[i]["corners"]["topl"][1]))
                print(f"{j} + see")
                print(WorldDict[i]["loc"])
                screen.blit(WorldDict[i]["loc"], (0, 0))

                # Maybe faster like this:
                # if World[i[j[1]]] in range(int(math.ceil((bgx - screenX - 100) / 100.0)) * 100, int(math.ceil(bgx / 100.0)) * 100, 100) and World[i[j[2]] in range(int(math.ceil((bgy - screenX - 100) / 100.0)) * 100, int(math.ceil(bgy / 100.0)) * 100, 100):








def MapSlicer(Map, screenW, screenH):

    x = 0

    # getting the sizes
    im = Image.open(Map)
    #print(im.width)
    imgwidth, imgheight = im.size
    #print(imgwidth)
    #print(imgheight)


    rows = imgwidth / screenW / 4
    columns = imgheight / screenH / 4
    theight = imgheight // math.ceil(columns)
    twidth = imgwidth // math.ceil(rows)

    # cutting it small
    for i in range(0, math.ceil(rows)):
        for j in range(0, math.ceil(columns)):
            tile = im.crop((i * twidth, j * theight, (i + 1) * twidth, (j + 1) * theight))
            x += 1
            # save the image
            tile.save(f"img/tile-{x}-{i + 1}#{j + 1}-.png")
            # tile corners for loading points (and round up to hundreds for easier calc)
            topl = [int(math.ceil(theight * i / 100.0)) * 100, int(math.ceil(twidth * j / 100.0)) * 100]
            topr = [int(math.ceil(theight * i / 100.0)) * 100, int(math.ceil(twidth * (j + 1) / 100.0)) * 100]
            botl = [int(math.ceil(theight * (i + 1) / 100.0)) * 100, int(math.ceil(twidth * j / 100.0)) * 100]
            botr = [int(math.ceil(theight * (i + 1) / 100.0)) * 100, int(math.ceil(twidth * (j + 1) / 100.0)) * 100]

            # create world dict
            World["Tile" + str(x)] = {}
            World["Tile" + str(x)]["loc"] = f"img/tile-{x}-{i + 1}#{j + 1}-.png"
                # ("img/tile-" + x + "-" + str(i) + "#" + str(j) + "-" + ".png")
            World["Tile" + str(x)]["corners"] = [topl, topr, botl, botr]
    print(World)



MapSlicer('img/floorwood.png', 50, 50)
MapDraw(300, 300, World)