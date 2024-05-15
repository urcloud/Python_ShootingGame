import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 5, 10))