import pygame as pg
import numpy as np
import Ball
import Paddle
import random

WIDTH = 1400
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
color_def = "white"
score_a = 0
score_b = 0

if __name__ == '__main__' : 
    pg.init()
    clock = pg.time.Clock()
    ball = Ball.Ball(500,50,screen)
    font = pg.font.Font(None, 36)

    paddle_a = Paddle.Paddle(10,HEIGHT//2,10,100)
    paddle_b = Paddle.Paddle(WIDTH-20,HEIGHT//2,10,100)
    while True:
        screen.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()  # Thêm lệnh này để thoát chương trình hoàn toàn
            
        paddle_a.Draw(screen)
        paddle_b.Draw(screen)
        
        paddle_a.Move1()
        paddle_b.Move2()
        
        if ball.ball_position[0] <= 0 + 5:
            score_b += 1
            ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
        if ball.ball_position[0] >= WIDTH - 5:
            score_a += 1
            ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng

        score_display = font.render(f"{score_a} : {score_b}", True, color_def)
        screen.blit(score_display, (WIDTH//2 - 20, 10))

        ball.check_boundary(WIDTH,HEIGHT,paddle_a,paddle_b)
            
        ball.Updateposition(HEIGHT)
        ball.Display(screen)
        
        pg.display.flip()
        clock.tick(60)
