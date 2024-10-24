from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
import numpy as np
import Ball
import Paddle
import random
import Atribute_ball
import GUI 
WIDTH = 1400
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
color_def = "white"
score_a = 0
score_b = 0
combo_countera = 0
combo_counterb = 0
game_state = "game_menu"
mode = "single"
mode_changed = False
mode_changed_1 = False
mode_changed_2 = False
mode_map = "map1"




def draw_objects(window, background):
        
    window.blit(background, (0, 0))
    paddle_a.Draw(window)
    paddle_b.Draw(window)
    test_ball.Display(window)
    ball.Display(window)
    score_display = font.render(f"{score_a} : {score_b}", True, "red")
    window.blit(score_display, (WIDTH//2 - 26, 10))

if __name__ == '__main__' : 
    pg.init()
    pg.mixer.init()
    cheer = pg.mixer.Sound('sound/Cheering.wav')  #Thiết lập âm thanh cổ động viên 
    ohh = pg.mixer.Sound('sound/ohh.wav')         #Thiết lp âm thanh cổ động viên
    clock = pg.time.Clock()
    ball = Ball.Ball(WIDTH // 2, random.randint(20,HEIGHT-20),screen)
    font = pg.font.Font(None, 36)
    paddle_a = Paddle.Paddle(10,0,10,700)
    paddle_b = Paddle.Paddle(WIDTH-20,0,10,100)
    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4),0,screen)
    Draw = GUI.Draw(screen)
    while True:
        Draw.draw_map(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()  # Thêm lệnh này để thoát chương trình hoàn toàn
        
        if game_state == "game_menu":
            Draw.draw_game_menu(mode,mode_map ,screen)
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                game_state = "playing"

            if keys[pg.K_r]:
                if not mode_changed:
                    mode_changed = True
                    if mode == "single":
                        mode = "player"
                    elif mode == "player":
                        mode = "single"
                    
            else:
                mode_changed = False 

            if keys[pg.K_a]:
                if not mode_changed_1:
                    mode_changed_1 = True
                    if mode_map == "map2":
                        Draw.change_background('images/field.png')
                        mode_map = "map1"
                    elif mode_map == "map3":
                        Draw.change_background('images/sand_field.png')
                        mode_map = "map2"
                    elif mode_map == "map1":
                        Draw.change_background('images/space_field.png')
                        mode_map = "map3"
            else:
                mode_changed_1 = False
            if keys[pg.K_d]:
                if not mode_changed_2:
                    mode_changed_2 = True
                    if mode_map == "map2":
                        Draw.change_background('images/space_field.png')
                        mode_map = "map3"
                    elif mode_map == "map1":
                        Draw.change_background('images/sand_field.png')
                        mode_map = "map2"
                    elif mode_map == "map3":
                        Draw.change_background('images/field.png')
                        mode_map = "map1"
            else:
                mode_changed_2 = False 
        
        elif game_state == "playing":    
            paddle_a.Move1()
            if mode == "player":
                paddle_b.Move2()
            elif mode == "single":
                if paddle_b.rect.y + paddle_b.height/2 > int(ball.ball_position[1]) and abs(paddle_b.rect.y - ball.ball_position[1]) > 0:
                    paddle_b.paddble_b_up()
                elif paddle_b.rect.y + paddle_b.height/2 < int(ball.ball_position[1]) and abs(paddle_b.rect.y - ball.ball_position[1]) > 0:
                    paddle_b.paddble_b_down()
            draw_objects(screen, Draw.background)
            # ball.check_Hit_Atribute(test_ball)
            ball.check_boundary(WIDTH,HEIGHT,paddle_a,paddle_b)
            if ball.ball_position[0] <= 0 + 5:
                score_b += 1
                combo_counterb += 1
                combo_countera = 0
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
                if combo_counterb % 3 == 0:
                    cheer.set_volume(0.5)
                    cheer.play()    #lệnh chạy âm thanh
                    combo_counterb = 0
                elif score_a - score_b >= 4 and combo_counterb == 1:
                    ohh.set_volume(0.7)
                    ohh.play()
            if ball.ball_position[0] >= WIDTH - 5:
                score_a += 1
                combo_countera += 1
                combo_counterb = 0
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
                if combo_countera % 3 == 0:
                    cheer.set_volume(0.5)
                    cheer.play()    
                    combo_countera = 0
                elif score_b - score_a >= 4 and combo_countera == 1:
                    ohh.set_volume(0.7)
                    ohh.play()
            if ball.ball.colliderect(paddle_a) or (ball.ball_position[0] <= 20 and (ball.ball_position[1] >= paddle_a.paddle_position[1] and ball.ball_position[1] <= paddle_a.paddle_position[1] + paddle_a.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
            elif ball.ball.colliderect(paddle_b) or (ball.ball_position[0] >= WIDTH - 20 and (ball.ball_position[1] >= paddle_b.paddle_position[1] and ball.ball_position[1] <= paddle_b.paddle_position[1] + paddle_b.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
                
            ball.Updateposition(HEIGHT,test_ball, paddle_a, paddle_b, Draw)
            test_ball.Updateposition(HEIGHT,WIDTH)

        if score_a >= 10 or score_b >= 10:
            game_state = "game_over"
            winner = "A" if score_a > score_b else "B"
            Draw.draw_game_over(winner, screen)
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                game_state = "game_menu"
                Draw.change_background('images/field.png')
                Draw.background = pg.transform.scale(Draw.background, (WIDTH, HEIGHT))
                score_a = score_b = 0
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
                paddle_a.Reset(10,HEIGHT//2)
                paddle_b.Reset(WIDTH-20,HEIGHT//2)
        
        pg.display.flip()
        clock.tick(90)
