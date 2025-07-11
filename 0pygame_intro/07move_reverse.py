import pygame as pg
import sys
import Color
from Constant import *

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()


# 變數初始化

r1_x = 100
r1_y = 100

r2_x = 200
r2_y = 400

c_color = Color.RED


# 定義移動的函數，並加入反向移動的選項
def move(dx, dy, REVERSE=True):
    global r1_x, r1_y, r2_x, r2_y

    """
    想想看:
    1.如果固定圓形，只移動方形，怎麼樣可以感覺是圓形在移動？
    """
    if REVERSE:
        dx = -dx
        dy = -dy

    r1_x += dx
    r1_y += dy
    r2_x += dx
    r2_y += dy


# 主迴圈
while True:
    screen.fill(Color.BLACK)
    r1 = pg.draw.rect(screen, Color.BLUE, (r1_x, r1_y, 200, 150))
    r2 = pg.draw.rect(screen, Color.GREEN, (r2_x, r2_y, 100, 100))
    c = pg.draw.circle(screen, c_color, (200, 175), 50)

    pg.display.flip()

    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        move(-5, 0)
    if keys[pg.K_RIGHT]:
        move(5, 0)
    if keys[pg.K_UP]:
        move(0, -5)
    if keys[pg.K_DOWN]:
        move(0, 5)

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS)
