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
    try:
        with open(file_config, "r") as file:
            for line in file:
                if line.startswith("key_player_1="):
                    keys = line.strip().split("=")[1].split(",")
                    key_player_1[0] = int(keys[0])
                    key_player_1[1] = int(keys[1])
                elif line.startswith("key_player_2="):
                    keys = line.strip().split("=")[1].split(",")
                    key_player_2[0] = int(keys[0])
                    key_player_2[1] = int(keys[1])
    except FileNotFoundError:
        reset_key()
        save_config()

def save_config():
    print("Saving config...")  # Debug print
    with open(file_config, "w") as file:
        file.write(f"key_player_1={key_player_1[0]},{key_player_1[1]}\n")
        file.write(f"key_player_2={key_player_2[0]},{key_player_2[1]}\n")
    print("Config saved")  # Debug print

def set_key(player, keys):
    global key_player_1, key_player_2
    if player == 1:
        key_player_1 = keys
    else:
        key_player_2 = keys
    

def get_key_player_1():
    return key_player_1
def get_key_player_2():
    return key_player_2

def reset_key():
    print("Resetting keys...")  # Debug print
    global key_player_1, key_player_2
    key_player_1 = [defaut_up_player_1, defaut_down_player_1]
    key_player_2 = [defaut_up_player_2, defaut_down_player_2]
    save_config()
    print("Keys reset")  # Debug print
    


