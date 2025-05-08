#Jeet Morker
#Jm5265
#This main script creates the game that puts all the objects onto the screen and created a point value that changes each time the ball hits an object

#importing files
import pygame
from ball import Ball
from paddle import Paddle
from text import Text
from drawable import *

#Creating all variables are objects needed for the game
pygame.init()
surface = pygame.display.set_mode((800, 600))
DREXEL_BLUE = (7, 41, 77)
red = (255, 0, 0)
aqua = (0, 255, 255)
green = (0, 255, 0)
myBall = Ball(400, 300, 25, DREXEL_BLUE)
myPaddle = Paddle(200, 25, DREXEL_BLUE)
tri1 = Triangle(100, 200, red)
tri2 = Triangle(650, 200, red)
tri3 = Triangle(400, 250, red)
sq1 = Square(200, 300, aqua)
sq2 = Square(525, 300, aqua)
sq3 = Square(375, 0, aqua)
circ = Circle(400, 100, 25, green)
circ2 = Circle(400, 500, 25, green)
line = Line(0, 595, red)

#Objects that can be intersected are stored in this list
objects = [myPaddle, tri1, tri2, tri3, sq1, sq2, sq3, circ, circ2, line]

#The scoreboard shows the game state. The user wins with 8+ points and loses with less than 0
myScoreBoard = Text("Score: 0", 10, 10)
win = Text("You earned 8+ points! You Win!", 50, 250, green, 50)
lose = Text("You are below 0 points! You Lose!", 50, 250, red, 40)
running  = True
fpsClock = pygame.time.Clock()
numHits = 0

#Draws objects onto the game
while running:
    surface.fill((210, 180, 140))
    myBall.draw(surface)
    myScoreBoard.draw(surface)
    for item in objects:
        item.draw(surface)
        
    #If the ball intersects an object, it bounces in the opposite direction and speeds up. Has a maximum speed limit.
    for item in objects:
        if myBall.intersects(item):
            if myBall.getYSpeed() > -8 and myBall.getYSpeed() < 8: 
                myBall.setYSpeed(myBall.getYSpeed()*-2)
            else:
                myBall.setYSpeed(myBall.getYSpeed()*-1)
                
            #Checks to see what the intersected object is. Point values change depending on the type. 
            if isinstance(item, Triangle):
                numHits -= 1
            elif isinstance(item, Circle):
                numHits += 3
            elif isinstance(item, Line):
                numHits -= 1
            else:
                numHits += 1
                
            #Objects disapear when hit, except for the paddle and line
            if isinstance(item, Paddle):
                pass
            elif isinstance(item, Line):
                pass
            else:
                item.setVisible(False)
            #Score is updated after each hit
            myScoreBoard.setMessage("Score: " + str(numHits))
    
    #The user wins if point value is 8+ and loses when its less than 0. All objects dissapear to show that the game is over. 
    if numHits >= 8:
        myBall.setVisible(False)
        for item in objects:
            item.setVisible(False)
        win.draw(surface)
    elif numHits < 0:
        myBall.setVisible(False)
        for item in objects:
            item.setVisible(False)
        lose.draw(surface)
    
    myBall.move()
    
    #Allows the user to exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        #The user can click the mouse botton to make the ball invisible to avoid hitting objects
        elif event.type == pygame.MOUSEBUTTONDOWN:
            myBall.setVisible(not myBall.isVisible())
    pygame.display.update()
    fpsClock.tick(30) # Approx. 30 Frames Per Second
exit()
