import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            x,y = self.position
            angle = random.uniform(20,50)
            split_angle_1 = self.position.rotate(angle)
            split_angle_2 = self.position.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(x, y, new_radius)
            split_asteroid_2 = Asteroid(x,y, new_radius)
            split_asteroid_1.velocity = split_angle_1 * 1.2
            split_asteroid_2.velocity = split_angle_2  * 1.2