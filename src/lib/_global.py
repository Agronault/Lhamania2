import pygame as pg
import const
import sprite
import lane


page = 1   # 1=menu, 2=game, 3=

background = pg.display.set_mode((const.WIDTH, const.HEIGHT))

elementsgame = pg.sprite.Group()
elementsmenu = pg.sprite.Group()

Lhama1 = sprite.Player(pg.image.load('../../media/sprite/Skin0Test.png').convert_alpha())

Fundo1Game = sprite.Fundo(pg.image.load('../../media/img/FundoTest.png').convert_alpha())
Fundo1Menu = sprite.Fundo(pg.image.load('../../media/img/MenuTest.png').convert_alpha())


Enemy1 = sprite.Enemy(2)
Enemy2 = sprite.Enemy(1)
Enemy3 = sprite.Enemy(3)

Guacamole1 = sprite.Point(3)

Lane1 = lane.Lane(1, const.WIDTH/2-150)
Lane2 = lane.Lane(2, const.WIDTH/2)
Lane3 = lane.Lane(3, const.WIDTH/2+150)


lanes = [Lane1, Lane2, Lane3]
