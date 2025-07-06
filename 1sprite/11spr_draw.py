
import pygame as pg
import sys
import Color
from Constant import *

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()


class GameObject(pg.sprite.Sprite):
    def __init__(self, size, position=(100, 100)):
        super().__init__()
        self.ori_size = size  # 儲存原始大小
        self.ori_position = position  # 儲存原始位置

    def move(self, dx, dy):
        # 移動物件
        self.rect.x += dx
        self.rect.y += dy

    def set_position(self, position):
        # 設定位置
        self.rect.topleft = position

    def reset(self):
        # 重置大小和位置
        self.rect.topleft = self.ori_position
        self.rect.size = self.ori_size


class CircleObject(GameObject):
    def __init__(self, color, circle_radius, position=(100, 100)):
        super().__init__((circle_radius * 2, circle_radius * 2), position)
        self.image = pg.Surface(
            (circle_radius * 2, circle_radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, color, (circle_radius,
                       circle_radius), circle_radius)
        self.rect = self.image.get_rect(center=position)


class RectangleObject(GameObject):
    def __init__(self, color, size, position=(100, 100)):
        super().__init__(size, position)
        self.ori_position = position
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)


# 物件初始化
player = CircleObject(Color.WHITE, 50, (400, 300))

obstacles = pg.sprite.Group(
    RectangleObject(Color.BLUE, (200, 150), (100, 100)),
    RectangleObject(Color.GREEN, (100, 100), (200, 400))
)

# *代表解包，把obstacles每一項物件都加入到all_sprites中
all_sprites = pg.sprite.Group(player, *obstacles)
backgroundObjects = pg.sprite.Group(*obstacles)


# 主迴圈
while True:
    screen.fill(Color.BLACK)
    all_sprites.draw(screen) # 畫出所有物件
    pg.display.flip()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS)
