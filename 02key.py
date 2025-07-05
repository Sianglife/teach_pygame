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

    # 檢查鍵盤輸入
    """
    試試看:
    1.怎麼做可以讓按下ESC鍵時，程式結束? Hint: pg.K_ESCAPE
    2.keys裡面長什麼樣子?print出來看看。
    3.取keys[pg.K_LEFT]是什麼原理?為什麼拿他用if判斷?
    """
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

    clock.tick(60)  # 控制FPS為每秒60幀
