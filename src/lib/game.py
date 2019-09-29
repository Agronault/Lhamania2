import pygame as pg
from _global import *


def drawgame():
    elementsgame.update()
    elementsgame.draw(background)


def drawmenu():
    elementsmenu.draw(background)