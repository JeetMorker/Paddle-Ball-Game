#Jeet Morker
#Jm5265
#This file creates the paddle class which is the object that user will be able to move around to hit the ball

from drawable import Drawable
import pygame

class Paddle(Drawable):
    #Paddle location changes based on mouse movement but its height and width stay the same
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height
    
    #Created the actual object on the screen
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.rect(surface, self.__color, self.get_rect())
     
    #The border moves with the mouse
    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, screenHeight - 20 - (self.__height), self.__width, self.__height)