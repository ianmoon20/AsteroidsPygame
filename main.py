import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    if(pygame.get_init() == False):
        pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Bullet.containers = (bullets, updateable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    while(True):
        screen.fill((0,0,0))

        for sprite in updateable:
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        for sprite in asteroids:
            if sprite.test_collision(player):
                print("Game over!")
                return
            
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.test_collision(asteroid):
                    bullet.kill()
                    asteroid.break_apart()

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
