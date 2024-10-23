from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
import numpy as np
import random
import threading
import time

defaut_color = "yellow"
pg.mixer.init()
bounce = pg.mixer.Sound('bouncingball.wav')     #Thiết lập âm thanh nảy của bóng
left = pg.mixer.Sound('leftplayer.wav')         #Thiết lập âm thanh của người chơi bên trái
right = pg.mixer.Sound('rightplayer.wav')       #Thiết lập âm thanh của người chơi bên phải

class Ball:
    ball_radius = 10
    def __init__(self,ball_x,ball_y,window):
        self.lock = threading.Lock()
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_position = np.array([ball_x,ball_y],dtype= np.float64)
        self.ball_velocity = np.array([6,6],dtype= np.float64)
        self.color = "yellow"
        self.ball = pg.draw.circle(window,self.color,self.ball_position,self.ball_radius)

    def Display(self,window):
        self.ball = pg.draw.circle(window,self.color,self.ball_position,self.ball_radius)

    

    def Hit(self):
        self.ball_velocity[0] *= -1
        if self.ball_velocity[0] > 0:
            self.ball_velocity += [0,0]
        else:
            self.ball_velocity += [-0,0]
        pass
    def Updateposition(self, HEIGHT, ball_Atribute, paddle_a, paddle_b):
        atribute_speed = threading.Thread(target=self.run_check_Hit_Atribute_speed, args=(ball_Atribute,)) 
        atribute_paddle_speed = threading.Thread(target=self.run_check_Hit_Atribute_paddle_speed, args=(ball_Atribute, paddle_a, paddle_b,))
        atribute_size = threading.Thread(target=self.run_check_Hit_Atribute_size, args=(ball_Atribute,))
        atribute_speed.start()
        atribute_paddle_speed.start()
        atribute_size.start()
        if self.ball_position[1] <= 0 +15 or self.ball_position[1] >= HEIGHT - 15:
            self.ball_velocity[1] *= -1
            bounce.play() 
        self.ball_position = self.ball_position + self.ball_velocity      #lệnh chạy âm thanh
        pass

    def Reset(self, x, y):
        self.ball_position = np.array([x, y], dtype=np.float64)
        self.ball_velocity = np.array([(abs(self.ball_velocity[0])/self.ball_velocity[0])*6,6],dtype= np.float64)
        ran = random.randint(-1, 1)
        while ran == 0:
            ran = random.randint(-1, 1)
        self.ball_velocity[1] *= ran


    def check_boundary(self, WIDTH, HEIGHT,bar,bar2):
        # Check left and right boundaries
        if self.ball_position[0] <= 20 and (self.ball_position[1] >= bar.rect.y and self.ball_position[1] <= bar.rect.y + bar.height):  # Left boundary (bar width + ball radius)
            self.ball_position[0] = 20
            left.play()
            self.Hit()
        elif self.ball_position[0] >= WIDTH - 20 and (self.ball_position[1] >= bar2.rect.y and self.ball_position[1] <= bar2.rect.y + bar2.height):  # Right boundary
            self.ball_position[0] = WIDTH - 20
            right.play()
            self.Hit()
    def check_Hit_Atribute_speed(self,ball_Atribute):
        if self.ball.colliderect(ball_Atribute.ball) and ball_Atribute.color == "red":
            return True
    def run_check_Hit_Atribute_speed(self,ball_Atribute):
        if self.check_Hit_Atribute_speed(ball_Atribute) and ball_Atribute.hit == False:
            print("Hit1")
            ball_Atribute.hit = True
            self.ball_velocity[0] += 10 * (abs(self.ball_velocity[0]) / self.ball_velocity[0])
            self.ball_velocity[1] += 10 * (abs(self.ball_velocity[1]) / self.ball_velocity[1])
            time.sleep(5)
            self.ball_velocity[0] -= 10 * (abs(self.ball_velocity[0]) / self.ball_velocity[0])
            self.ball_velocity[1] -= 10 * (abs(self.ball_velocity[1]) / self.ball_velocity[1])

        
    def check_Hit_Atribute_paddle_speed(self,ball_Atribute):
        if self.ball.colliderect(ball_Atribute.ball) and ball_Atribute.color == "blue":
            return True
    def run_check_Hit_Atribute_paddle_speed(self,ball_Atribute, paddle_a, paddle_b):
        if self.check_Hit_Atribute_paddle_speed(ball_Atribute) and ball_Atribute.hit == False:
            print("Hit2")
            ball_Atribute.hit = True
            if self.ball_velocity[0] > 0:
                paddle_a.speed += 10
                time.sleep(5)
                paddle_a.speed -= 10
            else:
                paddle_b.speed += 10
                time.sleep(5)
                paddle_b.speed -= 10

    def check_Hit_Atribute_size(self,ball_Atribute):
        if self.ball.colliderect(ball_Atribute.ball) and ball_Atribute.color == "green":
            return True
    def run_check_Hit_Atribute_size(self,ball_Atribute):
        if self.check_Hit_Atribute_size(ball_Atribute) and ball_Atribute.hit == False:
            print("Hit3")
            ball_Atribute.hit = True
            self.ball_radius *= 2
            time.sleep(5)
            self.ball_radius /= 2

        
        

    




