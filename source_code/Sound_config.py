from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg

pg.mixer.init()

cheer = pg.mixer.Sound('sound/Cheering.wav')  
ohh = pg.mixer.Sound('sound/ohh.wav')
tick_sound = pg.mixer.Sound('sound/tick_sound.mp3')
chosed_sound = pg.mixer.Sound('sound/chosed_sound.mp3')
bounce = pg.mixer.Sound('sound/bouncingball.wav')    
left = pg.mixer.Sound('sound/leftplayer.wav')         
right = pg.mixer.Sound('sound/rightplayer.wav')

game15_15 = pg.mixer.Sound('sound/15_15.mp3')
game15_30 = pg.mixer.Sound('sound/15_30.mp3')
game15_40 = pg.mixer.Sound('sound/15_40.mp3')
game30_30 = pg.mixer.Sound('sound/30_30.mp3')
game40_30 = pg.mixer.Sound('sound/40_30.mp3')
game40_40 = pg.mixer.Sound('sound/40_40.mp3')
gameAD = pg.mixer.Sound('sound/AD.mp3')
gameEnd = pg.mixer.Sound('sound/Game_end.mp3')
game0_15 = pg.mixer.Sound('sound/love_15_new.mp3')
game0_30 = pg.mixer.Sound('sound/love_30.mp3')
game0_40 = pg.mixer.Sound('sound/love_40.mp3')




default_volume = 1
Master_volume = default_volume  
Cheering_volume = default_volume
Ball_volume = default_volume
SFX_volume = default_volume

def SetMaster_volume(volume):
    global Master_volume
    Master_volume = volume
    # Update all sound volumes while preserving their individual levels
    update_all_volumes()

def SetCheering_volume(volume):
    global Cheering_volume
    Cheering_volume = volume
    # Only update cheering sounds
    update_cheering_volumes()

def SetBall_volume(volume):
    global Ball_volume
    Ball_volume = volume
    # Only update ball sounds
    update_ball_volumes()

def SetSFX_volume(volume):
    global SFX_volume
    SFX_volume = volume
    # Only update SFX sounds
    update_sfx_volumes()

# New helper functions to update volumes
def update_all_volumes():
    update_cheering_volumes()
    update_ball_volumes()
    update_sfx_volumes()

def update_cheering_volumes():
    cheer.set_volume(Master_volume * Cheering_volume)
    ohh.set_volume(Master_volume * Cheering_volume)
    game0_15.set_volume(Master_volume * Cheering_volume)
    game0_30.set_volume(Master_volume * Cheering_volume)
    game0_40.set_volume(Master_volume * Cheering_volume)
    game15_15.set_volume(Master_volume * Cheering_volume)
    game15_30.set_volume(Master_volume * Cheering_volume)
    game15_40.set_volume(Master_volume * Cheering_volume)
    game30_30.set_volume(Master_volume * Cheering_volume)
    game40_30.set_volume(Master_volume * Cheering_volume)
    game40_40.set_volume(Master_volume * Cheering_volume)
    gameAD.set_volume(Master_volume * Cheering_volume)
    gameEnd.set_volume(Master_volume * Cheering_volume)


def update_ball_volumes():
    bounce.set_volume(Master_volume * Ball_volume)
    left.set_volume(Master_volume * Ball_volume)
    right.set_volume(Master_volume * Ball_volume)

def update_sfx_volumes():
    tick_sound.set_volume(Master_volume * SFX_volume)
    chosed_sound.set_volume(Master_volume * SFX_volume)

def load_sound_config():
    global Master_volume
    global Cheering_volume
    global Ball_volume
    global SFX_volume
    try:
        with open('config/Sound_config.txt','r') as file:
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
    with open('config/Sound_config.txt','w') as file:
        file.write(f"Master_volume = {Master_volume}\n")
        file.write(f"Cheering_volume = {Cheering_volume}\n")
        file.write(f"Ball_volume = {Ball_volume}\n")
        file.write(f"SFX_volume = {SFX_volume}\n")

def Reset_sound_config():
    global Master_volume, Cheering_volume, Ball_volume, SFX_volume
    Master_volume = default_volume
    Cheering_volume = default_volume
    Ball_volume = default_volume
    SFX_volume = default_volume
    # Update all volumes after reset
    update_all_volumes()


