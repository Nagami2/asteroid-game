from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x , y, PLAYER_RADIUS)
        self.rotation = 0 # adding a rotation field

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    # update method to check for key presses
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # call rotate() with a negative dt to turn left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # handle movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    # method to calculate the triangle's points
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override draw method to draw a polygon(our triangle)
    def draw(self, screen):
        pygame.draw.polygon (screen, "white", self.triangle(), 2)
