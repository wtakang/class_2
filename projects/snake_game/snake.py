#!/home/tanyi/development/pythonclass/class_2/projects/snake_game/bin/python3

import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.position = [100,50] # this is the starting position of the snake
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT" #this is the direction of movement of snake aat start of game
       

    def changeDirTo(self,dir): #these are the directions when the arrow keys are pressed
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        elif dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        elif dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        elif dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"
        
    def move(self,foodPos): # here we move the forward or backward by either add or removing 10 and we do same for up and down movements
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + 10
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - 10
        elif self.direction == "UP":
            self.position[1] = self.position[1] - 10
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + 10
        self.body.insert(0,list(self.position))
        
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def move_Right(self): # directions of movements
        self.position[0] = self.position[0] + 10
    def move_Left(self):
        self.position[0] = self.position[0] - 10
    def move_Up(self):
        self.position[0] = self.position[1] - 10
    def move_Down(self):
        self.position[0] = self.position[1] + 10
    
    def checkCollision(self): # collision against the wall
        if self.position[0] > 490 or self.position[0] < 10:
            return 1 
        elif self.position[1] > 500 or self.position[1] < 10:
            return 1
        for bodyPart in self.body[1:]: # collision against itself
            if self.position == bodyPart:
                return 1
        return 0

    def getHeadPosition(self):
        return self.position
    
    def getBody(self):
        return self.body


class FoodSpawn():
    def __init__(self): # drop food at random x and y positions
        self.position = [random.randint(4,46)*10,random.randint(4,46)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(4,46)*10,random.randrange(4,46)*10]
            self.isFoodOnScreen = True
        return self.position
    
    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b


window = pygame.display.set_mode((500 + 20,500 + 20)) # set the game window size
pygame.display.set_caption("mySnake")# game title
fps = pygame.time.Clock() # clock for frames per second which is used to control snake speed

score = 0 #initial score at start of game

snake = Snake()
foodSpawner = FoodSpawn()

def gameOver():
    font = pygame.font.SysFont('Verdana', 30)
    score_text = font.render("Congrats you got " + str(score) + " points!",4,(255,0,0))
    window.blit(score_text,(100,250))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

while True: # here the loops for the game play
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
            snake.changeDirTo('RIGHT')
        elif pressed[pygame.K_LEFT]:
            snake.changeDirTo('LEFT')
        elif pressed[pygame.K_UP]:
            snake.changeDirTo('UP')
        elif pressed[pygame.K_DOWN]:
            snake.changeDirTo('DOWN')
        elif pressed[pygame.K_ESCAPE]:
            gameOver()

    foodPos = foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score+=1 # increase the score each time the food is picked by the snake
        foodSpawner.setFoodOnScreen(False)

    window.fill(pygame.Color(225,225,225))
    
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
    
    if(snake.checkCollision()==1):
        gameOver()
    
    pygame.display.set_caption("Snake | Score: " + str(score))# display final score at end of game
    pygame.display.flip()
    fps.tick(10)

pygame.quit()