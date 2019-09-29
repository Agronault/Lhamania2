import pygame as pg
import _global


def verify(event):
    if event.type == pg.KEYDOWN:
        verifyKey(event)
    elif event.type == pg.MOUSEBUTTONDOWN and _global.page == 1:
        _global.page = 2


def verifyKey(event):
    if event.key == pg.K_LEFT:
        if _global.Lhama1.lane > 1:
            _global.Lhama1.lane -= 1
    elif event.key == pg.K_RIGHT:
        if _global.Lhama1.lane < 3:
            _global.Lhama1.lane += 1
