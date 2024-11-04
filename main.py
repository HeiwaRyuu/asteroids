import pygame
from constants import *
from player import Player

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
    # Adding all Players to the groups
    Player.containers = (updatable, drawable)
    # Instantiating the player in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
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
        # Rendering all DRAWABLES
        for obj in drawable:
            obj.draw(screen)
        # Re-rendegin the screen
        pygame.display.flip()
        # Delta
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
