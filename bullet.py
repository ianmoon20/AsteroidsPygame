from circleshape import *
from constants import *

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def move(self, dt):
        self.position +=  self.velocity * dt

    def update(self, dt):
        self.move(dt)