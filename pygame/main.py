import pygame
import os
import random

# basic setup stuff
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("very awesome two player game")
pygame.font.init()
FPS = 60

# info for each player character
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 60
PLAYER1_IMAGE = pygame.image.load(os.path.join('Assets', 'obamacare_blue.png'))
PLAYER2_IMAGE = pygame.image.load(os.path.join('Assets', 'obamacare_red.png'))
PLAYER1 = pygame.transform.rotate(
    pygame.transform.scale(PLAYER1_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90
)
PLAYER2 = pygame.transform.rotate(
    pygame.transform.scale(PLAYER2_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270
)

# constant bullet variables
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 6
P1_BULLET_COLOR = (0, 0, 255)
P2_BULLET_COLOR = (255, 0, 0)

# ammo class for making the little reload boxes that appear on each player's side
class Ammo:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 12, 12)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        

def draw_window(player1, player2, p1_bullets, p2_bullets, p1_score, p2_score, p1_ammo, p2_ammo):
    WIN.fill((255, 255, 255))

    # line that visually separates the two sides
    pygame.draw.line(WIN, (0, 0, 0), (450, 0), (450, 500))

    # stuff to make the scoreboard
    font = pygame.font.Font(None, 74)
    p1_score_surface = font.render(str(p1_score), True, (0, 0, 0))
    WIN.blit(p1_score_surface, (WIDTH//2 - 50, 20))
    p2_score_surface = font.render(str(p2_score), True, (0, 0, 0))
    WIN.blit(p2_score_surface, (WIDTH//2 + 21, 20))

    # draw each player on the window
    WIN.blit(PLAYER1, (player1.x, player1.y))
    WIN.blit(PLAYER2, (player2.x, player2.y))

    # draw the bullets in bullet array
    for p1_bullet in p1_bullets:
        pygame.draw.rect(WIN, P1_BULLET_COLOR, p1_bullet)
    for p2_bullet in p2_bullets:
        pygame.draw.rect(WIN, P2_BULLET_COLOR, p2_bullet)
    
    # this and below handle how the ammount of ammo left is represented above each player's score
    p1_max_bullets = MAX_BULLETS - len(p1_bullets)
    p2_max_bullets = MAX_BULLETS - len(p2_bullets)

    for p1_bullet in range(p1_max_bullets):
        p1_ammo_shape = pygame.Rect((WIDTH//2) - 70 + p1_bullet * 10, 10, 8, 10)
        pygame.draw.rect(WIN, P1_BULLET_COLOR, p1_ammo_shape)
    for p2_bullet in range(p2_max_bullets):
        p2_ammo_shape = pygame.Rect(14 + (WIDTH//2) + p2_bullet * 10, 10, 8, 10)
        pygame.draw.rect(WIN, P2_BULLET_COLOR, p2_ammo_shape)

    for ammo in p1_ammo:
        ammo.draw(WIN)
    for ammo in p2_ammo:
        ammo.draw(WIN)

    pygame.display.update()

# controls for each player
def player_movement(keys_pressed, player1, player2):
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0:
        player1.x -= VEL
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < WIDTH / 2:
        player1.x += VEL
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0:
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL + player1.height < HEIGHT:
        player1.y += VEL

    if keys_pressed[pygame.K_j] and player2.x - VEL > WIDTH / 2:
        player2.x -= VEL
    if keys_pressed[pygame.K_l] and player2.x + VEL + player2.width > WIDTH / 2 and player2. x + VEL + player2.width < WIDTH:
        player2.x += VEL
    if keys_pressed[pygame.K_i] and player2.y - VEL > 0:
        player2.y -= VEL
    if keys_pressed[pygame.K_k] and player2.y + VEL + player2.height < HEIGHT:
        player2.y += VEL

# each time a player is hit by a bullet, this sets everything back to original state
def reset_game(player1, player2, p1_bullets, p2_bullets, p1_ammo, p2_ammo):
    player1.x, player1.y = 100, 225
    player2.x, player2.y = 750, 225
    p1_bullets.clear()
    p2_bullets.clear()
    p1_ammo.clear()
    p2_ammo.clear()

    font = pygame.font.Font(None, 100)
    
    # little timer to make sure each player is prepared
    ready_surface = font.render("READY", True, (255, 255, 0))
    WIN.blit(ready_surface, (328, 225))
    pygame.display.update()
    pygame.time.delay(1000)

    go_surface = font.render("GO", True, (0, 255, 0))
    WIN.blit(go_surface, (400, 225))
    pygame.display.update()
    pygame.time.delay(1000)

# collision for players and bullets
def handle_bullets(player1_bullets, player2_bullets, player1, player2, player1_score, player2_score, p1_ammo, p2_ammo):
    for p1_bullet in player1_bullets:
        p1_bullet.x += BULLET_VEL
        
        if p1_bullet.colliderect(player2):
            player1_score += 1
            reset_game(player1, player2, player1_bullets, player2_bullets, p1_ammo, p2_ammo)
            

    for p2_bullet in player2_bullets:
        p2_bullet.x -= BULLET_VEL
        
        if p2_bullet.colliderect(player1):
            player2_score += 1
            reset_game(player1, player2, player1_bullets, player2_bullets, p1_ammo, p2_ammo)
            
        # if a bullet hits a bullet, they both cancel out 
        for p1_bullet in player1_bullets:
            if p2_bullet.colliderect(p1_bullet):
                player1_bullets.remove(p1_bullet)
                player2_bullets.remove(p2_bullet)
    
    # score is passed back to the draw function where it can be used to update the scoreboard
    return player1_score, player2_score
    
    

def main():
    clock = pygame.time.Clock()

    player1 = pygame.Rect(100, 225, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(750, 225, PLAYER_WIDTH, PLAYER_HEIGHT)

    # variables for basic game stuff
    p1_score, p2_score = 0, 0
    p1_bullets, p2_bullets = [], []
    p1_ammo_timer, p2_ammo_timer = 0, 0
    p1_ammo_delay, p2_ammo_delay = 300, 300
    p1_ammo, p2_ammo = [], []

    # main loop that runs for as long as the user hasn't pressed the exit button
    run = True
    while run:
        clock.tick(FPS)

        # runs through all the events that happen while the game is running
        for event in pygame.event.get():
            # quit program if the x button is clicked
            if event.type == pygame.QUIT:
                run = False
            
            # adds bullets to bullet array when each player presses their shoot button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x and len(p1_bullets) < MAX_BULLETS:
                    p1_bullet = pygame.Rect(player1.x + player1.width - 5, player1.y + player1.height//2, 10, 5)
                    p1_bullets.append(p1_bullet)
                if event.key == pygame.K_m and len(p2_bullets) < MAX_BULLETS:
                    p2_bullet = pygame.Rect(player2.x, player2.y + player2.height//2, 10, 5)
                    p2_bullets.append(p2_bullet)

        # timer with some randomness that makes ammo (reload) objects appear on each player's side
        p1_ammo_timer += 1
        p2_ammo_timer += 1
        if p1_ammo_timer >= p1_ammo_delay and random.randint(1, 100) == 2:
            p1_new_ammo = Ammo(random.randint(20, WIDTH//2 - 20), random.randint(20, 480), P1_BULLET_COLOR)
            p1_ammo.append(p1_new_ammo)
            p1_ammo_timer = 0
        if p2_ammo_timer >= p2_ammo_delay and random.randint(1, 100) == 2:
            p2_new_ammo = Ammo(random.randint((WIDTH//2) + 20, WIDTH - 20), random.randint(20, 480), P2_BULLET_COLOR)
            p2_ammo.append(p2_new_ammo)
            p2_ammo_timer = 0
        
        # when a player runs into the ammo box, they get full ammo
        for ammo in p1_ammo:
            if player1.colliderect(ammo):
                p1_ammo.remove(ammo)
                p1_bullets.clear()
        for ammo in p2_ammo:
            if player2.colliderect(ammo):
                p2_ammo.remove(ammo)
                p2_bullets.clear()

        # player movement 
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player1, player2)

        # call handle_bullets function to get collision and also player scores
        p1_score, p2_score = handle_bullets(p1_bullets, p2_bullets, player1, player2, p1_score, p2_score, p1_ammo, p2_ammo)

        draw_window(player1, player2, p1_bullets, p2_bullets, p1_score, p2_score, p1_ammo, p2_ammo)

        
    pygame.quit()

if __name__ == "__main__":
    main()