import pygame
import time
import random

pygame.init()

# pygame.display.flip() like a flipbook updates the entire surface
# pygame.display.update() will update the entire surface if you dont give it a area (more spesific)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
d_green = (0, 51, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height)) # 2() is nessacery sod that it doesnt read it as 2 seperate "800" "600"
pygame.display.set_caption('Nomster')

Icon = pygame.image.load("N_icon.png")
pygame.display.set_icon(Icon)

Apple = pygame.image.load('Apple.png')
S_H = pygame.image.load('Snake_Head.png')
#S_B = pygame.image.load('Snake_Body.png')
#S_T = pygame.image.load('Snake_Tail.png')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS= 15

direction = "right"

smallfont = pygame.font.SysFont("chiller", 25)
medfont = pygame.font.SysFont("chiller", 50)
largefont = pygame.font.SysFont("chiller", 80)

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(green)
        message_to_screen("Paused",
                          black,
                          0,
                          size="large")

        message_to_screen("Press C to continue or Q to quit",
                          black,
                          50)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - block_size))# / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size))# / 10.0) * 10.0

    return  randAppleX,randAppleY

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Welcome to Nomster",
                          blue,
                          -100,
                          "large")

        message_to_screen("How many apples can your Nomster eat?",
                          green,
                          0,
                          "medium")

        message_to_screen("Remember the more you eat. The more you grow!",
                          purple,
                          50,
                          "medium")

        message_to_screen("Nomster loves to eat. Careful not to eat yourself!",
                          red,
                          100,
                          "medium")

        message_to_screen("Press C to play, P to pause or Q to quit",
                          yellow,
                          200,
                          "medium")

        pygame.display.update()
        clock.tick(5)

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(S_H, 270)

    if direction == "left":
        head = pygame.transform.rotate(S_H, 90)

    if direction == "up":
        head = S_H

    if direction == "down":
        head = pygame.transform.rotate(S_H, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    #gameDisplay.blits(S_B, (snakeList[0][1], snakeList[0][2]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)
#    screen_text = font.render(msg, True, color)
#   gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():
    global direction

    direction ="right"
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("GAME OVER",
                              red,
                              -50,
                              size="large")
            message_to_screen("Try again. Press C",
                              purple,
                              0,
                              size="medium")
            message_to_screen("Get a life Press Q",
                              blue,
                              50,
                              size="medium")
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT: #so you can use the X on the window to close
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get(): #the keystrokes(user input)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True


            #print(event) will show the events happening (not in the window but for developers

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        gameDisplay.blit(Apple, (randAppleX, randAppleY))
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        score(snakeLength-1)

        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

        ##       if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness: for a bigger object collition
        ##          if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness
        ##              randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
        ##              randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        ##              snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()