import pygame
from constants import * 
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    color_rotation_dict = {0:(0,1,0), 1:(-1,0,0), 2:(0,0,1), 3:(0,-1,0), 4:(1,0,0), 5:(0,0,-1)}

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.forward = pygame.Vector2(0, 1)
        self.shot_cooldown = 60
        self.color = RAINBOW_START
        self.max_rgb_value = max(self.color)
        self.color_rotation_index = 0

    def triangle(self):
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - right
        c = self.position - self.forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 0) # screen, color, points, line_width (FILL FORM IF 0)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def find_rgb_index(self, color_rotation_index):
        counter = 0
        for index in self.color_rotation_dict[color_rotation_index]:
            if index != 0:
                return counter
            counter += 1

    # I have to create this trash function so i can iterate over different colors, converting TUPLE -> LIST -> TUPLE to change the correct RGB in sequence
    def next_rgb(self):
        rgb_index = self.find_rgb_index(self.color_rotation_index)
        next_value = self.color_rotation_dict[self.color_rotation_index][rgb_index]
        if self.color[rgb_index] + next_value > 0 and self.color[rgb_index] + next_value < self.max_rgb_value:
            self.color = list(self.color)
            self.color[rgb_index] = self.color[rgb_index] + (next_value * COLOR_CHANGE_RATIO)
            self.color = tuple(self.color)
        else:
            if self.color_rotation_index < 5:
                self.color_rotation_index += 1
            else:
                self.color_rotation_index = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown += dt
        # Color rotation
        self.next_rgb()

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
            shot.color = self.color


    def move(self, dt):
        self.position += self.forward * PLAYER_SPEED * dt
