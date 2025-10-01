import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x , y, PLAYER_RADIUS)
        self.rotation = 0 # adding a rotation field
        self.shoot_timer = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # create a new shot at the player's position
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot  = Shot(self.position.x, self.position.y)
        # set the shot's velocity to move forward from the ship
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
    
    # update method to check for key presses
    def update(self, dt):
        # decrease the timer by dt every frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

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

        # spacebar input to call shoot method
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()

    
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
