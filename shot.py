import pygame
from constants import *
from circleshape import CircleShape

class Shot (CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
    
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, PLAYER_SHOOT_SPEED: float) -> None:
        self.position += (self.velocity * PLAYER_SHOOT_SPEED)
        