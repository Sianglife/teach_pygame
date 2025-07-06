
import pygame as pg
import sys
import Color
from Constant import *

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()


class BackgroundObject(pg.sprite.Sprite):
    def __init__(self, color, width, height, x=100, y=100):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


class Obstacle(BackgroundObject):
    def __init__(self, color, width, height, x=100, y=100):
        super().__init__(color, width, height, x, y)


# 物件初始化
player = Player(Color.WHITE, 200, 150)

obstacles = pg.sprite.Group(
    Obstacle(Color.BLUE, 200, 150),
    Obstacle(Color.GREEN, 100, 100, 200, 400)
)

# 定義移動的函數，並加入反向移動的選項


def move_background(dx, dy):
    global r1_x, r1_y, r2_x, r2_y

    REVERSE = True  # 是否反向移動
    if REVERSE:
        # 顛倒移動的方向
        dx = -dx
        dy = -dy

    r1_x += dx
    r1_y += dy
    r2_x += dx
    r2_y += dy


# 主迴圈
while True:
    screen.fill(Color.BLACK)
    pg.display.flip()

    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        move_background(-5, 0)
    if keys[pg.K_RIGHT]:
        move_background(5, 0)
    if keys[pg.K_UP]:
        move_background(0, -5)
    if keys[pg.K_DOWN]:
        move_background(0, 5)

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS)
