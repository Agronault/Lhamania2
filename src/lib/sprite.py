import pygame as pg
import const
import _global


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(const.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (const.WIDTH/2, const.HEIGHT/2)
        self.lane = 2

    def update(self):
        self.rect.x += (_global.lanes[self.lane-1].x-self.rect.x)/4


class Enemy(pg.sprite.Sprite):
    def __init__(self, lane):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((25, 25))
        self.image.fill(const.RED)
        self.rect = self.image.get_rect()
        if lane == 1:
            self.rect.center = (const.WIDTH/2-150, 0)
        elif lane == 2:
            self.rect.center = (const.WIDTH/2, -50)
        elif lane == 3:
            self.rect.center = (const.WIDTH/2+150, -100)
        self.lane = lane

    def update(self):
        if const.HEIGHT/2+10 > self.rect.y > const.HEIGHT/2-10 and _global.Lhama1.lane == self.lane:
            print('PERDEU')
        self.rect.y += 5
        if self.rect.y > const.HEIGHT + 25:
            self.rect.y = -25
            self.rect.x = _global.lanes[self.lane-1].x
        if self.lane == 1:
            self.rect.x -= 1
        if self.lane == 3:
            self.rect.x += 1

