import pygame as pg
import numpy as np
import random

defaut_color = "yellow"

class Ball:
    ball_radius = 10
    def __init__(self,ball_x,ball_y,window):
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
            self.ball_velocity += [1,0]
        else:
            self.ball_velocity += [-1,0]
        pass
    def Updateposition(self,HEIGHT,ball_Atribute):
        if self.check_Hit_Atribute(ball_Atribute):
            self.ball_velocity *= 2
        self.ball_position = self.ball_position + self.ball_velocity

        if self.ball_position[1] <= 0 +15 or self.ball_position[1] >= HEIGHT - 15:
            self.ball_velocity[1] *= -1
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
        if self.ball_position[0] <= 20 and (self.ball_position[1] >= bar.y and self.ball_position[1] <= bar.y + bar.height):  # Left boundary (bar width + ball radius)
            self.ball_position[0] = 20
            self.Hit()
        elif self.ball_position[0] >= WIDTH - 20 and (self.ball_position[1] >= bar2.y and self.ball_position[1] <= bar2.y + bar2.height):  # Right boundary
            self.ball_position[0] = WIDTH - 20
            self.Hit()
    def check_Hit_Atribute(self,ball_Atribute):
        if self.ball.colliderect(ball_Atribute.ball):
            return True
            # ball_Atribute.Atribute_function(self.ball_velocity)
        
        

    




