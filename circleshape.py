import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass


    def check_collision(self, circle):
        center_distance = calculate_distance(self.position, circle.position)
        r1 = self.radius
        r2 = circle.radius
        if center_distance <= (r1+r2):
            return True 
        return False

    def out_of_bounds(self):
        rect_p1 = (0, 0)
        rect_p2 = (SCREEN_WIDTH, SCREEN_HEIGHT)
        within_x = (self.position.x + self.radius) >= rect_p1[0] and (self.position.x - self.radius) <= rect_p2[0]
        within_y = (self.position.y + self.radius) >= rect_p1[1] and (self.position.y - self.radius) <= rect_p2[1]
        if within_x and within_y:
            return False
        return True


def calculate_distance(p1, p2):
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**(1/2)
