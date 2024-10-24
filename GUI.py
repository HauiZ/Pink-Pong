import pygame as pg
import numpy as np
import Ball
import Paddle
import random
import Atribute_ball
import threading

WIDTH = 1400
HEIGHT = 700
color_def = "white"
score_a = 0
score_b = 0
combo_countera = 0
combo_counterb = 0
game_state = "game_menu"
mode = "single"
mode_changed = False


class Draw():
    def __init__(self,window):
        self.lock = threading.Lock()
        self.background = pg.image.load('images/field.png')
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        self.ball = Ball.Ball(WIDTH // 2, random.randint(20,HEIGHT-20),window)
        self.test_ball = Atribute_ball.Atribute_ball(random.randint(WIDTH//4, WIDTH - WIDTH//4),0,window)
        self.font = pg.font.Font(None, 36)
        self.paddle_a = Paddle.Paddle(10,0,10,700)
        self.paddle_b = Paddle.Paddle(WIDTH-20,0,10,100)
        

    def draw_game_menu(self,mode,mode_map,window):
        table_surface = pg.Surface((WIDTH * 0.5, HEIGHT * 0.3)) 
        table_surface.fill((0, 0, 0)) 
        pg.draw.rect(table_surface, (255, 255, 255), table_surface.get_rect(), 10)  
        mode_game_clolor = "green" if mode == "single" else "red"
        text = self.font.render("Welcome to Pong!", True, "white")
        start = self.font.render("Press Space to start", True, "white")
        mode_game = self.font.render("Press R to switch mode : ", True, "white")
        mode_game_left_txt = self.font.render(f"<<", True, "white")
        mode_game_changed = self.font.render(f"{mode}", True, mode_game_clolor)
        mode_game_right_txt = self.font.render(f">>", True, "white")
        mode_map_text = self.font.render("Press [A,D] to change map : ", True, "white")
        if mode_map == "map1":
            mode_map_color = "white"
        elif mode_map == "map2":
            mode_map_color = "yellow"
        else:
            mode_map_color = "blue"
        mode_map_left_txt = self.font.render(f"<<", True, "white")
        mode_map_changed = self.font.render(f"{mode_map}", True, mode_map_color)
        mode_map_right_txt = self.font.render(f">>", True, "white")
        table_surface.blit(text, (WIDTH * 0.16, 20))
        table_surface.blit(start, (WIDTH * 0.155, 60))
        table_surface.blit(mode_game, (WIDTH * 0.11, 100))
        table_surface.blit(mode_game_left_txt, (WIDTH * 0.33, 100))
        table_surface.blit(mode_game_changed, (WIDTH * 0.36, 100))
        table_surface.blit(mode_game_right_txt, (WIDTH * 0.42, 100))
        table_surface.blit(mode_map_text, (WIDTH * 0.11, 140))
        table_surface.blit(mode_map_left_txt, (WIDTH * 0.35, 140))
        table_surface.blit(mode_map_changed, (WIDTH * 0.38, 140))
        table_surface.blit(mode_map_right_txt, (WIDTH * 0.44, 140))
        window.blit(self.background, (0, 0))
        window.blit(table_surface, (WIDTH//2 - table_surface.get_width()//2, HEIGHT//3))
    

    def draw_game_over(self,winner,window):
        window.blit(self.background, (0, 0))
        text = self.font.render(f"Player {winner} win!", True, "red")
        restart = self.font.render("Press R to restart", True, "red")
        window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
        window.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2))
        

    def draw_map(self,window):
        with self.lock:
            window.blit(self.background, (0, 0))
            
    def change_background(self, new_background_path):
        with self.lock:
            self.background = pg.image.load(new_background_path)
            self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
