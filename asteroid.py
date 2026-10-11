from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_asteroids_angle = random.uniform(20,50)
            split_asteroid_velocity_one= self.velocity.rotate(new_asteroids_angle)
            split_asteroid_velocity_two = self.velocity.rotate(-new_asteroids_angle)
            split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            split_asteroid_one = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
            split_asteroid_one.velocity = split_asteroid_velocity_one * 1.2
            split_asteroid_two = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
            split_asteroid_two.velocity = split_asteroid_velocity_two * 1.2
