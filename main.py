import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()
    # Initialize screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Initialize screen refresh clock
    screen_clock = pygame.time.Clock()
    dt = 0
    # Create groups
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (shots_group, updateable_group, drawable_group)

    # Create a player
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create an asteroid field
    asteroid_field_1 = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        for item in updateable_group:
            item.update(dt)
        for item in asteroid_group:
            if item.collision(player1):
                print("Game over!")
                exit()
            for bullet in shots_group:
                if bullet.collision(item):
                    bullet.kill()
                    item.split()
        for item in drawable_group:
            item.draw(screen)
        pygame.display.flip()
        dt = (screen_clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
