import random
import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT // 2)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, 30, 30))