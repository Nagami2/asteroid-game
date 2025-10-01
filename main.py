import pygame
from constants import *

from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # create a player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit the main function, which ends the game
        
        player.update(dt) # calling player's update method each frame

        # drawing comes after updating
        screen.fill("black") # fill the screen with a black color
        player.draw(screen)

        pygame.display.flip() # refresh the screen to show the new drawings

        # tick the clock to limit the FPS and get delta time for next frame
        dt = clock.tick(60) / 1000 # converting milliseconds to seconds 


if __name__ == "__main__":
    main()
