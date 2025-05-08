#Jeet Morker
#Jm5265
#This file creates the drawable class and creates three different classes that derive from it for objects in the game

from abc import ABC
import pygame


class Drawable(ABC):
    #Each object needs a position and color
    def __init__(self, x=0, y=0, color = (0, 0, 0)):
        self.__visible = True
        self.__x = x
        self.__y = y
        self.__color = color
        
    #Getters and setters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    #All derived classes will use draw and get_rect
    def draw(self, surface):
        pass

    def get_rect(self):
        pass
    
    def getLoc(self):
        return (self.__x, self.__y)
    
    #Visibilty determines if the object is visible in the game state
    def isVisible(self):
        return self.__visible

    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False
            
    #Checks the border of two visible objects to see if they have intersected
    def intersects(self, other):
        if self.isVisible() and other.isVisible():
            rect1 = self.get_rect()
            rect2 = other.get_rect()
            if (rect1.x <= rect2.x + rect2.width) and \
               (rect1.x + rect1.width >= rect2.x) and \
               (rect1.y <= rect2.y + rect2.height) and \
               (rect1.height + rect1.y >= rect2.y):
                return True
        return False

#Triangle object that will make the player lose a point
class Triangle(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color
        
    #Created triangle using three points of equal distance    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.polygon(surface, self.__color, ((self.getX(), self.getY()), (self.getX() - 25, self.getY() - 50), (self.getX() + 25, self.getY() - 50),))
    
    #Rectangular border for the triangle to determine if the ball intersects it
    def get_rect(self):
        width = 50
        height = 50
        if self.isVisible():
            return pygame.Rect(self.getX() - 25 , self.getY() - 50, width, height)

#Sqaure object will allow user to gain a point
class Square(Drawable):
    def __init__(self, x=0, y=0, color=(0, 0, 0)):
        super().__init__(x, y, color)
    
    #Squares are about the same size as triangles
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.rect(surface, self.getColor(), (self.getX(), self.getY(), 50, 50))
            
    #Border is the same as the actual shape   
    def get_rect(self):
        if self.isVisible():
            return pygame.Rect(self.getX(), self.getY(), 50, 50)

#Circle object allows player to gain a large amount of points
class Circle(Drawable):
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y, color)
        self.__radius = radius
        
    #Getter and setter for the radius
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.__radius = radius
    
    #Circle will be about the same size as the ball
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.getColor(), (self.getX(), self.getY()), self.__radius)
    
    #Border is slightly larger than circle
    def get_rect(self):
        radius = self.__radius
        if self.isVisible():
            return pygame.Rect(self.getX() - radius, self.getY() - radius, 2 * radius, 2 * radius)

#Line object will appear at the bottom of screen. They player will lose a point if the ball hits it.
class Line(Drawable):
    def __init__(self, x=0, y=0, color=(0, 0, 0)):
        super().__init__(x, y, color)
        
    #Line will span the bottom of the screen below the paddle    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.line(surface, self.getColor(), (self.getX(), self.getY()), (self.getX() + 800, self.getY()))
    
    #Border is the same size as the line
    def get_rect(self):
        if self.isVisible():
            return pygame.Rect(self.getX(), self.getY(), 800, 1)

    