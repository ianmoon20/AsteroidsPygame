import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Ignore for now
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Set up the variables for controlling and displaying the hitboxes and sprites
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        # Every subclass will need to override this
        pass

    def update(self, dt):
        # Every subclass will need to override this
        pass

    def test_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius