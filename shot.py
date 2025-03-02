import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        if velocity is None:
            self.velocity = pygame.Vector2(0, 0)
        else:
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt