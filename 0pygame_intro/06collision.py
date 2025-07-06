"""
你會學到:
1. 如何檢查圖形間的碰撞
2. 如何改變顏色
"""

import pygame as pg
import sys
import Color
from Constant import *  # 把Constant.py裡面的變數都引入進來，通常常數(不會變動的變數)會用全大寫命名

# 初始化pygame
pg.init()
pg.display.set_caption("window Game")

# 視窗大小依照常數設定
screen = pg.display.set_mode(SCREEN_SCALE)

# 預留設定FPS(每秒幾張畫面)的計時工具
clock = pg.time.Clock()


# 方形的位置變數
r_x = 100
r_y = 100
c_color = Color.RED

while True:
    screen.fill(Color.BLACK)  # 黑色背景

    # 繪製圖形，加上指定成變數
    r = pg.draw.rect(screen, Color.BLUE, (r_x, r_y, 200, 150))  # 正方形
    c = pg.draw.circle(screen, c_color, (200, 175), 50)  # 在方形內畫一個圓

    # 檢查碰撞
    if c.colliderect(r):  # 如果圓形碰到方形
        c_color = Color.WHITE
    else:
        # 沒碰到就恢復圓的顏色
        c_color = Color.RED

    # 更新畫面(4move會有更多內容)
    pg.display.flip()

    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        r_x -= 5  # 改變方形的x座標
    if keys[pg.K_RIGHT]:
        r_x += 5
    if keys[pg.K_UP]:
        r_y -= 5  # 改變方形的y座標
    if keys[pg.K_DOWN]:
        r_y += 5

    for e in pg.event.get():
        # 檢查退出事件(按X關閉視窗)
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS)  # 控制FPS為常數的值
