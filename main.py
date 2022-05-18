import pygame as pg
import random
from StartData import *
import StartData as SD
from map import *
global \
        screen, FovX, FovY

# init pg
pg.init()

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
    #obstacle1.simpledraw()
    #obstacle_group.draw(screen)





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


        # player will be able to get hit again
        if event.type == INVISEVENT:
            print("event triggered")
            player.invincible = False
            player.text_surface = my_font.render(f'HP: {player.playerHp}', False, (255, 100, 100))

        # Death of player, make respawn available
        if event.type == PLAYERDEATH:
            player.death()
            backg.set_alpha(90)
            screen.blit(backg, (0, 0))
            screen.blit(player.text_surface, (450, 450))
            pg.display.update()
            pg.time.wait(3000)
            sys.exit()


    # move the player -> map and obstacles, Walls, enemies usw....
    xchange, ychange = player.move(bgxs, bgys, playerstance, ultimateframe)
    allspritemove(xchange, ychange)


    #hold player inside map bounds
    #BorderCheck()


    # shows HUD
    screen.blit(player.text_surface, (50,50))


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