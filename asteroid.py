import pygame
from circleshape import CircleShape
from constants import *
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, num_points=12):
        super().__init__(x, y, radius)
        self.num_points = num_points
        self.points = self.generate_points()

    def generate_points(self):
        points = []
        for i in range(self.num_points):
            angle = i * (2 * math.pi / self.num_points)
            radius_variation = random.uniform(0.8, 1.2)
            x = self.radius * radius_variation * math.cos(angle)
            y = self.radius * radius_variation * math.sin(angle)
            points.append((x, y))
        return points

    def draw(self, screen):
        translated_points = [(self.position.x + point[0], self.position.y + point[1]) for point in self.points]
        pygame.draw.polygon(screen, "white", translated_points, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = a * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = b * 1.2
