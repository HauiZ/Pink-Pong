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
        self.settings_font = pg.font.Font(None, 30)  # Smaller font for settings
        self.selected_option = 1  # Initialize selected_option
        self.blink_timer = 0
        self.blink_interval = 500  # Blink every 100 milliseconds (10 times per second)

        

    def draw_game_menu(self,mode,mode_map,window):
        table_surface = pg.Surface((WIDTH * 0.5, HEIGHT * 0.3)) 
        table_surface.fill((0, 0, 0)) 
        pg.draw.rect(table_surface, (255, 255, 255), table_surface.get_rect(), 10)  
        mode_game_clolor = "green" if mode == "single" else "red"
        text = self.font.render("Welcome to Pong!", True, "white")
        start = self.font.render("Press Space to start", True, "white")
        mode_game = self.font.render("Press R to switch mode : ", True, "white")
        mode_game_changed = self.font.render(f"{mode}", True, mode_game_clolor)
        mode_map_text = self.font.render("Press M to change map : ", True, "white")
        if mode_map == "map1":
            mode_map_color = "white"
        elif mode_map == "map2":
            mode_map_color = "yellow"
        else:
            mode_map_color = "blue"
        mode_map_changed = self.font.render(f"{mode_map}", True, mode_map_color)
        table_surface.blit(text, (WIDTH * 0.16, 20))
        table_surface.blit(start, (WIDTH * 0.155, 60))
        table_surface.blit(mode_game, (WIDTH * 0.11, 100))
        table_surface.blit(mode_game_changed, (WIDTH * 0.36, 100))
        table_surface.blit(mode_map_text, (WIDTH * 0.11, 140))
        table_surface.blit(mode_map_changed, (WIDTH * 0.36, 140))
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



    def draw_setting(self, surface, start_y):
        settings = ["SETTINGS", "SFX", "CONTROLLER"]
        y_offset = 20
        line_spacing = 100

        settings_font = pg.font.Font(None, 64)
        
        # Calculate blink color using milliseconds for smoother transitions
        current_time = pg.time.get_ticks()
        blink_color = "red" if (current_time // self.blink_interval) % 2 == 0 else "blue"
        
        for i, setting in enumerate(settings):
            text = settings_font.render(setting, True, "white")
            text_x = surface.get_width()//2 - text.get_width()//2
            
            if i == 0:
                title_font = pg.font.Font(None, 80)
                text = title_font.render(setting, True, "white")
                text_x = surface.get_width()//2 - text.get_width()//2
                surface.blit(text, (text_x, y_offset))
                y_offset += line_spacing + 20
            else:
                surface.blit(text, (text_x, y_offset))
                
                # Draw triangles for SFX and CONTROLLER options
                if i == self.selected_option:
                    triangle_size = 20
                    # Left triangle
                    pg.draw.polygon(surface, blink_color, [
                        (text_x - 40, y_offset + text.get_height()//2),
                        (text_x - 40 - triangle_size, y_offset + text.get_height()//2 - triangle_size//2),
                        (text_x - 40 - triangle_size, y_offset + text.get_height()//2 + triangle_size//2)
                    ])
                    # Right triangle
                    pg.draw.polygon(surface, blink_color, [
                        (text_x + text.get_width() + 40, y_offset + text.get_height()//2),
                        (text_x + text.get_width() + 40 + triangle_size, y_offset + text.get_height()//2 - triangle_size//2),
                        (text_x + text.get_width() + 40 + triangle_size, y_offset + text.get_height()//2 + triangle_size//2)
                    ])
                
                y_offset += line_spacing

        # Add instructions for navigation
        instructions_font = pg.font.Font(None, 30)
        instructions = instructions_font.render("Use Up/Down to navigate", True, "white")
        surface.blit(instructions, (surface.get_width()//2 - instructions.get_width()//2, y_offset + 20))
    def draw_setting_menu(self, window):
        table_surface = pg.Surface((WIDTH * 0.5, HEIGHT * 0.6))
        table_surface.fill((0, 0, 0))
        pg.draw.rect(table_surface, (255, 255, 255), table_surface.get_rect(), 10)
        
        self.draw_setting(table_surface, 60)
        
        window.blit(self.background, (0, 0))
        window.blit(table_surface, (WIDTH//2 - table_surface.get_width()//2, HEIGHT//2 - table_surface.get_height()//2))
    def handle_settings_navigation(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.selected_option = max(1, self.selected_option - 1)
                elif event.key == pg.K_DOWN:
                    self.selected_option = min(2, self.selected_option + 1)
                # Left and Right key handling can be implemented later if needed
