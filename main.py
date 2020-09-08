import pygame as pg
import random
from pygame_functions import *
#from map import *
#import threading
from map import *
from screenclass import *

global\
bgx, bgy, screen



# init pg
pg.init()




# Player position
playerimg = pg.image.load('img/knight.png')
playerX = 384
playerXch = 0
playerY = 480
playerYch = 0
viewX = 0
viewY = 0

# draw player
def playerpos(x, y):
    screen.blit(playerimg, (x, y))


# Enemy position
enemyimg = pg.image.load('img/enemy.png')
enemyX = random.randint(0, screenX-32)
enemyXch = random.randint(-10, 10) / 50000
enemyY = random.randint(0, screenY-32)
enemyYch =random.randint(-10, 10) / 50000

# draw enemy
def enemypos(x, y):
    screen.blit(enemyimg, (x, y))



clock = pygame.time.Clock()

#MapSlicer('img/floorwood.png', 50, 50)
#map = threading.Thread(target=MapSlicer, args=('img/floorwood.png', 50, 50))
#map.start()

bgx = 1200
bgy = 1200

MapSlicer('img/10x10.png', 50, 50)

# game loop
running = True
while running:
    #backg = newSprite('img/10x10.png', 1)
    backg = pygame.image.load('img/1000x1000grey.png')
    screen.blit(backg, (0, 0))
    MapDraw(1200, 1200, World)



    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # movement x-y axis
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerXch += -0.0006
                viewX += -1
                bgx += 1
            if event.key == pg.K_RIGHT:
                playerXch += 0.0006
                viewX += 1
            if event.key == pg.K_UP:
                playerYch += -0.0006
                viewY += 1
            if event.key == pg.K_DOWN:
                playerYch += 0.0006
                viewY += -1

        # movement stop
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                playerXch += 0.0006
                viewX = 1
                bgx += -1
            if event.key == pg.K_RIGHT:
                playerXch += -0.0006
                viewX = -1
            if event.key == pg.K_UP:
                playerYch += 0.0006
                viewY += 1
            if event.key == pg.K_DOWN:
                playerYch += -0.0006
                viewY += -1




    # background movement (scrollable background)
    #def Scroll(sx, sy):



    # x borders
    if playerX <= 0:
        playerX = 0
    elif playerX >= screenX-32:
        playerX = screenX-32
    # y borders
    if playerY <= 0:
        playerY = 0
    elif playerY >= screenY-32:
        playerY = screenY-32

    # change player pos
    playerY += screenY * playerYch
    playerX += screenX * playerXch
    playerpos(int(playerX), int(playerY))


    # enemy pos
    enemyX += screenY * enemyXch
    enemyY += screenX * enemyYch
    enemypos(int(enemyX), int(enemyY))

    # border
    if enemyX <= 0:
        enemyX = 0
        enemyXch = random.randint(-10, 10) / 50000
    elif enemyX >= screenX-32:
        enemyX = screenX-32
        enemyXch = random.randint(-10, 10) / 50000
    # y borders
    if enemyY <= 0:
        enemyY = 0
        enemyYch =random.randint(-10, 10) / 50000
    elif enemyY >= screenY-32:
        enemyY = screenY-32
        enemyYch =random.randint(-10, 10) / 50000

    # enemy hitbox + checking
    enemyXhit = range(round(enemyX)-32, round(enemyX))
    enemyYhit = range(round(enemyY)-32, round(enemyY))
    playerXhit = round(playerX-16)
    playerYhit = round(playerY-16)



    clock.tick()
    fps = clock.get_fps()
    print(fps)

    if playerXhit in enemyXhit and playerYhit in enemyYhit:
        running = False



    # screeenupdate
    pg.display.update()