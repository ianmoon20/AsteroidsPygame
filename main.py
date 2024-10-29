import pygame
from constants import *

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    if(pygame.get_init() == False):
        pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while(True):
        screen.fill((0,0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        '''
        Pause the game until 1/60th of a second has passed, then store the amount of time that's passed since the last time tick was called 
        converted from ms to seconds.
        '''
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
