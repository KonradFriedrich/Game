import pygame as pg


pg.init()

# create window
screenX = 1200
screenY = 1200
screen = pg.display.set_mode((screenX, screenY))

# title and icon (change later)
pg.display.set_caption("Hack and Slay")
icon = pg.image.load('img/knight.png')
pg.display.set_icon(icon)
bgx = 0
bgy = 0