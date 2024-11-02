
import pygame as pg
from source_code import Sound_config
WIDTH = 1400

class logic_score:
    def __init__(self):
        self.playera_points = 0
        self.playerb_points = 0
        self.score_a = []
        self.score_b = []
        self.set_score = ["0", "15", "30", "40","AD"]
        self.game_score_a = "0"
        self.game_score_b = "0"
        self.set1_score_a = 0
        self.set1_score_b = 0
        self.tb_score_a = 0
        self.tb_score_b = 0
     
    def update_playerapoints(self):
        self.playera_points += 1

    def update_playerbpoints(self):    
        self.playerb_points += 1
    
    def reset_game_points(self): 
        self.playera_points = 0 
        self.playerb_points = 0

    def game_scoreb(self):
        if self.playerb_points == 0 and ( self.set1_score_a != 6  or self.set1_score_b != 6)  :
            self.score_b.clear()
            self.score_b.append(self.set_score[0])
            self.game_score_b = str(self.score_b[0])
        elif self.playerb_points == 1 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_b.clear()
            self.score_b.append(self.set_score[1])
            self.game_score_b = str(self.score_b[0])
        elif self.playerb_points == 2 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_b.clear()
            self.score_b.append(self.set_score[2])
            self.game_score_b = str(self.score_b[0])
        elif self.playerb_points == 3 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_b.clear()
            self.score_b.append(self.set_score[3])
            self.game_score_b = str(self.score_b[0])
    
    def game_scorea(self):
        if self.playera_points == 0 and ( self.set1_score_a != 6  or self.set1_score_b != 6)  :
            self.score_a.clear()
            self.score_a.append(self.set_score[0])
            self.game_score_a = str(self.score_a[0])
        elif self.playera_points == 1 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_a.clear()
            self.score_a.append(self.set_score[1])
            self.game_score_a = str(self.score_a[0])
        elif self.playera_points == 2 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_a.clear()
            self.score_a.append(self.set_score[2])
            self.game_score_a = str(self.score_a[0])
        elif self.playera_points == 3 and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_a.clear()
            self.score_a.append(self.set_score[3])
            self.game_score_a = str(self.score_a[0])

    def SetScoreb(self):
        if self.playerb_points == 4 and (self.game_score_b == self.game_score_a) and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_b.clear()
            self.score_b.append(self.set_score[4])
            self.game_score_b = str(self.score_b[0])
            Sound_config.gameAD.play()
        elif self.playerb_points == self.playera_points == 4:
            self.score_b.clear()
            self.score_b.append(self.set_score[3])
            self.game_score_b = str(self.score_b[0])
            self.score_a.clear()
            self.score_a.append(self.set_score[3])
            self.game_score_a = str(self.score_a[0])
            self.playera_points = 3
            self.playerb_points = 3
        elif (self.playerb_points == 4 or self.playerb_points >= 5)  and (self.playerb_points - self.playera_points >=1) and (self.set1_score_b <= 7) : 
            if self.set1_score_b < 6 and self.set1_score_b >= 5 and self.set1_score_a <= 6 and self.set1_score_a > 4:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_b +=1
                Sound_config.gameEnd.play()
                if self.set1_score_b == 6 and self.set1_score_a == 6:
                    self.playerb_points = 3
                    self.playera_points = 3

            elif self.set1_score_b < 6 and self.set1_score_a <= 5 and self.set1_score_a !=7 and self.set1_score_a!= 6:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_b +=1
                Sound_config.gameEnd.play()

            elif self.set1_score_b >= 6 and self.set1_score_a == 5 and self.set1_score_b != 7:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_b +=1
                Sound_config.gameEnd.play()

            elif (self.set1_score_a == 6 and self.set1_score_b == 6):
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.playerb_points = 3
                self.playera_points = 3
                self.tb_score_b += 1
                Sound_config.gameEnd.play()
                if (self.tb_score_b >= 7 )and (self.tb_score_b - self.tb_score_a >= 2):
                    self.set1_score_b +=1
                    self.reset_game_points()
                    Sound_config.gameEnd.play()
    
    def SetScorea(self):
        if self.playera_points == 4 and (self.game_score_b == self.game_score_a) and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_a.clear()
            self.score_a.append(self.set_score[4])
            self.game_score_a = str(self.score_a[0])
            Sound_config.gameAD.play()
        elif self.playerb_points == self.playera_points == 4:
            self.score_b.clear()
            self.score_b.append(self.set_score[3])
            self.game_score_b = str(self.score_b[0])
            self.score_a.clear()
            self.score_a.append(self.set_score[3])
            self.game_score_a = str(self.score_a[0])
            self.playera_points = 3
            self.playerb_points = 3
        elif (self.playera_points == 4 or self.playera_points >= 5)  and (self.playera_points - self.playerb_points >=1) and (self.set1_score_a <= 7) : 
            if self.set1_score_a < 6 and self.set1_score_a >= 5 and self.set1_score_b <= 6 and self.set1_score_b > 4:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_a +=1
                Sound_config.gameEnd.play()
                if self.set1_score_b == 6 and self.set1_score_a == 6:
                    self.playerb_points = 3
                    self.playera_points = 3

            elif self.set1_score_a < 6 and self.set1_score_b <= 5 and self.set1_score_b !=7 and self.set1_score_b!= 6:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_a +=1
                Sound_config.gameEnd.play()

            elif self.set1_score_a >= 6 and self.set1_score_b == 5 and self.set1_score_a != 7:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_a +=1
                Sound_config.gameEnd.play()

            elif (self.set1_score_a == 6 and self.set1_score_b == 6):
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.playerb_points = 3
                self.playera_points = 3
                self.tb_score_a += 1
                Sound_config.gameEnd.play()
                if (self.tb_score_a >= 7 )and (self.tb_score_a - self.tb_score_b >= 2):
                    self.set1_score_a +=1
                    self.reset_game_points()
                    Sound_config.gameEnd.play()

    def Sound(self):
        if(self.playera_points == self.playerb_points == 1):
            Sound_config.game15_15.play()
        elif(self.playera_points == 1 and self.playerb_points == 2) or (self.playera_points == 2 and self.playerb_points == 1):
            Sound_config.game15_30.play()
        elif(self.playera_points == 1 and self.playerb_points == 3) or (self.playera_points == 3 and self.playerb_points == 1):
            Sound_config.game15_40.play()
        elif(self.playera_points == self.playerb_points == 2):
            Sound_config.game30_30.play()
        elif(self.playera_points == 3 and self.playerb_points == 2) or (self.playera_points == 2 and self.playerb_points == 3):
            Sound_config.game40_30.play()
        elif(self.playera_points == self.playerb_points == 3):
            Sound_config.game40_40.play()
        elif(self.playera_points == 0 and self.playerb_points == 1) or (self.playera_points == 1 and self.playerb_points == 0):
            Sound_config.game0_15.play()
        elif(self.playera_points == 0 and self.playerb_points == 2) or (self.playera_points == 2 and self.playerb_points == 0):
            Sound_config.game0_30.play()
        elif(self.playera_points == 0 and self.playerb_points == 3) or (self.playera_points == 3 and self.playerb_points == 0):
            Sound_config.game0_40.play()    
    def gameover(self):
        if self.set1_score_a >= 6 and (self.set1_score_a - self.set1_score_b >=1) and self.set1_score_b <= 4:
            return True
        elif self.set1_score_b >= 6 and (self.set1_score_b - self.set1_score_a >=1) and self.set1_score_a <= 4:           
            return True
        elif self.set1_score_a == 7 and (self.set1_score_a - self.set1_score_b >=1) and self.set1_score_b >= 5:
            return True
        elif self.set1_score_b == 7 and (self.set1_score_b - self.set1_score_a >=1) and self.set1_score_a >= 5:
            return True
    

