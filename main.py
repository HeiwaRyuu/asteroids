import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Setting screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Setting clock / FPS parameters
    dt = 0
    clock = pygame.time.Clock()
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Adding all Players, Shots and Asterois to the respective groups
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # Instantiating the player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Instantiating an AsteroidField
    asteroid_field = AsteroidField()
    while True:
        # Checking for close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Filling up the screen as black
        pygame.Surface.fill(screen,(0,0,0))
        # Updating all UPDATABLES
        for obj in updatable:
            obj.update(dt)
        # Checking for asteroid collision with player
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            if asteroid.out_of_bounds():
                asteroid.kill()
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.kill()
                if shot.out_of_bounds():
                    shot.kill()
        # Rendering all DRAWABLES
        for obj in drawable:
            obj.draw(screen)
        # Re-rendegin the screen
        pygame.display.flip()
        # Delta
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
