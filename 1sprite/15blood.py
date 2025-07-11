import pygame as pg
import sys
import Color
import math
from Constant import *

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()


class blood:
    def __init__(self, x, y):
        self.hp = 100
        self.bg = pg.Surface((200, 20))
        self.bg_rect = self.bg.get_rect(center=(x, y))
        self.bg.fill(Color.BLACK)
        self.blood = pg.Surface((200, 20))
        self.blood_rect = self.blood.get_rect(center=(x, y))

    def update(self):
        self.blood_rect.width = self.hp / 100 * 200

    def draw(self, surface):
        surface.blit(self.bg, self.bg_rect)
        surface.blit(self.blood, self.blood_rect)

    def damage(self, value):
        self.hp -= value
        if self.hp < 0:
            self.hp = 0
        self.update()
    

hp = blood(100, 100)

# 主迴圈
while True:
    screen.fill(Color.BLACK)
    hp.draw(screen)
    pg.display.flip()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()

    hp.damage(0.1)  # 每次迴圈減少血量
    
    clock.tick(FPS)
