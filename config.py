import pygame
import sys
# key defaults
defaut_up_player_1 = pygame.K_w # player 1 (value 119)
defaut_down_player_1 = pygame.K_s # value 115
defaut_up_player_2 = pygame.K_UP # player 2 (value 1073741906)
defaut_down_player_2 = pygame.K_DOWN # (value 1073741905)


file_config = "config.txt"
# with open(file_config, "w") as file:
#     file.write("key_player_1=119,220\n")
#     file.write("key_player_2=1073741906\n")

key_player_1= [defaut_up_player_1,defaut_down_player_1] # player 1
key_player_2= [defaut_up_player_2,defaut_down_player_2]# player 2


def load_config():
    pass
def save_config():
    pass
def set_key(player,key):
    pass
def get_key_player_1():
    return key_player_1
def get_key_player_2():
    return key_player_2

def reset_key():
    key_player_1= [defaut_up_player_1,defaut_down_player_1] # player 1
    key_player_2= [defaut_up_player_2,defaut_down_player_2]# player 2
    


