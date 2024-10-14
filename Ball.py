import pygame as pg
import numpy as np

defaut_color = "white"

class Ball:

    def __init__(self,ball_x,ball_y):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_position = np.array([ball_x,ball_y],dtype= np.float64)
        self.ball_velocity = np.array([0,0],dtype= np.float64)
        self.color = defaut_color
    def Draw(self,window):
        pg.draw.circle(window,self.color,(50,50),30)

    




