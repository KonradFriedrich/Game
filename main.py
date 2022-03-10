import pygame as pg
import random
from StartData import *
import StartData as SD
from map import *
global \
        screen, FovX, FovY

# init pg
pg.init()


obstacles = pg.sprite.Group()



clock = pg.time.Clock()

bgxs = 0
bgys = 0


PMS = 4

#MapSlicer('grey2k', 50, 50)
MapSlicer('img/2xDungeon.png', 50, 50)



#init framecounter
framecounter = pygame.time.get_ticks()
ultimateframe = 0

#startpos player
playerstance = "e"



zk = 0

# game loop
running = True
while running:
    #get frame for animation
    if pygame.time.get_ticks() > framecounter:
        ultimateframe = (1 + ultimateframe) % 12
        framecounter += 80


    #load a Background for where there is no map
    backg = pygame.image.load('img/1024Black.png')
    screen.blit(backg, (0, 0))
    MapDraw()
    obstacle1.simpledraw()





    #event handler
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

    # move the player / map
    player.move(bgxs, bgys, playerstance, ultimateframe)


    #hold player inside map bounds
    BorderCheck()



    # change player pos
    #screen.blit(player.img[ultimateframe], (screenX / 2, screenY / 2))

    #detect if player runs into enemy
    player.detectdamage()

    # enemy pos
    SD.enemy.enemypos(ultimateframe)


    if zk == 10:
        print("do it")
        enemy.pathfinding(player)

    zk = zk + 1
    #print(zk)
    clock.tick()
    fps = clock.get_fps()

    # screeenupdate
    pg.display.update()