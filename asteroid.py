import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
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
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        debris_velocity_pos_angle = self.velocity.rotate(random_angle)
        debris_velocity_neg_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Asteroid debris broken into 2 pieces in different directions
        asteroid_debris1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_debris1.velocity = debris_velocity_pos_angle * 1.2

        asteroid_debris2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_debris2.velocity = debris_velocity_neg_angle * 1.2