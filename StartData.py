import pygame as pg
import random
from PIL import Image
import os, sys


pg.init()

STARTPOSX = -300
STARTPOSY = -300


bgx = STARTPOSX
bgy = STARTPOSY

# create window
screenX = 1000
screenY = 1000

screen = pg.display.set_mode((screenX, screenY))

# title and icon (change later)
pg.display.set_caption("Hack and Slay")
icon = pg.image.load('img/knight.png')
pg.display.set_icon(icon)



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
        self.nodes = []


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
        global bgx, bgy
        # direction = north east south west / n,e,s,w so at least 4x8 frames needed
        self.rect = self.imgrect.move(screenX/2, screenY/2)

        # obstacle blocking

        # "theoretically" move the player then look if he intersects with an obstacle and then either leave it be or move him back

        #print("1:  " + str(self.rect.left))
        #print(x)
        self.rect.move_ip(x, 0)
        #print("2:  " + str(self.rect.left))
        if pg.sprite.collide_rect(player, obstacle1):
            x = 0
        #print("3:  " + str(self.rect.left))
        self.rect.move_ip(-x, 0)
        #print("4:  " + str(obstacle1.rect))

        self.rect.move_ip(0, y)
        if pg.sprite.collide_rect(player, obstacle1):
            y = 0
        self.rect.move_ip(0, -y)





        #dont fuckin g move the rect move the map!!!!!!!!!!!!!!!!!!!!!!!!! change this later!!!!!!!!!!
        #change bg x/y not player rect!!!!
        print(x)
        bgx = x + bgx
        bgy = y + bgy
        self.rect.move(x, y)

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









    def detectdamage(self):
        #print(pg.sprite.spritecollide(player, enemies_group, False))
        #pygame.sprite.spritecollideany
        self.rect = self.imgrect.move(screenX/2 - bgx,screenY/2 - bgy)
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



    def enemypos(self, frame):
        #if self.enemyXch == -1:
        #    screen.blit(self.img[frame + 12], (x, y))
        #else:
        #    screen.blit(self.img[frame], (x, y))
        if enemy.enemyX > 520:
            enemy.enemyXch = -1
        elif enemy.enemyX < 420:
            enemy.enemyXch = 1
        enemy.enemyX += enemy.enemyXch
        if enemy.enemyXch == -1:
            frame = frame + 12


        screen.blit(self.img[frame], (enemy.enemyX + bgx, enemy.enemyY + bgy))
        self.rect = self.imgrect.move(enemy.enemyX + bgx, enemy.enemyY + bgy)
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


    def pathfinding(self, target):
        path1 = path(self, target)
        subpaths = path1.intersect()
        if len(subpaths) == 2:
            self.node.append(subpaths[0])
            self.node.append(subpaths[1])
        elif len(subpaths) == 1:
            self.node.append(subpaths[0])
        else:
            print("paths")










class path(pg.sprite.Sprite):
    def __init__(self, start, target):
        super().__init__()
        self.startx = start.rect.center[0]
        self.starty = start.rect.center[1]
        self.targetx = target.rect.center[0] + 10
        self.targety = target.rect.center[1] + 10

        self.rect = [self.startx, self.starty, self.targetx, self.targety]

        self.length = abs(self.startx - self.targetx + self.starty - self.targety)

        #basically the line just wider so it looks cleaner when the enemy passes the obs probably not gonna use it for now
        #self.wideline =

    def intersect(self):
        paths = []
        print(1)
        intersects = pg.sprite.spritecollide(player, enemies_group, False)
        print(intersects)
        print(2)
        #not over 8 nodes bcs 9+ is 516 possible paths -> too much computing
        if 8 < len(intersects) > 0:
            #find out closest to start + sorting algorythm may be uselfull?
            distance1 = 1000000
            for i in intersects:
                distance2 = abs(self.startx - i.rect.center[0] + self.starty - i.rect.center[1])
                if distance2 > distance1:
                    distance1 = distance2
                    close = i

            #possible corners for first obj
            #way to corner + extra then check if intersect because without extra definitly intersect
            path1 = ""
            path2 = ""
            tl = path(self.start, close.rect.topleft)
            tl[0] += -3
            tl[1] += 3
            bl = path(self.start, close.rect.topleft)
            bl[0] += -3
            bl[1] += -3
            tr = path(self.start, close.rect.topleft)
            tr[0] += 3
            tr[1] += 3
            br = path(self.start, close.rect.topleft)
            br[0] += 3
            br[1] += -3
            print("1")
            #check for intersects in same ob, if yes delete path, then for intersects in other obj and find ways around
            cornerpaths = [tl, bl, tr, br]


            for j in cornerpaths:
                if len(pg.sprite.spritecollide(j, enemies_group, False)) == 0:
                    print("2")
                    if path1 == "":
                        path1 = j
                    else:
                        path2 = j

                paths = [path1, path2]






        elif len(intersects) > 8:
            print("too many obstacles")

        else:
            print("nothing")

        return paths




class obstacle(pg.sprite.Sprite):
    def __init__(self, topleft, bottomright, image):
        #create coords by usinjg topleft and bottomright corner
        super().__init__()
        self.rect = ((topleft[0], topleft[1]), (bottomright[0] - topleft[0], bottomright[1] - topleft[1]))
        self.tl = topleft
        self.br = bottomright
        self.img = pg.image.load(image)

        #self.rect = (self.tl[0], self.tl[1], self.br[0], self.br[1])

    def simpledraw(self):
        self.rect = ((self.tl[0] + bgx, self.tl[1] + bgy), (self.br[0] - self.tl[0], self.br[1] - self.tl[1]))
        screen.blit(self.img, (self.tl[0] + bgx, self.tl[1] + bgy))
        #pg.draw.rect(screen, (0, 0, 0), (bgx self.rect)









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
obstacle1 = obstacle([400, 400], [450, 450], "img/red50.jpeg")
obstacles.add(obstacle1)