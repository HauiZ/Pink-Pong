import pygame as pg
import numpy as np
import Ball
import Paddle

WIDTH = 1024
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
color_def = "white"

if __name__ == '__main__' : 
    pg.init()
    clock = pg.time.Clock()
<<<<<<< Updated upstream
    ball = Ball.Ball(50,50,screen)
    
=======
    ball = Ball.Ball(50,50)
    paddle_a = Paddle.Paddle(0,HEIGHT//2 - 50,10,100)
    paddle_b = Paddle.Paddle(WIDTH-10,HEIGHT//2 - 50,10,100)
>>>>>>> Stashed changes
    while True:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
<<<<<<< Updated upstream
=======
            
        paddle_a.Move1()
        paddle_b.Move2()
        
        screen.fill("black")

        ball.Draw(screen)
        paddle_a.Draw(screen)
        paddle_b.Draw(screen)

>>>>>>> Stashed changes

        #bound
        bar = pg.draw.rect(screen,(255, 192, 203),pg.Rect(10,0,10,HEIGHT))
        bar2 = pg.draw.rect(screen,(255, 192, 203),pg.Rect(WIDTH -20,0,10,HEIGHT))


        if pg.Rect.colliderect(ball.ball,bar) or pg.Rect.colliderect(ball.ball,bar2):
            ball.Hit()
        ball.Updateposition(HEIGHT)
        ball.Display(screen)
        
       
        pg.display.flip()
        clock.tick(60)