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

#pg.sprite.spritecollide()




# draw enemy


clock = pygame.time.Clock()

bgxs = 0
bgys = 0


PMS = 3

MapSlicer('img/DUNGEON.png', 50, 50)

framecounter = pygame.time.get_ticks()
ultimateframe = 0

playerstance = "e"

# game loop
running = True
while running:
    if pygame.time.get_ticks() > framecounter:
        ultimateframe = (1 + ultimateframe) % 12
        framecounter += 80
    #print(ultimateframe)


    backg = pygame.image.load('img/1024Black.png')
    screen.blit(backg, (0, 0))
    MapDraw(bgx, bgy)




    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # movement x-y axis
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                bgxs += PMS
                playerstance = "w"
            if event.key == pg.K_RIGHT:
                bgxs += -PMS
                playerstance = "e"
            if event.key == pg.K_UP:
                bgys += PMS
                #playerstance = "n"
            if event.key == pg.K_DOWN:
                bgys += -PMS
                #playerstance = "s"

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
    #screen.blit(player.img[ultimateframe], (screenX / 2, screenY / 2))
    if pg.key.get_pressed() == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
        playerstance = "idle"
    player.move(screenX / 2, screenY / 2, playerstance, ultimateframe)

    # enemy pos
    enemy.enemyX += enemy.enemyXch
    enemy.enemyY += enemy.enemyYch
    enemy.enemypos((enemy.enemyX + bgx), (enemy.enemyY + bgy), ultimateframe)



    clock.tick()
    fps = clock.get_fps()
    #print(fps)


    # screeenupdate
    pg.display.update()
