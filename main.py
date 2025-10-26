import pygame
from constants import *
import player

def main():
    # Initialize pygame
    pygame.init()
    # Initialize screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Initialize screen refresh clock
    screen_clock = pygame.time.Clock()
    dt = 0
    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        player1.draw(screen)
        pygame.display.flip()
        dt = (screen_clock.tick(60))/1000
        


if __name__ == "__main__":
    main()
