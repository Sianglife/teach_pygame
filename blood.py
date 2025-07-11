import pygame as pg
import sys
import Color

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode((800, 600))

clock = pg.time.Clock()

blood = 5

space_last_status = None

while True:
    screen.fill(Color.BLACK)
    pg.draw.rect(screen, Color.RED, (100, 100, 40 * 5, 150))
    pg.display.flip()

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE] and keys[pg.K_SPACE] != space_last_status:
        blood -= 1
    space_last_status = keys[pg.K_SPACE]

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(60)
