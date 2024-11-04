import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = RED_PINK

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0) # screen, color, position(center), radius, line_width (SOLID FILL IF 0)

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
