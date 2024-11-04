import pygame
from constants import * 
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.forward = pygame.Vector2(0, 1)
        self.shot_cooldown = 60

    def triangle(self):
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - right
        c = self.position - self.forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.polygon(screen, white, self.triangle(), 2) # screen, color, points, line_width

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown += dt

        # Rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_cooldown > SHOT_DELAY:
            self.shot_cooldown = 0
            shot_direction = self.forward
            shot_position = self.position + shot_direction * self.radius
            shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
            shot.velocity = shot_direction * SHOT_VELOCITY


    def move(self, dt):
        self.position += self.forward * PLAYER_SPEED * dt
