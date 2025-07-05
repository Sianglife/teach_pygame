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


# 方形的位置變數

rect_x = 100
rect_y = 100

while True:
    screen.fill(Color.BLACK)  # 黑色背景

    # 繪製圖形
    """
    想想看:
    1.為什麼要用變數來記錄位置?前面為什麼數字就好?
    2.方形移動的時候，變數怎麼變化?
    """
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

    """
    試試看:
    1.如果FPS降低，畫面會變得怎樣?試試調成10
    2.大概臨界再多少FPS時，畫面會開始卡頓?
    """
    clock.tick(60)  # 控制FPS為每秒60幀
