import pygame
import random
import sys
import os
import time
from pygame.locals import *

os.environ['SDL_AUDIODRIVER'] = 'darwin'
pygame.mixer.init()

# Global constants
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 30
BADDIEMINSIZE = 2
BADDIEMAXSIZE = 5
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5


hitSound = pygame.mixer.Sound('/Users/roshan1610/Downloads/Road Rush Game using Pygame/sound/zapsplat_impacts_car_crash_smash_head_on_23549.mp3')
runningSound = pygame.mixer.Sound('/Users/roshan1610/Downloads/Road Rush Game using Pygame/sound/car-race-car-citroen-race-screeching-tires-76578.mp3')

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Road Rush Game')
    pygame.mouse.set_visible(False)

    font = pygame.font.SysFont(None, 30)

    windowSurface.fill(BACKGROUNDCOLOR)

    playerRect = pygame.Rect((WINDOWWIDTH / 2, WINDOWHEIGHT - 50),(19,47))

    playerImage = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/car1.png')
    car3 = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/car3.png')
    car4 = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/car4.png')
    baddieImage = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/car2.png')
    wallLeft = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/left.png')
    wallRight = pygame.image.load('/Users/roshan1610/Downloads/Road Rush Game using Pygame/image/right.png')

    drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
    pygame.display.update()
    waitForPlayerToPressKey()

    # Initialize count variable with a value
    global count
    count = 3

    SAVE_FILE_PATH = '/Users/roshan1610/Downloads/Road Rush Game using Pygame/data/save.dat'
    if not os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, 'w') as f:
            f.write(str(0))

    # Read the top score from the save file
    with open(SAVE_FILE_PATH, 'r') as v:
        topScore = int(v.readline())

    while (count > 0):
        baddies = []
        score = 0
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        baddieAddCounter = 0

        while True: 
            runningSound.play()
            score += 1 

            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    if event.key == ord('z'):
                        reverseCheat = True
                    if event.key == ord('x'):
                        slowCheat = True
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == ord('w'):
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveUp = False
                        moveDown = True

                if event.type == KEYUP:
                    if event.key == ord('z'):
                        reverseCheat = False
                        score = 0
                    if event.key == ord('x'):
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                        terminate()

                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False

            if not reverseCheat and not slowCheat:
                baddieAddCounter += 1
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = 1 
                newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                            'surface': pygame.transform.scale(random.choice([playerImage, car3, car4, baddieImage]), (23, 47)),
                            }
                baddies.append(newBaddie)
                sideLeft= {'rect': pygame.Rect(0,0,126,600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(wallLeft, (126, 599)),
                        }
                baddies.append(sideLeft)
                sideRight= {'rect': pygame.Rect(497,0,303,600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(wallRight, (303, 599)),
                        }
                baddies.append(sideRight)

            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)

            for b in baddies:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif reverseCheat:
                    b['rect'].move_ip(0, -5)
                elif slowCheat:
                    b['rect'].move_ip(0, 1)

            for b in baddies[:]:
                if b['rect'].top > WINDOWHEIGHT:
                    baddies.remove(b)

            windowSurface.fill(BACKGROUNDCOLOR)
            drawText('Score: %s' % (score), font, windowSurface, 128, 0)
            drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
            drawText('Lives: %s' % (count), font, windowSurface, 128, 40)
            windowSurface.blit(playerImage, playerRect)

            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])

            pygame.display.update()

            if playerHasHitBaddie(playerRect, baddies):
                hitSound.play()
                runningSound.stop()
                count -= 1
                if count == 0:
                    break

            if playerHasHitBaddie(playerRect, baddies):
                hitSound.play()
                runningSound.stop()
                if score > topScore:
                    with open("data/save.dat", 'w') as g:
                        g.write(str(score))
                    topScore = score
                break

            mainClock.tick(FPS)

        time.sleep(1)
        if count == 0:
            runningSound.stop()
            drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
            pygame.display.update()
            time.sleep(2)
            waitForPlayerToPressKey()
            count = 3

if __name__ == '__main__':
    main()  # Call the main function when the script is executed directly
