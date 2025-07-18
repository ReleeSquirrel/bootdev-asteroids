import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_direction_1 = self.velocity.rotate(split_angle)
            split_direction_2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = split_direction_1 * 1.2
            new_asteroid_2.velocity = split_direction_2 * 1.2
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    

    def update(self, dt):
        self.position += (self.velocity * dt)