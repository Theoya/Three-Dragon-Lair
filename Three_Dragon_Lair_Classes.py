import pygame, sys, random
from pygame.locals import *

class entity:

    def __init__(self, pos, image):
        self.pos = pos
        self.image = image


    def getImage():
        return image
    def getPos():
        return pos
    def setImage(new):
        self.image = new
    def setPos(new):
        self.pos = new
        
    

    




class snake(entity):

    
    def __init__(self, pos, image):
        super().__init__(pos, image)
        
    
        
    def snakeLog(self, player):
        
        if (self.pos[0]==player.pos[0] and self.pos[1]==player.pos[1]):
            if (player.image != pygame.image.load("winner.png")):
                player.image = self.image
            

        if self.pos[0]<player.pos[0]:
            self.pos[0]+=1
            
        elif self.pos[0]>player.pos[0]:
            self.pos[0]-=1
            
        elif self.pos[1]<player.pos[1]:
            self.pos[1]+=1
            
        elif self.pos[1]>player.pos[1]:
            self.pos[1]-=1
            


        
class player(entity):



    def __init__(self, pos, image):
        super().__init__(pos,image)
        


    
    






        
