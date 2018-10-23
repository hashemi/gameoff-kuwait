import pygame
import random

# Initilize PyGame
pygame.init()

#Set width/height
win = pygame.display.set_mode((500,500))

#Set display name
pygame.display.set_caption('Kuwait GameOFF')

# Gameobject with all functionality 
class GameObject:

    #defining the object 
    def __init__(self):
        #Place of the object in the screen
        self.x = 50
        self.y = 50
        #Size of the object
        self.width = 40
        self.height = 60
        #Velocity which the object travels in
        self.velocity = 10
        #Is the object jumping and a counter for the velocity which he fells to regular y-axes at
        self.isJumping = False
        self.jumpCount = 5

    #Handles moving and checking if its going outside the border of the game
    def left(self):
        if (self.x - self.velocity > 0):
            self.x -= self.velocity
    def right(self):
        if (self.x+self.velocity+self.width<500):
            self.x += self.velocity
    def up(self):
        if (self.y-self.velocity>0):
            self.y -= self.velocity
    def down(self):
        if (self.y+self.velocity+self.height<500):
            self.y += self.velocity
    #Jumping logic
    def jumping(self):
        if self.jumpCount >= -5:
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            self.y -= (self.jumpCount ** 2)  * neg
            self.jumpCount -= 1
        else:
            self.isJumping = False
            self.jumpCount = 5
    #Returns current location/width&height of the object
    def info(self):
        return ((self.x,self.y,self.width,self.height))

#Creates the object
gameobj = GameObject()
#Variable to controll running and disabling of the game
run = True

#Actual game logic
while run:
    #Delay to give realistic sense of a game
    pygame.time.delay(100)
    #Handles quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Grabs a list of all keys that are pressed to assign them to their functions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        break
    if keys[pygame.K_LEFT]:
        gameobj.left()
    if keys[pygame.K_RIGHT]:
        gameobj.right()
    #If the object is jumping we cannot control its vertial controllers 
    if not gameobj.isJumping:
        if keys[pygame.K_UP]:
            gameobj.up()
        if keys[pygame.K_DOWN]:
            gameobj.down()
        if keys[pygame.K_SPACE]:
            gameobj.isJumping = True
    else:
        gameobj.jumping()
    # Fills the background with the color black "RGB"
    win.fill((0,0,0))
    # Draws the game object
    pygame.draw.rect(win, (255,0,0), gameobj.info())
    # Updates the display of the game
    pygame.display.update()
#If it breaks outside the while loop it will quit the game
pygame.quit()