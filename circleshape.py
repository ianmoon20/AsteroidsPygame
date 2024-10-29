from typing import Any
import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Ignore for now
        if hasattr(self, "container"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Set up the variables for controlling and displaying the hitboxes and sprites
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector(0,0)
        self.radius = radius

    def draw(self, screen) -> None:
        # Every subclass will need to override this
        pass

    def update(self, dt) -> None:
        # Every subclass will need to override this
        pass