import pygame as pg
from PIL import Image

# declare borders as one big square around the map
# and all cutouts are obstacles


class level():
    def __init__(self, map, Startpos, enemies, obstacles):
        self.map = map[0]
        self.bg = map[1]
        self.borders = level.rectborders(self, map[0])
        self.STARTPOSX = Startpos[0]
        self.STARTPOSY = Startpos[1]
        self.enemies = enemies
        self.obstacles = obstacles


    def rectborders(self, map):
        im = Image.open(map)
        imgwidth, imgheight = im.size
        # in bgx coords (0x, 0y, 1x, 1y)
        return [0, 0, imgwidth, imgheight]



class Border(pg.sprite.Sprite):
    #toplefx+y und bottomrightx+y

    def xborder(self, x):
        self.x = x


    def yborder(self, y):
        self.y = y

    def rectborders(self, map):
        im = Image.open(map)
        imgwidth, imgheight = im.size
        #in bgx coords
        return [0, 0, imgwidth, imgheight]
        



Level1 = level(
    #["img/2xDungeon.png", "img/1024Black.png"], [300, 300], [], []
    ["img/2xDungeon.png", "img/1024Black.png"], [300, 300], [], []
)


print(Level1.borders)