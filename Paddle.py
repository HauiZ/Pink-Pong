import pygame
import numpy as np

defaut_color = "white"

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.paddle_position = np.array([x,y],dtype=np.float64)
        self.color = defaut_color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 10
        self.velocity = 1

    def Draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        
    def Move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < 700:
            self.rect.y += self.speed
        self.y = self.rect.y

    def Move1(self):
        self.Move(pygame.K_w, pygame.K_s)

    def Move2(self):
        self.Move(pygame.K_UP, pygame.K_DOWN)

    def Reset(self,x,y):
        self.paddle_position = [x,y]
        self.rect = pygame.Rect( self.paddle_position[0], self.paddle_position[1], self.width, self.height)
    
    def paddble_b_up(self):
        if self.rect.top> 0:
            self.rect.y -= 8
    def paddble_b_down(self):
        if self.rect.bottom < 700 :
            self.rect.y += 8