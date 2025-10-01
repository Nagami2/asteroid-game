import pygame
import sys
from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create drawable and updatable groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    #setting the containers for the player class, before creating any player instance
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # create a player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # exit the main function, which ends the game
        
        # player.update(dt) # calling player's update method each frame
        updatable.update(dt) # update all updatable objects

        # check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit() 

        # check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # call split method, instead of removing it
                    shot.kill()      # remove the shot

        # remove shots that are off-screen to prevent memory leaks
        for shot in shots:
            if (shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or 
                shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT):
                shot.kill()

        # drawing comes after updating
        screen.fill("black") # fill the screen with a black color

        # loop through all drawables
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip() # refresh the screen to show the new drawings

        # tick the clock to limit the FPS and get delta time for next frame
        dt = clock.tick(60) / 1000 # converting milliseconds to seconds 


if __name__ == "__main__":
    main()
