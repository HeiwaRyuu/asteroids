import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2) # screen, color, position(center), radius, line_width

    def update(self, dt):
        self.position += self.velocity * dt
