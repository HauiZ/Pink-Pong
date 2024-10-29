import pygame as pg
import numpy as np
import Ball
import Paddle
import random
import Atribute_ball
import GUI 
import Sound_config
WIDTH = 1400
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
color_def = "white"
score_a = 0 #score a
score_b = 0 #score b
combo_countera = 0 #combo counter a
combo_counterb = 0 #combo counter b
game_state = "game_menu" #game state
mode = "single" #mode game
mode_changed = False #mode changed
mode_changed_1 = False #mode changed 1
mode_changed_2 = False #mode changed 2
clicked = False #clicked
clicked_1 = False #clicked 1
mode_map = "map1" #mode map



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
        
    clock = pg.time.Clock()
    ball = Ball.Ball(WIDTH // 2, random.randint(20,HEIGHT-20),screen)
    font = pg.font.Font(None, 36)
    paddle_a = Paddle.Paddle(10,0,10,700)
    paddle_b = Paddle.Paddle(WIDTH-20,0,10,100)
    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4),0,screen)
    Draw = GUI.Draw(screen)
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if game_state == "playing":
                        game_state = "setting"
                    elif game_state == "setting":
                        game_state = "playing"

        Draw.draw_map(screen)
        if game_state == "game_menu":
            

            Draw.draw_game_menu(mode,mode_map ,screen)
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                
                Sound_config.chosed_sound.play()
                game_state = "playing"

            if keys[pg.K_r]:
                if not mode_changed:
                    mode_changed = True
                    
                    Sound_config.tick_sound.play()
                    if mode == "single":
                        mode = "player"
                    elif mode == "player":
                        mode = "single"
                    
            else:
                mode_changed = False 

            if keys[pg.K_m]:
                if not mode_changed_1:
                    mode_changed_1 = True
                    Sound_config.tick_sound.play()
                    if mode_map == "map1":
                        Draw.change_background('images/sand_field.png')
                        mode_map = "map2"
                    elif mode_map == "map2":
                        Draw.change_background('images/space_field.png')
                        mode_map = "map3"
                    elif mode_map == "map3":
                        Draw.change_background('images/field.png')
                        mode_map = "map1"
            else:
                mode_changed_1 = False
 
        
        elif game_state == "setting":
            Draw.draw_setting_menu(screen)
            result = Draw.handle_settings_navigation(events)
            if result == "game_menu":
                game_state = "game_menu"
                Sound_config.chosed_sound.play()
        
        elif game_state == "playing": 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        game_state = "setting"
                        
            paddle_a.Move1()
            if mode == "player":
                paddle_b.Move2()
            elif mode == "single":
                if paddle_b.rect.y + paddle_b.rect.height/2 > int(ball.ball_position[1]) and abs(paddle_b.rect.y - ball.ball_position[1]) > 0:
                    paddle_b.paddble_b_up()
                elif paddle_b.rect.y + paddle_b.rect.height/2 < int(ball.ball_position[1]) and abs(paddle_b.rect.y - ball.ball_position[1]) > 0:
                    paddle_b.paddble_b_down()
            draw_objects(screen, Draw.background)
            # ball.check_Hit_Atribute(test_ball)
            ball.check_boundary(WIDTH,HEIGHT,paddle_a,paddle_b)
            if ball.ball_position[0] <= 0 + 5:
                score_b += 1
                combo_counterb += 1
                combo_countera = 0
                ball.Reset(paddle_b.x+paddle_b.width+10, random.randint(paddle_b.y + 10,paddle_b.y+paddle_b.height-10 ))  # Đặt lại vị trí bóng
                if combo_counterb % 3 == 0:
                    
                    Sound_config.cheer.play()    #lệnh chạy âm thanh
                    combo_counterb = 0
                elif score_a - score_b >= 4 and combo_counterb == 1:
                    
                    Sound_config.ohh.play()
            if ball.ball_position[0] >= WIDTH - 5:
                score_a += 1
                combo_countera += 1
                combo_counterb = 0
                ball.Reset(paddle_a.x+paddle_a.width+10, random.randint(paddle_a.y + 10,paddle_a.y+paddle_a.height-10 ))  # Đặt lại vị trí bóng
                if combo_countera % 3 == 0:
                    
                    Sound_config.cheer.play()   
                    combo_countera = 0
                elif score_b - score_a >= 4 and combo_countera == 1:
                    
                    Sound_config.ohh.play()
            if ball.ball.colliderect(paddle_a) or (ball.ball_position[0] <= 20 and (ball.ball_position[1] >= paddle_a.paddle_position[1] and ball.ball_position[1] <= paddle_a.paddle_position[1] + paddle_a.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
            elif ball.ball.colliderect(paddle_b) or (ball.ball_position[0] >= WIDTH - 20 and (ball.ball_position[1] >= paddle_b.paddle_position[1] and ball.ball_position[1] <= paddle_b.paddle_position[1] + paddle_b.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
                
            ball.Updateposition(HEIGHT,test_ball, paddle_a, paddle_b,screen)
            test_ball.Updateposition(HEIGHT,WIDTH)

        if score_a >= 10 or score_b >= 10:
            game_state = "game_over"
            winner = "A" if score_a > score_b else "B"
            Draw.draw_game_over(winner, screen)
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                Sound_config.chosed_sound.play()
                game_state = "game_menu"
                Draw.change_background('images/field.png')
                Draw.background = pg.transform.scale(Draw.background, (WIDTH, HEIGHT))
                score_a = score_b = 0
                ball.Reset(WIDTH // 2, random.randint(20,HEIGHT-20))  # Đặt lại vị trí bóng
                paddle_a.Reset(10,HEIGHT//2)
                paddle_b.Reset(WIDTH-20,HEIGHT//2)
        
        pg.display.flip()
        clock.tick(90)
