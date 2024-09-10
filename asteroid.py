import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        #self.rotation = 0

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, 2)

    def update(self,dt):
        self.move(dt)

    def move(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.position)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector_a = pygame.math.Vector2.rotate(self.velocity,angle)
            vector_b = pygame.math.Vector2.rotate(self.velocity,-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_a = Asteroid(self.position.x,self.position.y,split_radius)
            split_b = Asteroid(self.position.x,self.position.y,split_radius)
            split_a.velocity = vector_a*1.2
            split_b.velocity = vector_b*1.2