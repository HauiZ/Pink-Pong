import pygame as pg
import numpy as np

defaut_color = "white"

class Ball:

    def __init__(self,ball_x,ball_y,window):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_position = np.array([ball_x,ball_y],dtype= np.float64)
        self.ball_velocity = np.array([-3,-7],dtype= np.float64)
        self.color = defaut_color
        self.ball = pg.draw.circle(window,defaut_color,self.ball_position,10)

    def Display(self,window):
        self.ball = pg.draw.circle(window,defaut_color,self.ball_position,10)

    

    def Hit(self):
        self.ball_velocity[0] *= -1
        pass
    def Updateposition(self,HEIGHT):
        self.ball_position = self.ball_position + self.ball_velocity
        if self.ball_position[1] <= 0 +15 or self.ball_position[1] >= HEIGHT - 15:
            self.ball_velocity[1] *= -1

        pass

    




