import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        red = (255, 0, 0)
        pygame.draw.circle(screen, red, self.position, self.radius, 2) # screen, color, position(center), radius, line_width

    def update(self, dt):
        if self.velocity.length() < MAX_SHOT_VELOCITY:
            self.position += self.velocity 
            self.velocity *= SHOT_ACCELERATION 
        else:
            self.velocity = MAX_SHOT_VELOCITY
        if self.radius + SHOT_SIZE_INCREASE < MAX_SHOT_RADIUS:
            self.radius += SHOT_SIZE_INCREASE
        else:
            self.radius = MAX_SHOT_RADIUS
