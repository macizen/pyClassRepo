import pygame
import os
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
ENEMY_VEL = 2

OBAMA_WIDTH, OBAMA_HEIGHT = 60, 60
OBAMA_IMAGE = pygame.image.load(os.path.join('Assets', 'obamacare.png'))
OBAMA = pygame.transform.rotate(
    pygame.transform.scale(OBAMA_IMAGE, (OBAMA_WIDTH, OBAMA_HEIGHT)), 90
)

ENEMY_WIDTH, ENEMY_HEIGHT = 70, 70
ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'game_me.JPEG'))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.vel = ENEMY_VEL
    
    def update(self):
        self.rect.x -= self.vel

    def draw(self, window):
        window.blit(ENEMY, (self.rect.x, self.rect.y))

    def is_off_screen(self):
        return self.rect.x < -ENEMY_WIDTH

def draw_window(player, player_bullets, enemies):
    WIN.fill(WHITE)
    WIN.blit(OBAMA, (player.x, player.y))
    for bullet in player_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for enemy in enemies:
        enemy.draw(WIN)

    pygame.display.update()

def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH:
        player.x += VEL
    if keys_pressed[pygame.K_UP] and player.y - VEL > 0:
        player.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player.y + VEL + player.height < HEIGHT:
        player.y += VEL

def handle_bullets(player_bullets, enemies):
        for bullet in player_bullets:
            bullet.x += BULLET_VEL

            if bullet.x > WIDTH:
                player_bullets.remove(bullet)
                continue
            for enemy in enemies:
                if bullet.colliderect(enemy.rect):
                    player_bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

def main():

    player = pygame.Rect(100, 300, OBAMA_WIDTH, OBAMA_HEIGHT)
    player_bullets = []
    enemies = []

    enemy_spawn_timer = 0
    enemy_spawn_delay = 60

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player.x + player.width, player.y + player.height//2, 10, 5)
                    player_bullets.append(bullet)

        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            new_enemy = Enemy(WIDTH, random.randint(50, HEIGHT - ENEMY_HEIGHT - 50))
            enemies.append(new_enemy)
            enemy_spawn_timer = 0
        for enemy in enemies:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)
        
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
        handle_bullets(player_bullets, enemies)

        draw_window(player, player_bullets, enemies)
        
    pygame.quit()

if __name__ == "__main__":
    main()