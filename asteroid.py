import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # override to draw a circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() # original asteroid is always destroyed

        # if smallest aestoriod, do nothing else
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # generate random angle for the new asteroids' trajectories
        random_angle = random.uniform(20,50)

        # create 2 new velocity vectors rotated from the original
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        # calculate the radius for the new, smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create two new asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = new_vel1 * 1.2 # slightly faster
        asteroid2.velocity = new_vel2 * 1.2
        

        

