import pygame as pg
import numpy as np
import random

defaut_color = "yellow"

class Ball:

    def __init__(self,ball_x,ball_y,window):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_position = np.array([ball_x,ball_y],dtype= np.float64)
        self.ball_velocity = np.array([6,6],dtype= np.float64)
        self.color = defaut_color
        self.ball = pg.draw.circle(window,defaut_color,self.ball_position,10)

    def Display(self,window):
        self.ball = pg.draw.circle(window,defaut_color,self.ball_position,10)

    

    def Hit(self):
        self.ball_velocity[0] *= -1
        if self.ball_velocity[0] > 0:
            self.ball_velocity += [1,0]
        else:
            self.ball_velocity += [-1,0]
        pass
    def Updateposition(self,HEIGHT):
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
        if self.ball_position[0] <= 20 and self.ball.colliderect(bar):  # Left boundary (bar width + ball radius)
            self.ball_position[0] = 20
            self.Hit()
        elif self.ball_position[0] >= WIDTH - 20 and self.ball.colliderect(bar2):  # Right boundary
            self.ball_position[0] = WIDTH - 20
            self.Hit()
        

    




