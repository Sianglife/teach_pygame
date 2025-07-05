import pygame as pg
import sys
import Color # 顏色的常數檔

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

    
    for e in pg.event.get():
        # 檢查退出事件(按X關閉視窗)
        """
        試試看: 
        1.如果不加這個檢查，按X關閉視窗會發生什麼事?
        2.按X一定要關視窗嗎?可以按X做其他事情嗎?
        3.有沒有印象APP常看到「確定要退出嗎?」
        """
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(60)  # 控制FPS為每秒60幀
