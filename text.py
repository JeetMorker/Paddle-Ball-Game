#Jeet Morker
#Jm5265
#This file creates the text class which is used for the score and the ending screen text

from drawable import Drawable
import pygame


class Text(Drawable):
    #Each text needs a message string and a font
    def __init__(self, message="Pygame", x=0, y=0, color=(0,0,0), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)
        
    #Creates the text on a certain location    
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLoc())
    
    #Doesn't have an actual border that can be intersected
    def get_rect(self):
        return self.__surface.get_rect()
    
    #Used to change message such as score
    def setMessage(self, message):
        self.__message = message