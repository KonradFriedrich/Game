import pygame

pygame.init()

class Enemy:
    def __init__(self, Type):
        self.type = Type.type
        self.ms = Type.ms
        self.hp = Type.hp
        self.msx = -1
        self.msy = -1
        pass
    def spawn(self, x, y):
        self.posx = x + bgx
        self.posy = y + bgy
        screen.blit("Standbyimg" + self.type + ".png", (self.posx, self.posy))

class Chabu:
    def __init__(self):
        self.type = "chabu"
        self.ms = 10
        self.hp = 3
        pass

global chabu
chabu = Chabu()