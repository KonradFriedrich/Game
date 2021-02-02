import pygame as pg
import random
# from map import *
# import threading
from map import *
from StartData import *

global \
    bgx, bgy, screen, FovX, FovY

# init pg
pg.init()


obstacles = pg.sprite.Group()

pg.sprite.spritecollide()


# draw enemy
def enemypos(x, y):
    screen.blit(enemyimg, (x, y))


clock = pygame.time.Clock()

bgxs = 0
bgys = 0


PMS = 3

MapSlicer('img/3kx3k.jpg', 50, 50)

# game loop
running = True
while running:
    backg = pygame.image.load('img/1000x1000grey.png')
    screen.blit(backg, (0, 0))
    MapDraw(bgx, bgy)



    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # movement x-y axis
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                bgxs += PMS
            if event.key == pg.K_RIGHT:
                bgxs += -PMS
            if event.key == pg.K_UP:
                bgys += PMS
            if event.key == pg.K_DOWN:
                bgys += -PMS

        # movement stop
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                bgxs += -PMS
            if event.key == pg.K_RIGHT:
                bgxs += PMS
            if event.key == pg.K_UP:
                bgys += -PMS
            if event.key == pg.K_DOWN:
                bgys += PMS

    bgx = bgxs + bgx
    bgy = bgys + bgy

    bgx, bgy = BorderCheck(bgx, bgy)


    # change player pos
    screen.blit(playerimg, (screenX / 2, screenY / 2))

    # enemy pos
    enemyX += enemyXch
    enemyY += enemyYch
    enemypos((enemyX + bgx), (enemyY + bgy))



    clock.tick()
    fps = clock.get_fps()
    #print(fps)


    # screeenupdate
    pg.display.update()
