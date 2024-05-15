import random
import pygame
from pygame.locals import *
import sqlite3
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED
from player import Player
from bullet import Bullet
from enemy import Enemy
from game import Game

# 데이터베이스 연결
conn = sqlite3.connect("main.db")
cursor = conn.cursor()

# 점수를 저장할 테이블 생성
cursor.execute("CREATE TABLE IF NOT EXISTS scores (player TEXT, score INTEGER)")

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

bullets = []  # bullets 변수 생성
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, bullets)
enemies = []
game = Game()

clock = pygame.time.Clock()
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_SPACE:
                player.shoot()

    screen.fill((0, 0, 0))

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)
        if bullet.y < 0:
            bullets.remove(bullet)

    if random.randint(0, 100) < 3:
        enemy = Enemy()
        enemies.append(enemy)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

    player.draw(screen)

    # 충돌 감지
    for enemy in enemies:
        for bullet in bullets:
            if (
                bullet.x > enemy.x
                and bullet.x < enemy.x + 30
                and bullet.y > enemy.y
                and bullet.y < enemy.y + 30
            ):
                enemies.remove(enemy)
                bullets.remove(bullet)
                game.increase_score(10)  # 적 처치 시 점수 증가

    # 충돌 감지: 플레이어와 충돌 시 게임 종료
    for enemy in enemies:
        if (
            enemy.x > player.x - 30
            and enemy.x < player.x + 20
            and enemy.y > player.y - 30
            and enemy.y < player.y + 20
        ):
            # 플레이어 점수 저장
            cursor.execute("INSERT INTO scores (player, score) VALUES (?, ?)", ("Player1", game.score))
            conn.commit()
            running = False
            break

    game.display_score(screen)  # 점수 표시

    pygame.display.flip()
    clock.tick(60)

# 데이터베이스 연결 종료
conn.close()
pygame.quit()