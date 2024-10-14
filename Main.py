import pygame as pg
import numpy as np
import Ball

WIDTH = 1024
HEIGHT = 650
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
color_def = "white"




if __name__ == '__main__' : 
    clock = pg.time.Clock()
    ball = Ball.Ball(50,50)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        ball.Draw(screen)
        

        pg.display.flip()
        clock.tick(60)