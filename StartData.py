import pygame as pg
import random
from PIL import Image

pg.init()

# create window
screenX = 1000
screenY = 1000

screen = pg.display.set_mode((screenX, screenY))

# title and icon (change later)
pg.display.set_caption("Hack and Slay")
icon = pg.image.load('img/knight.png')
pg.display.set_icon(icon)
STARTPOSX = -300
STARTPOSY = -300
bgx = STARTPOSX
bgy = STARTPOSY



hellboy = ['img/knight.png', 382, 480]
basicmonster = ['img/enemy.png']




# player init
class Playerob(pg.sprite.Sprite):
    def __init__(self, playertype):
        super().__init__()
        self.img = []
        self.playerX = playertype[1]
        self.playerXch = 0
        self.playerY = playertype[2]
        self.playerYch = 0


    def animationspliter(self, image, frames = 1):
        print("init")
        self.animation = Image.open(f"{image}.png")
        self.originalwidth, self.originalheight = self.animation.size

        self.cutwidth = self.originalwidth / frames
        self.framesize = [self.cutwidth, self.originalheight]

        i = 0
        while i <= frames:
            frame = self.animation.crop((i * self.cutwidth, 0, (i + 1) * self.cutwidth, self.originalheight))
            frame.save(f"{image}#1.png")
            addframe = pg.image.load(f"{image}#1.png")
            self.img.append(addframe)

            i += 1

        self.currentimage = self.img[0]

    def move(self, x, y, direction, frame):
        # direction = north east south west / n,e,s,w so at least 4x8 frames needed
        if direction == "n":
            screen.blit(self.img[12 * 0 + frame], (x, y))
        elif direction == "e":
            screen.blit(self.img[12 * 0 + frame], (x, y))
        elif direction == "s":
            screen.blit(self.img[12 * 1 + frame], (x, y))
        elif direction == "w":
            screen.blit(self.img[12 * 1 + frame], (x, y))



class Enemyob(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.enemyimg = pg.image.load(enemytype[0])
        self.img = []
        self.enemyX = random.randint(0, screenX - 32)
        self.enemyXch = 1
        self.enemyY = random.randint(0, screenY - 32)
        self.enemyYch = 1
        self.currentframe = 0


    def animationspliter(self, image, frames = 1):
        print("init")
        self.animation = Image.open(f"{image}.png")
        self.originalwidth, self.originalheight = self.animation.size
        print(self.originalwidth)

        self.cutwidth = self.originalwidth / frames
        self.framesize = [self.cutwidth, self.originalheight]
        print(self.cutwidth)

        i = 0
        while i <= frames:
            frame = self.animation.crop((i * self.cutwidth, 0, (i + 1) * self.cutwidth, self.originalheight))
            frame.save(f"{image}#1.png")
            addframe = pg.image.load(f"{image}#1.png")
            self.img.append(addframe)

            i += 1



    def enemypos(self, x, y, frame):
        screen.blit(self.img[frame], (x, y))

    def move(self, x, y, direction, frame):
        # direction = north east south west / n,e,s,w so at least 4x8 frames needed
        if direction == "n":
            screen.blit(self.img[12 * 0 + frame], (x, y))
        elif direction == "e":
            screen.blit(self.img[12 * 1 + frame], (x, y))
        elif direction == "s":
            screen.blit(self.img[12 * 2 + frame], (x, y))
        elif direction == "w":
            screen.blit(self.img[12 * 3 + frame], (x, y))






enemy = Enemyob()
enemy.animationspliter("imgs/Idleanimation_Minutaur", 12)


player = Playerob(hellboy)
player.animationspliter("imgs/idk", 24)


obstacles_group = pg.sprite.Group()

player_group = pg.sprite.Group()
player_group.add(player)

enemies_group = pg.sprite.Group()
enemies_group.add(enemy)