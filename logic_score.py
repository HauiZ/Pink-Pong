import GUI
import pygame as pg
import Sound_config
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
        self.font2 = pg.font.Font("fonts/Antonio-Bold.ttf",20)
        self.font3 = pg.font.Font("fonts/Antonio-Bold.ttf",14)
     
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
        elif self.playerb_points == 4 and (self.game_score_b == self.game_score_a) and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_b.clear()
            self.score_b.append(self.set_score[4])
            self.game_score_b = str(self.score_b[0])
        elif self.playerb_points == self.playera_points == 4:
            self.score_b.clear()
            self.score_b.append(self.set_score[3])
            self.game_score_b = str(self.score_b[0])
            self.score_a.clear()
            self.score_a.append(self.set_score[3])
            self.game_score_a = str(self.score_a[0])
            self.playera_points = 3
            self.playerb_points = 3
    
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
        elif self.playera_points == 4 and (self.game_score_b == self.game_score_a) and ( self.set1_score_a != 6  or self.set1_score_b != 6 )  :
            self.score_a.clear()
            self.score_a.append(self.set_score[4])
            self.game_score_a = str(self.score_a[0])
        elif self.playerb_points == self.playera_points == 4:
            self.score_b.clear()
            self.score_b.append(self.set_score[3])
            self.game_score_b = str(self.score_b[0])
            self.score_a.clear()
            self.score_a.append(self.set_score[3])
            self.game_score_a = str(self.score_a[0])
            self.playera_points = 3
            self.playerb_points = 3

    def SetScoreb(self):
        if (self.playerb_points == 4 or self.playerb_points >= 5)  and (self.playerb_points - self.playera_points >=1) and (self.set1_score_b <= 7) : 
            if self.set1_score_b < 6 and self.set1_score_b >= 5 and self.set1_score_a <= 6 and self.set1_score_a > 4:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_b +=1
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

            elif self.set1_score_b >= 6 and self.set1_score_a == 5 and self.set1_score_b != 7:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_b +=1

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
                if (self.tb_score_b >= 7 )and (self.tb_score_b - self.tb_score_a >= 2):
                    self.set1_score_b +=1
                    self.reset_game_points()
    
    def SetScorea(self):
        if (self.playera_points == 4 or self.playera_points >= 5)  and (self.playera_points - self.playerb_points >=1) and (self.set1_score_a <= 7) : 
            if self.set1_score_a < 6 and self.set1_score_a >= 5 and self.set1_score_b <= 6 and self.set1_score_b > 4:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_a +=1
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

            elif self.set1_score_a >= 6 and self.set1_score_b == 5 and self.set1_score_a != 7:
                self.score_b.clear()
                self.score_b.append(self.set_score[0])
                self.game_score_b = str(self.score_b[0])
                self.score_a.clear()
                self.score_a.append(self.set_score[0])
                self.game_score_a = str(self.score_a[0])
                self.reset_game_points()
                self.set1_score_a +=1

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
                if (self.tb_score_a >= 7 )and (self.tb_score_a - self.tb_score_b >= 2):
                    self.set1_score_a +=1
                    self.reset_game_points()

    def gameover(self):
        if self.set1_score_a >= 6 and (self.set1_score_a - self.set1_score_b >=1) and self.set1_score_b <= 4:
            return True
        elif self.set1_score_b >= 6 and (self.set1_score_b - self.set1_score_a >=1) and self.set1_score_a <= 4:           
            return True
        elif self.set1_score_a == 7 and (self.set1_score_a - self.set1_score_b >=1) and self.set1_score_b >= 5:
            return True
        elif self.set1_score_b == 7 and (self.set1_score_b - self.set1_score_a >=1) and self.set1_score_a >= 5:
            return True
    def score_board(self,window):
        # Tạo bảng Game Over
        table_surface = pg.Surface((200, 60), pg.SRCALPHA)  # Nền trong suốt
        pg.draw.rect(table_surface, (0, 0, 0, 200), table_surface.get_rect(), border_radius=20)
        score_display1 = self.font3.render(f"Game", True, "white")
        score_display13 = self.font3.render(f"Player A", True, "white")
        score_display14 = self.font3.render(f"Player B", True, "white")
        score_display2 = self.font2.render(f"{self.game_score_a}", True, "red")
        score_display3 = self.font2.render(f"{self.game_score_b}", True, "red")
        score_display4 = self.font3.render(f"Set", True, "white")
        score_display5 = self.font2.render(f"{self.set1_score_a}", True, "red")
        score_display6 = self.font2.render(f"{self.set1_score_b}", True, "red")
        score_display15 = self.font3.render(f"Tie-break", True, "white")
        score_display16 = self.font2.render(f"{self.tb_score_a}", True, "red")
        score_display17 = self.font2.render(f"{self.tb_score_b}", True, "red")

        #Game score board
        table_surface.blit(score_display1, (55, 0))
        table_surface.blit(score_display2, (65, 15))
        table_surface.blit(score_display3, (65, 35))
        table_surface.blit(score_display13, (10, 19))
        table_surface.blit(score_display14, (10, 38))

        #Set score board
        table_surface.blit(score_display4, (100, 0))
        table_surface.blit(score_display5, (107, 15))
        table_surface.blit(score_display6, (107, 35))

        #Tie-break score board
        table_surface.blit(score_display15, (130, 0))
        table_surface.blit(score_display16, (155, 15))
        table_surface.blit(score_display17, (155, 35))
        window.blit(table_surface, ((WIDTH//2 - table_surface.get_width()//2)-5, 0))

