import pygame
from constants import *
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2) # screen, color, position(center), radius, line_width

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Small asteroid (do not split)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        a1_velocity = self.velocity.rotate(angle)
        a2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_velocity
        a2.velocity = a2_velocity 
