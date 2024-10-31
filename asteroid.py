from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def move(self, dt):
        self.position +=  self.velocity * dt

    def spawn_asteroid(self):
        asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid.velocity = self.velocity.rotate(random.uniform(20, 50)) * (random.uniform(.75, 2))

    def break_apart(self):
        self.kill()
        if self.radius >= ASTEROID_MIN_RADIUS * 2:
            self.spawn_asteroid()
            self.spawn_asteroid()

    def update(self, dt):
        self.move(dt)