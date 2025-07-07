import pygame as pg
import sys
from Const import *

# 初始化pygame
pg.init()
pg.display.set_caption("window Game")

# 視窗大小800x600，也就是後面座標的範圍
screen = pg.display.set_mode((800, 600))

clock = pg.time.Clock()

r_x = 300
r_y = 200

c_color=WHITE

while True:
    screen.fill(BLACK)
    # (X, Y, Width, Height)
    r = pg.draw.rect(screen, RED, (r_x, r_y, 200, 100))
    c = pg.draw.circle(screen, c_color, (100, 200), 50)

    pg.display.flip()

    if c.colliderect(r):
        c_color=GREEN
    else:
        c_color=WHITE



    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        r_x -= 2
    if keys[pg.K_RIGHT]:
        r_x += 2
    if keys[pg.K_UP]:
        print("Up key pressed")
    if keys[pg.K_DOWN]:
        print("Down key pressed")

    for e in pg.event.get():
        # 檢查退出事件(按X關閉視窗)
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(60)
