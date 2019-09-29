import pygame as pg
import const
import _global
from _global import background
from game import drawgame
from game import drawmenu
import events

try:
    pg.init()
except:
    print('[ERROR]: Pygame initialization')

pg.display.set_caption('Lhamania! 2')
run = True
fonte = pg.font.SysFont('comicsansms', 30)
pg.mixer.music.load('../../media/audio/hp_background.mp3')
pg.mixer.music.play()  # deve ser enviado para inicializaJogo assim que a função for feita
clock = pg.time.Clock()
_global.elementsgame.add(_global.Fundo1Game)
_global.elementsgame.add(_global.Enemy1)
_global.elementsgame.add(_global.Enemy2)
_global.elementsgame.add(_global.Enemy3)
_global.elementsgame.add(_global.Guacamole1)
_global.elementsgame.add(_global.Lhama1)

_global.elementsmenu.add(_global.Fundo1Menu)

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
    if _global.page == 1:
        drawmenu()
    elif _global.page == 2:
        drawgame()
        text = fonte.render(
            'Carregando: {} Entregue: {}'.format(_global.Lhama1.carryCurrency, _global.Lhama1.ingameCurrency), True,
            const.BLUE)
        textRect = text.get_rect()
        textRect.center = (200, 20)
        background.blit(text, textRect)
    # game
    pg.display.update()
pg.quit()
