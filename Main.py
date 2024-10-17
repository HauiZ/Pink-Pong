import pygame as pg
import numpy as np
import Ball

WIDTH = 1024
HEIGHT = 650
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
color_def = "white"

if __name__ == '__main__' : 
    pg.init()
    clock = pg.time.Clock()
    ball = Ball.Ball(50,50,screen)
    
    while True:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        #bound
        bar = pg.draw.rect(screen,(255, 192, 203),pg.Rect(10,0,10,HEIGHT))
        bar2 = pg.draw.rect(screen,(255, 192, 203),pg.Rect(WIDTH -20,0,10,HEIGHT))


        if pg.Rect.colliderect(ball.ball,bar) or pg.Rect.colliderect(ball.ball,bar2):
            ball.Hit()
        ball.Updateposition(HEIGHT)
        ball.Display(screen)
        
       
        pg.display.flip()
        clock.tick(60)