import pygame as pg
import sys
import Color
from Constant import *  # 把Constant.py裡面的變數都引入進來，通常常數(不會變動的變數)會用全大寫命名

"""
想想看:
1.什麼樣的變數適合用常數來定義?為什麼?
"""

# 初始化pygame
pg.init()
pg.display.set_caption("window Game")

# 視窗大小依照常數設定
screen = pg.display.set_mode(SCREEN_SCALE) 

# 預留設定FPS(每秒幾張畫面)的計時工具
clock = pg.time.Clock()


# 方形的位置變數
rect_x = 100
rect_y = 100

while True:
    screen.fill(Color.BLACK)  # 黑色背景

    # 繪製圖形
    pg.draw.rect(screen, Color.RED, (rect_x, rect_y, 200, 150))  # 正方形

    # 更新畫面(4move會有更多內容)
    pg.display.flip()

    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        print("Left key pressed")
        rect_x -= 5  # 改變方形的x座標
    if keys[pg.K_RIGHT]:
        print("Right key pressed")
        rect_x += 5
    if keys[pg.K_UP]:
        print("Up key pressed")
        rect_y -= 5  # 改變方形的y座標
    if keys[pg.K_DOWN]:
        print("Down key pressed")
        rect_y += 5

    for e in pg.event.get():
        # 檢查退出事件(按X關閉視窗)
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS)  # 控制FPS為常數的值
