from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    
    def triangle(self):
        forward = self.__get_forward_vector()
        right = self.__get_right_vector() * self.radius / 1.5

        # Get three points on the circle to represent the player's sprite of a triangle 
        a  = self.position + forward * self.radius
        b  = self.position - forward * self.radius - right
        c  = self.position - forward * self.radius + right
        
        return  [a, b, c]
    
    def __get_forward_vector(self):
        return pygame.Vector2(0,1).rotate(self.rotation)
    
    def __get_right_vector(self):
        return pygame.Vector2(1,0).rotate(self.rotation)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), PLAYER_LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        self.position +=  self.__get_forward_vector() * PLAYER_MOVE_SPEED * dt

    def shoot(self, dt):
        bullet = Bullet(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shoot(dt)