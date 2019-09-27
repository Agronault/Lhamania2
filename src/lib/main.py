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
fonte = pg.font.SysFont('comicsansms', 30)
clock = pg.time.Clock()
_global.elements.add(_global.Lhama1)
_global.elements.add(_global.Enemy1)
_global.elements.add(_global.Enemy2)
_global.elements.add(_global.Enemy3)
_global.elements.add(_global.Guacamole1)

ingameCurrency = 0

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
    # UI
    text = fonte.render('Carregando: {} Entregue: {}'.format(_global.Lhama1.carryCurrency, _global.Lhama1.ingameCurrency), True, const.BLUE)
    textRect = text.get_rect()
    textRect.center = (200, 20)
    background.blit(text, textRect)
    # UI
    pg.display.update()
pg.quit()
