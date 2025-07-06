import pygame as pg
import sys
import Color

# 初始化pygame
pg.init()
pg.display.set_caption("window Game")

# 視窗大小800x600，也就是後面座標的範圍
screen = pg.display.set_mode((800, 600))

# 預留設定FPS(每秒幾張畫面)的計時工具
clock = pg.time.Clock()

while True:
    screen.fill(Color.BLACK)  # 黑色背景
    pg.display.flip()  # 更新畫面(4move會有更多內容)
    clock.tick(60)  # 控制FPS為每秒60幀

    # 檢查鍵盤輸入
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        print("Left key pressed")
    if keys[pg.K_RIGHT]:
        print("Right key pressed")
    if keys[pg.K_UP]:
        print("Up key pressed")
    if keys[pg.K_DOWN]:
        print("Down key pressed")

    for e in pg.event.get():
        # 檢查退出事件(按X關閉視窗)
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
