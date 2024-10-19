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
background = pg.image.load('Tennis.jpeg')
background = pg.transform.scale(background, (WIDTH, HEIGHT))
game_state = "playing"

def draw_game_over(winner):
    screen.blit(background, (0, 0))
    text = font.render(f"Player {winner} win!", True, "red")
    restart = font.render("Press R to restart", True, "red")
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2))

def draw_objects():
    screen.blit(background, (0, 0))
    paddle_a.Draw(screen)
    paddle_b.Draw(screen)
    ball.Display(screen)
    score_display = font.render(f"{score_a} : {score_b}", True, "yellow")
    screen.blit(score_display, (WIDTH//2 - 20, 10))

if __name__ == '__main__' : 
    pg.init()
    clock = pg.time.Clock()
    ball = Ball.Ball(WIDTH // 2, random.randint(20,HEIGHT-20),screen)
    font = pg.font.Font(None, 36)
    paddle_a = Paddle.Paddle(10,0,10,HEIGHT)
    paddle_b = Paddle.Paddle(WIDTH-20,0,10,HEIGHT)
    while True:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()  # Thêm lệnh này để thoát chương trình hoàn toàn
        if game_state == "playing":
                
            paddle_a.Move1()
            paddle_b.Move2()
            draw_objects()
            ball.check_boundary(WIDTH,HEIGHT,paddle_a,paddle_b)
            if ball.ball_position[0] <= 0 + 5:
                score_b += 1
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
            if ball.ball_position[0] >= WIDTH - 5:
                score_a += 1
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
            
           
                
            ball.Updateposition(HEIGHT)
        

        if score_a >= 10 or score_b >= 10:
            game_state = "game_over"
            winner = "A" if score_a > score_b else "B"
            draw_game_over(winner)
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                game_state = "playing"
                score_a = score_b = 0
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
                paddle_a.Reset(10,HEIGHT//2)
                paddle_b.Reset(WIDTH-20,HEIGHT//2)
        
        pg.display.flip()
        clock.tick(60)

