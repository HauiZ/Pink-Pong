from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg

pg.mixer.init()

cheer = pg.mixer.Sound('sound/Cheering.wav')  #Thiết lập âm thanh cổ động viên 
ohh = pg.mixer.Sound('sound/ohh.wav')
tick_sound = pg.mixer.Sound('sound/tick_sound.mp3')
chosed_sound = pg.mixer.Sound('sound/chosed_sound.mp3')
bounce = pg.mixer.Sound('sound/bouncingball.wav')     #Thiết lập âm thanh nảy của bóng
left = pg.mixer.Sound('sound/leftplayer.wav')         #Thiết lập âm thanh của người chơi bên trái
right = pg.mixer.Sound('sound/rightplayer.wav')

default_volume = 1
Master_volume = default_volume  
Cheering_volume = default_volume
Ball_volume = default_volume
SFX_volume = default_volume

def SetMaster_volume(volume):
    global Master_volume
    Master_volume = volume
def SetCheering_volume(volume):
    global Cheering_volume
    Cheering_volume = volume
def SetBall_volume(volume):
    global Ball_volume
    Ball_volume = volume
def SetSFX_volume(volume):
    global SFX_volume
    SFX_volume = volume

def load_sound_config():
    global Master_volume
    global Cheering_volume
    global Ball_volume
    global SFX_volume
    try:
        with open('Sound_config.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                key,value = line.split('=')
                if key == 'Master_volume':
                    Master_volume = float(value)
                elif key == 'Cheering_volume':
                    Cheering_volume = float(value)
                elif key == 'Ball_volume':
                    Ball_volume = float(value)
                elif key == 'SFX_volume':
                    SFX_volume = float(value)
    except (FileNotFoundError, ValueError, IndexError):
        Reset_sound_config()

def save_sound_config():
    with open('Sound_config.txt','w') as file:
        file.write(f"Master_volume = {Master_volume}\n")
        file.write(f"Cheering_volume = {Cheering_volume}\n")
        file.write(f"Ball_volume = {Ball_volume}\n")
        file.write(f"SFX_volume = {SFX_volume}\n")

def Reset_sound_config():
    global Master_volume
    global Cheering_volume
    global Ball_volume
    global SFX_volume
    Master_volume = default_volume
    Cheering_volume = default_volume
    Ball_volume = default_volume
    SFX_volume = default_volume


