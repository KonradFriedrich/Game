import pygame as pg
import random

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

#player init
playerimg = pg.image.load('img/knight.png')
playerX = 384
playerXch = 0
playerY = 480
playerYch = 0
viewX = 0
viewY = 0


# Enemy init
enemyimg = pg.image.load('img/enemy.png')
enemyX = random.randint(0, screenX - 32)
enemyXch = 1
enemyY = random.randint(0, screenY - 32)
enemyYch = 1