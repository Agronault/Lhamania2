import pygame as pg
import const
import sprite
import lane

background = pg.display.set_mode((const.WIDTH, const.HEIGHT))

elements = pg.sprite.Group()

Lhama1 = sprite.Player()

Enemy1 = sprite.Enemy(2)
Enemy2 = sprite.Enemy(1)
Enemy3 = sprite.Enemy(3)

Lane1 = lane.Lane(1, const.WIDTH/2-150)
Lane2 = lane.Lane(2, const.WIDTH/2)
Lane3 = lane.Lane(3, const.WIDTH/2+150)


lanes = [Lane1, Lane2, Lane3]
