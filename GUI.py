import pygame as pg
import numpy as np
import Ball
import Paddle
import random
import Atribute_ball
import threading
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import config  # Add this import at the top of the file

pg.mixer.init()
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
tick_sound = pg.mixer.Sound('sound/tick_sound.mp3')
chosed_sound = pg.mixer.Sound('sound/chosed_sound.mp3')

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
        self.show_controller_panel = False
        self.controller_options = ["Player1_UP", "Player1_DOWN", "Player2_UP", "Player2_DOWN"]
        self.selected_control = 0  # Add this line to track selected control option
        self.is_binding_mode = False  # Add this new state variable
        config.load_config()  # Load config when initializing
        self.notification = None
        self.notification_start_time = 0
        self.notification_duration = 2000  # 2 seconds in milliseconds
        
        

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
        
        for i, setting in enumerate(settings):#draw setting title and option
            text = settings_font.render(setting, True, "white")
            text_x = surface.get_width()//2 - text.get_width()//2
            
            if i == 0: #setting title
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

        # Call controller panel if enabled
        if self.show_controller_panel and self.selected_option == 2:
            self.draw_controller_panel(surface, y_offset)

    def draw_setting_menu(self, window):
        if self.show_controller_panel:
            # Draw only the controller panel
            table_surface = pg.Surface((WIDTH * 0.5, HEIGHT * 0.6))
            table_surface.fill((0, 0, 0))
            pg.draw.rect(table_surface, (255, 255, 255), table_surface.get_rect(), 10)
            
            self.draw_controller_panel(table_surface, 60)
            
            window.blit(self.background, (0, 0))
            window.blit(table_surface, (WIDTH//2 - table_surface.get_width()//2, HEIGHT//2 - table_surface.get_height()//2))
        else:
            # Draw the settings menu
            table_surface = pg.Surface((WIDTH * 0.5, HEIGHT * 0.6))
            table_surface.fill((0, 0, 0))
            pg.draw.rect(table_surface, (255, 255, 255), table_surface.get_rect(), 10)
            
            self.draw_setting(table_surface, 60)
            
            window.blit(self.background, (0, 0))
            window.blit(table_surface, (WIDTH//2 - table_surface.get_width()//2, HEIGHT//2 - table_surface.get_height()//2))

    def handle_settings_navigation(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    if self.show_controller_panel:
                        self.show_controller_panel = False
                        self.is_binding_mode = False  # Reset binding mode when exiting
                        chosed_sound.play()
                    return False
                
                if self.show_controller_panel:
                    # Add navigation for controller panel
                    if not self.is_binding_mode:
                        if event.key == pg.K_UP:
                            self.selected_control = (self.selected_control - 1) % len(self.controller_options)
                            tick_sound.play()
                        elif event.key == pg.K_DOWN:
                            self.selected_control = (self.selected_control + 1) % len(self.controller_options)
                            tick_sound.play()
                    
                    if event.key == pg.K_SPACE:
                        self.is_binding_mode = not self.is_binding_mode
                        chosed_sound.play()
                        return False

                    # Add save/reset shortcuts with notifications
                    elif event.key == pg.K_s and not self.is_binding_mode:
                        config.save_config()
                        self.show_notification("Settings Saved!")
                        chosed_sound.play()
                    elif event.key == pg.K_r and not self.is_binding_mode:
                        config.reset_key()
                        self.show_notification("Settings Reset!")
                        chosed_sound.play()

                    if self.is_binding_mode:
                        if event.key != pg.K_SPACE and event.key != pg.K_m:
                            # Get current key configurations
                            player1_keys = list(config.get_key_player_1())
                            player2_keys = list(config.get_key_player_2())
                            
                            # Check if the key is already used
                            if event.key in player1_keys + player2_keys:
                                # Find and remove the duplicate key
                                if event.key in player1_keys:
                                    idx = player1_keys.index(event.key)
                                    player1_keys[idx] = None
                                    config.set_key(1, player1_keys)
                                if event.key in player2_keys:
                                    idx = player2_keys.index(event.key)
                                    player2_keys[idx] = None
                                    config.set_key(2, player2_keys)
                            
                            # Set the new key
                            if self.selected_control < 2:
                                player1_keys[self.selected_control] = event.key
                                config.set_key(1, player1_keys)
                            else:
                                player2_keys[self.selected_control - 2] = event.key
                                config.set_key(2, player2_keys)
                            
                            self.is_binding_mode = False
                            chosed_sound.play()
                else:
                    # Main settings menu navigation logic
                    if event.key == pg.K_UP:
                        self.selected_option = max(1, self.selected_option - 1)
                        tick_sound.play()
                    elif event.key == pg.K_DOWN:
                        self.selected_option = min(2, self.selected_option + 1)
                        tick_sound.play()
                    elif event.key == pg.K_RETURN:
                        if self.selected_option == 2:  # If CONTROLLER is selected
                            self.show_controller_panel = True
                            chosed_sound.play()
            elif event.type == pg.MOUSEBUTTONDOWN and self.show_controller_panel:
                mouse_x, mouse_y = pg.mouse.get_pos()
                
                # Calculate the exact positions matching draw_controller_panel
                panel_width = WIDTH * 0.5
                panel_height = HEIGHT * 0.6
                panel_x = WIDTH//2 - panel_width//2
                panel_y = HEIGHT//2 - panel_height//2
                
                button_width = 100
                button_height = 40
                button_y = panel_y + 220  # Match the button_y in draw_controller_panel
                
                # Save button (left button)
                save_x = panel_x + panel_width//4 - button_width//2
                if (save_x <= mouse_x <= save_x + button_width and 
                    button_y <= mouse_y <= button_y + button_height):
                    print("Save clicked")  # Debug print
                    config.save_config()
                    chosed_sound.play()
                
                # Reset button (right button)
                reset_x = panel_x + 3*panel_width//4 - button_width//2
                if (reset_x <= mouse_x <= reset_x + button_width and 
                    button_y <= mouse_y <= button_y + button_height):
                    print("Reset clicked")  # Debug print
                    config.reset_key()
                    chosed_sound.play()
        
        return False

    def draw_controller_panel(self, surface, y_offset):
        panel_width = 400  # Increased from 300
        panel_height = 350  # Increased height to accommodate buttons
        panel_x = surface.get_width()//2 - panel_width//2
        panel_y = y_offset - 50

        # Draw panel background
        panel_surface = pg.Surface((panel_width, panel_height))
        panel_surface.fill((40, 40, 40))
        pg.draw.rect(panel_surface, (255, 255, 255), panel_surface.get_rect(), 2)

        # Get current key configurations
        player1_keys = list(config.get_key_player_1())
        player2_keys = list(config.get_key_player_2())
        all_keys = player1_keys + player2_keys

        # Calculate blink color using milliseconds for smoother transitions
        current_time = pg.time.get_ticks()
        blink_color = "red" if (current_time // self.blink_interval) % 2 == 0 else "blue"

        # Draw controller options
        option_spacing = 50
        for i, option in enumerate(self.controller_options):
            # Draw option background
            pg.draw.rect(panel_surface, (80, 80, 80), (20, 20 + i * option_spacing, 250, 35))  # Increased width from 180
            # Draw white rectangle on the right
            key_box = pg.draw.rect(panel_surface, (255, 255, 255), (290, 20 + i * option_spacing, 90, 35))  # Adjusted x position from 220 and increased width from 60

            # Draw triangle only for selected option
            if i == self.selected_control:
                triangle_size = 15
                # Draw single triangle on the left
                pg.draw.polygon(panel_surface, blink_color, [
                    (key_box.left - 20, key_box.centery),
                    (key_box.left - 20 - triangle_size, key_box.centery - triangle_size//2),
                    (key_box.left - 20 - triangle_size, key_box.centery + triangle_size//2)
                ])

            # Draw option text
            option_text = self.settings_font.render(option, True, (255, 255, 255))
            panel_surface.blit(option_text, (30, 25 + i * option_spacing))

            # Draw key name in white box
            key = all_keys[i]
            key_name = pg.key.name(key).upper() if key is not None else ""
            key_text = self.settings_font.render(key_name, True, (0, 0, 0))
            key_rect = key_text.get_rect(center=(335, 37 + i * option_spacing))  # Adjusted x position from 250
            panel_surface.blit(key_text, key_rect)

        # Draw Save and Reset buttons
        button_y = 220  # Position below the controller options
        button_width = 100
        button_height = 40
        button_spacing = 20

        # Save button
        save_button = pg.draw.rect(panel_surface, (0, 150, 0), 
                                 (panel_width//4 - button_width//2, button_y, 
                                  button_width, button_height))
        save_text = self.settings_font.render("Save", True, (255, 255, 255))
        save_text_rect = save_text.get_rect(center=save_button.center)
        panel_surface.blit(save_text, save_text_rect)

        # Reset button
        reset_button = pg.draw.rect(panel_surface, (150, 0, 0), 
                                  (3*panel_width//4 - button_width//2, button_y, 
                                   button_width, button_height))
        reset_text = self.settings_font.render("Reset", True, (255, 255, 255))
        reset_text_rect = reset_text.get_rect(center=reset_button.center)
        panel_surface.blit(reset_text, reset_text_rect)

        # Update the help text to include save/reset instructions
        if self.is_binding_mode:
            binding_text = self.settings_font.render("Press any key to bind...", True, (255, 255, 0))
            panel_surface.blit(binding_text, (panel_width//2 - binding_text.get_width()//2, panel_height - 60))
        else:
            help_text = self.settings_font.render("Press SPACE to bind key", True, (200, 200, 200))
            shortcut_text = self.settings_font.render("Press S to save, R to reset", True, (200, 200, 200))
            panel_surface.blit(help_text, (panel_width//2 - help_text.get_width()//2, panel_height - 80))
            panel_surface.blit(shortcut_text, (panel_width//2 - shortcut_text.get_width()//2, panel_height - 40))

        # Draw notification if active
        if self.notification and current_time - self.notification_start_time < self.notification_duration:
            # Create semi-transparent background for notification
            notification_surface = pg.Surface((300, 40))
            notification_surface.fill((0, 0, 0))
            notification_surface.set_alpha(200)
            
            # Calculate position for centered notification
            notification_x = panel_width//2 - 150  # 300/2 = 150
            notification_y = panel_height - 120
            
            # Draw notification background
            panel_surface.blit(notification_surface, (notification_x, notification_y))
            
            # Draw notification text
            notification_text = self.settings_font.render(self.notification, True, (255, 255, 255))
            text_rect = notification_text.get_rect(center=(panel_width//2, notification_y + 20))
            panel_surface.blit(notification_text, text_rect)
        elif current_time - self.notification_start_time >= self.notification_duration:
            self.notification = None

        surface.blit(panel_surface, (panel_x, panel_y))

    def show_notification(self, message):
        self.notification = message
        self.notification_start_time = pg.time.get_ticks()








