import pygame as pg
import random
from PIL import Image
import os, sys

pg.init()

STARTPOSX = 0
STARTPOSY = 0


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


INVISEVENT = pg.USEREVENT+1







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
        self.invincible = False
        self.rect = pg.rect
        self.nodes = []


    def animationspliter(self, image, frames = 1):
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

        # "theoretically" move the player then look if he intersects with an obstacle and then either leave it be or move him back
        # if checks for improved runtime/ optimized calc power
        if x != 0:
            self.rect.move_ip(-x, 0)
            if pg.sprite.spritecollide(player, obstacle_group, False):
                self.rect.move_ip(x, 0)
                x = 0
                #"anti" check -> checks if player would be outside of room
            elif not pg.sprite.spritecollide(player, map_area, False):
                self.rect.move_ip(x, 0)
                x = 0

            else:
                self.rect.move_ip(x, 0)


        if y != 0:
            self.rect.move_ip(0, -y)
            if pg.sprite.spritecollide(player, obstacle_group, False):
                self.rect.move_ip(0, y)
                y = 0
            elif not pg.sprite.spritecollide(player, map_area, False):
                self.rect.move_ip(0, y)
                y = 0
            else:
                self.rect.move_ip(0, y)


        # move the map -> actually moving the player
        bgx = x + bgx
        bgy = y + bgy


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
        return x, y




    def detectdamage(self):
        if pg.sprite.spritecollide(player, enemies_group, False):
            if self.invincible == False:
                # timer for 750 ms -> event -> invincibility gets cancelled
                pg.time.set_timer(INVISEVENT, 750, loops=1)
                self.playerHp = self.playerHp - 1
                print(self.playerHp)
                self.invincible = True
                if self.playerHp == 0:
                    print("Player Died!")
                    sys.exit()



class Enemyob(pg.sprite.Sprite):
    def __init__(self, x, y, image, frames = 1):
        super().__init__()
        #self.enemyimg = pg.image.load(enemytype[0])
        self.img = []
        #self.enemyX = random.randint(0, screenX - 32)
        self.enemyX = x
        self.enemyXch = 1
        #self.enemyY = random.randint(0, screenY - 32)
        self.enemyY = y
        self.enemyYch = 0
        self.currentframe = 0
        self.animationspliter(image, frames)
        self.rect = self.imgrect.move(x + bgx, y + bgy)


    def animationspliter(self, image, frames):
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
        self.rect = pg.Rect((topleft[0] + bgx, topleft[1] + bgy), (bottomright[0] - topleft[0], bottomright[1] - topleft[1]))
        self.tl = topleft
        self.br = bottomright
        self.image = pg.image.load(image)

        #self.rect = (self.tl[0], self.tl[1], self.br[0], self.br[1])


    def simpledraw(self):
        self.rect = ((self.tl[0] + bgx, self.tl[1] + bgy), (self.br[0] - self.tl[0], self.br[1] - self.tl[1]))
        screen.blit(self.image, (self.tl[0] + bgx, self.tl[1] + bgy))
        #pg.draw.rect(screen, (0, 0, 0), (bgx self.rect)



class area(pg.sprite.Sprite):
    def __init__(self, topleft, bottomright):
        super().__init__()
        #create coords by usinjg topleft and bottomright corner
        # <rect(0, 0, 36, 46)>      height:  178        twidth:  195
        self.rect = pg.Rect((topleft[0] + bgx + 195 + 36, topleft[1] + bgy + 178 + 46), (bottomright[0] - topleft[0] - 72, bottomright[1] - topleft[1] - 92))
        map_area.add(self)

    def give_image(self, image):
        self.image = pg.image.load(image)




enemy = Enemyob(420, 580, "imgs/2xMinutaurAnimations", 36)
#enemy.animationspliter("imgs/2xMinutaurAnimations", 36)


player = Playerob(hellboy)
player.animationspliter("imgs/2xPlayerAnimations", 36)

player_group = pg.sprite.Group()
player_group.add(player)

enemies_group = pg.sprite.Group()
enemies_group.add(enemy)


obstacle_group = pg.sprite.Group()
#OBSTACLES.add(enemy)



obstacle1 = obstacle([385, 320], [405, 340], "img/red50.jpeg")
obstacle_group.add(obstacle1)

# auf alle coordinaten 200 pixel wegen padding rechnen (passiert in der klasse)
map_area = pg.sprite.Group()
#room1 = area([385, 320], [865, 615])
room1 = area([160, 90], [700, 480])
room2 = area([545, 480], [600, 630])

#groupd of all sprites except for the player
all_sprites = pg.sprite.Group()
all_sprites.add(obstacle_group)
all_sprites.add(map_area)
all_sprites.add(enemies_group)


