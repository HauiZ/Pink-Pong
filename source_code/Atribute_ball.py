
import pygame as pg
import numpy as np
import random
class Atribute_ball():
    speed = 'red'
    paddle_speed = 'blue'
    size_ball = 'green'
    paddle_size = 'orange'
    
    def __init__(self, ball_x, ball_y, window):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_position = np.array([ball_x,ball_y],dtype= np.float64)
        self.Gravity = 0.01
        self.Atribute_list = [self.speed,self.paddle_speed,self.size_ball,self.paddle_size]
        self.color = random.choice(self.Atribute_list)
        self.element = random.choice(self.Atribute_list)
        self.atribute = str(self.element)
        self.ball_radius = 50
        self.ball_velocity = np.array([0,0.1],dtype= np.float64)
        self.ball = pg.draw.circle(window,self.color,self.ball_position,self.ball_radius)
        self.active = True
        self.hit = False

    def Display(self,window):
        self.ball = pg.draw.circle(window,self.color,self.ball_position,self.ball_radius)

    def Updateposition(self,HEIGHT,WIDTH):
        self.Reset(HEIGHT,WIDTH)
        self.ball_position = self.ball_position + self.ball_velocity
        self.ball_velocity[1] += self.Gravity
    def Reset(self,HEIGHT,WIDTH):
        if self.ball_position[1] > HEIGHT + 10:
            self.active = False
            self.hit = False
           
