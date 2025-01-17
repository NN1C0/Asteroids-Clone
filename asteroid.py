import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from event_constants import DESTROY_ASTEROID
from events import trigger_custom_event


class Asteroid(CircleShape):  
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.damage = self.radius / 2
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        super().kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            trigger_custom_event(DESTROY_ASTEROID)
            return
        spawn_angle = random.uniform(20, 50)
        angle1 = pygame.Vector2(self.velocity).rotate(spawn_angle)
        angle2 = pygame.Vector2(self.velocity).rotate(-(spawn_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_1.velocity = angle1 * 2
        asteroid_2.velocity = angle2 * 2