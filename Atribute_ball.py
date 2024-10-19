import Ball
import pygame as pg
import numpy as np
import random
class Atribute_ball(Ball.Ball):
    speed = 'red'
    size = 'blue'
    color = 'green'
    
    def __init__(self, ball_x, ball_y, window):
        super().__init__(ball_x, ball_y, window)
        self.Gravity = 0.15
        self.Atribute_list = [self.speed,self.size,self.color]
        self.color = random.choice(self.Atribute_list)
        
        self.ball_velocity = np.array([0,2],dtype= np.float64)
        
        
    def Atribute_function(self):
        element = random.choice(self.Atribute_list)
        print(element)
        if element == self.speed:
            self.color = 'red'
        elif element == self.size:
            self.color = "blue"
        elif element == self.color:
            self.color = 'white'
            
    def Updateposition(self,HEIGHT,WIDTH):
        self.Reset(HEIGHT,WIDTH)
        self.ball_position = self.ball_position + self.ball_velocity
        self.ball_velocity[1] += self.Gravity
    def Reset(self,HEIGHT,WIDTH):
        if self.ball_position[1] > HEIGHT + 10:
            self.Atribute_function()    
            self.ball_position = [WIDTH//2,0]
            self.ball_velocity[1] = 2
