import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class Game:
    def __init__(self):
        self.score = 0

    def increase_score(self, points):
        self.score += points

    def display_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))