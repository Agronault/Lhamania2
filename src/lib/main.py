import pygame as pg
import const
import _global
from _global import background
from game import drawgame
import events

try:
    pg.init()
except:
    print('[ERROR]: Pygame initialization')

pg.display.set_caption('Lhamania! 2')
run = True
clock = pg.time.Clock()
_global.elements.add(_global.Lhama1)
_global.elements.add(_global.Enemy1)
_global.elements.add(_global.Enemy2)
_global.elements.add(_global.Enemy3)

while run:
    clock.tick(90)
    for event in pg.event.get():
        events.verify(event)
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            exit()
    background.fill(const.WHITE)
    # game
    drawgame()
    # game
    pg.display.update()
pg.quit()
