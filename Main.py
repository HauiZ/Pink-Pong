from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
import numpy as np
import random
from source_code import Ball
from source_code import Paddle
from source_code import Atribute_ball
from source_code import GUI 
from source_code import Sound_config
from source_code import logic_score
WIDTH = 1400
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
color_def = "white"

combo_countera = 0 
combo_counterb = 0 

game_state = "game_menu"
mode = "single" 
mode_changed = False 
mode_changed_1 = False
mode_changed_2 = False 
clicked = False 
clicked_1 = False
mode_map = "map1"


 
def draw_objects(window, background):
        
    window.blit(background, (0, 0))
    paddle_a.Draw(window)
    paddle_b.Draw(window)
    test_ball.Display(window)
    ball.Display(window)
    Draw.score_board(logic.game_score_a,logic.game_score_b,logic.set1_score_a,logic.set1_score_b,logic.tb_score_a,logic.tb_score_b,window)
    
if __name__ == '__main__' : 
    pg.init()
        
    clock = pg.time.Clock()
    ball = Ball.Ball(20, random.randint(20,HEIGHT-20),screen)
    font = pg.font.Font(None, 36)
    paddle_a = Paddle.Paddle(10,HEIGHT//2-50,10,100)
    paddle_b = Paddle.Paddle(WIDTH-20,HEIGHT//2-50,10,100)
    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4),0,screen)
    Draw = GUI.Draw(screen)
    logic = logic_score.logic_score()
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
                logic.playera_points = 0
                logic.playerb_points = 0
                logic.score_a.clear()
                logic.score_b.clear()
                logic.game_score_a = "0"
                logic.game_score_b = "0"
                logic.set1_score_a = 0
                logic.set1_score_b = 0
                logic.tb_score_a = 0
                logic.tb_score_b = 0
                combo_countera = 0 
                combo_counterb = 0
                ball = Ball.Ball(30,HEIGHT//2,screen)
                paddle_a.Reset(10,HEIGHT//2-50)
                paddle_b.Reset(WIDTH-20,HEIGHT//2-50)
                
        
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
            
            

            ball.check_boundary(WIDTH,HEIGHT,paddle_a,paddle_b)
            if ball.ball_position[0] <= 0 + 5:
                logic.update_playerbpoints()
                combo_counterb += 1
                combo_countera = 0
                ball.Reset(WIDTH-30, HEIGHT//2)
                paddle_a.Reset(10,HEIGHT//2-50)
                paddle_b.Reset(WIDTH-20,HEIGHT//2-50)
                #logic score
                logic.game_scoreb()
                logic.SetScoreb()
                logic.Sound()
                if combo_counterb % 3 == 0:
                    Sound_config.ohh.play()    #lệnh chạy âm thanh
                    Sound_config.ohh.set_volume(0.7)  
                    combo_counterb = 0

            if ball.ball_position[0] >= WIDTH - 5:
                logic.update_playerapoints()
                combo_countera +=1
                combo_counterb = 0
                ball.Reset(30, HEIGHT//2)
                paddle_a.Reset(10,HEIGHT//2-50)
                paddle_b.Reset(WIDTH-20,HEIGHT//2-50)
                #logic score
                logic.game_scorea()
                logic.SetScorea()
                logic.Sound()
                if combo_countera % 3 == 0:
                    Sound_config.ohh.play()
                    Sound_config.ohh.set_volume(0.7)   
                    combo_countera = 0

            if ball.ball.colliderect(paddle_a) or (ball.ball_position[0] <= 20 and (ball.ball_position[1] >= paddle_a.paddle_position[1] and ball.ball_position[1] <= paddle_a.paddle_position[1] + paddle_a.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
            elif ball.ball.colliderect(paddle_b) or (ball.ball_position[0] >= WIDTH - 20 and (ball.ball_position[1] >= paddle_b.paddle_position[1] and ball.ball_position[1] <= paddle_b.paddle_position[1] + paddle_b.height)):
                if test_ball.active == False:
                    test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4), 0, screen)  # Tạo test_ball
                
            ball.Updateposition(HEIGHT,test_ball, paddle_a, paddle_b,screen)
            test_ball.Updateposition(HEIGHT,WIDTH)

        if logic.gameover() == True : 
            game_state = "game_over"
            winner = "A" if logic.set1_score_a > logic.set1_score_b else "B" 
            Draw.draw_game_over(winner, screen)
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                Sound_config.chosed_sound.play()
                game_state = "game_menu"
                Draw.change_background('images/field.png')
                Draw.background = pg.transform.scale(Draw.background, (WIDTH, HEIGHT))
                logic.playera_points = 0
                logic.playerb_points = 0
                logic.score_a.clear()
                logic.score_b.clear()
                logic.game_score_a = "0"
                logic.game_score_b = "0"
                logic.set1_score_a = 0
                logic.set1_score_b = 0
                logic.tb_score_a = 0
                logic.tb_score_b = 0
                ball.Reset(30, HEIGHT//2)
                paddle_a.Reset(10,HEIGHT//2-50)
                paddle_b.Reset(WIDTH-20,HEIGHT//2-50)
        
        pg.display.flip()
        clock.tick(90)
