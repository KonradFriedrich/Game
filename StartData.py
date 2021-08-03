import pygame as pg
import random
from PIL import Image
import os, sys


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


obstruction = pg.sprite.Group()
enattack = pg.sprite.Group()
plattack = pg.sprite.Group()


# player init
class Playerob(pg.sprite.Sprite):
    def __init__(self, playertype):
        super().__init__()
        self.img = []
        self.playerX = playertype[1]
        self.playerXch = 0
        self.playerY = playertype[2]
        self.playerYch = 0
        self.playerHp = 3
        self.playerEffect = []
        self.invincible = pg.time.Clock()
        self.rect = pg.rect


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
        self.imgrect = addframe.get_rect()


    def move(self,x, y, direction, frame):
        # direction = north east south west / n,e,s,w so at least 4x8 frames needed
        self.rect = self.imgrect.move(screenX/2, screenY/2)

        print(bgx)
        # animation
        if direction == "n":
            screen.blit(self.img[12 * 0 + frame], (screenX/2, screenY/2))
        elif direction == "e":
            screen.blit(self.img[12 * 0 + frame], (screenX/2, screenY/2))
        elif direction == "s":
            screen.blit(self.img[12 * 1 + frame], (screenX/2, screenY/2))
        elif direction == "w":
            screen.blit(self.img[12 * 1 + frame], (screenX/2, screenY/2))
        elif direction == "idle":
            screen.blit(self.img[12 * 2 + frame], (screenX/2, screenY/2))



        # obstacle blocking
        #print(pg.sprite.spritecollide(self, enemies_group, False))
        if pg.sprite.collide_rect(player, enemy):
            print("a")
            obstacle = pg.sprite.spritecollide(self, obstacles, False) #fill in whats obstacle probably will create list
            for i in obstacle:
                print(obstacles)
                # over x
                if self.rect.centery >= obstacle[0].rect.centery:
                    #may need to change to obstacle[i].rect.midtop[1]
                    y = obstacle[0].rect.midtop[1]
                else:
                    y = obstacle[0].rect.midbottom[1]
                if self.rect.centerx >= obstacle[0].rect.centerx:
                    # may need to change to obstacle[i].rect.midtop[0]
                    x = obstacle[0].rect.midleft[0]
                else:
                    x = obstacle[0].rect.midright[0]

        #dont fuckin g move the rect move the map!!!!!!!!!!!!!!!!!!!!!!!!! change this later!!!!!!!!!!
        #change bg x/y not player rect!!!!
        self.rect.move(x, y)






    def detectdamage(self, x, y):
        #print(pg.sprite.spritecollide(player, enemies_group, False))
        #pygame.sprite.spritecollideany
        self.rect = self.imgrect.move(screenX/2 - x,screenY/2 - y)
        #print(self.rect)
        #print(self.playerHp)
        if pg.sprite.collide_rect(player, enemy):
            self.invincible.tick()
            #print("b")
        #print(self.invincible.get_time)
            #if self.invincible.get_time >= 1.5:
                #self.playerHp = self.playerHp - 1
            #print(pg.sprite.spritecollide(player, enemies_group, False))
            #print("hawww yeah")
            # maybe effects will be hard tho
            # self.playerEffect.append("invis")
        #if self.playerHp == 0:
            #sys.exit()
        #print(self.playerHp)



class Enemyob(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.enemyimg = pg.image.load(enemytype[0])
        self.img = []
        #self.enemyX = random.randint(0, screenX - 32)
        self.enemyX = 420
        self.enemyXch = 1
        #self.enemyY = random.randint(0, screenY - 32)
        self.enemyY = 580
        self.enemyYch = 0
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
        self.imgrect = addframe.get_rect()
        self.rect = self.imgrect.move(enemy.enemyX + bgx, enemy.enemyY +bgy)



    def enemypos(self, x, y, frame):
        #if self.enemyXch == -1:
        #    screen.blit(self.img[frame + 12], (x, y))
        #else:
        #    screen.blit(self.img[frame], (x, y))
        screen.blit(self.img[frame], (x, y))
        self.rect = self.imgrect.move(enemy.enemyX, enemy.enemyY)
        #screen.blit(self.img[frame], self.rect)
        #print(self.rect)




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
        elif direction == "idle":
            screen.blit(self.img[12 * 5 + frame], (x, y))






enemy = Enemyob()
enemy.animationspliter("imgs/2xMinutaurAnimations", 36)


player = Playerob(hellboy)
player.animationspliter("imgs/2xPlayerAnimations", 36)

player_group = pg.sprite.Group()
player_group.add(player)

enemies_group = pg.sprite.Group()
enemies_group.add(enemy)

obstacles = pg.sprite.Group()
obstacles.add(enemy)