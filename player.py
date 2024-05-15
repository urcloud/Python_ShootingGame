import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from bullet import Bullet

class Player:
    def __init__(self, screen_width, screen_height, color, bullets):
        self.x = screen_width // 2
        self.y = screen_height - 50
        self.color = color
        self.bullets = bullets  # bullets 변수 추가
        self.speed = 5

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def shoot(self):
        bullet = Bullet(self.x, self.y)
        self.bullets.append(bullet)  # bullets 리스트에 bullet 추가

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 20, 20))
