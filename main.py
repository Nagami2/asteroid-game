import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit the main function, which ends the game
        # drawing
        screen.fill("black") # fill the screen with a black color

        # update the display
        pygame.display.flip() # refresh the screen to show the new drawings


if __name__ == "__main__":
    main()
