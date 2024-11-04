import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda radius,y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda radius,y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda radius,x: pygame.Vector2(x * SCREEN_WIDTH, -radius)
        ],
        [
            pygame.Vector2(0, -1),
            lambda radius,x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + radius
            ),
        ],
    ]

    def __init__(self):
        super().__init__(self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position, radius, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            # Spawn a new Asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            kind = random.randint(1, ASTEROID_KINDS)
            radius = ASTEROID_MIN_RADIUS * kind
            velocity = edge[0] * speed
            position = edge[1](radius,random.uniform(0, 1))
            self.spawn(position, radius, velocity)

    
