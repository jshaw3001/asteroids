import pygame
import random
import circleshape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vec1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        vec2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        A1 = Asteroid(self.position.x, self.position.y, new_radius)
        A2 = Asteroid(self.position.x, self.position.y, new_radius)
        A1.velocity = vec1 * 1.2
        A2.velocity = vec2 * 1.2
