import pygame
import random
import os

# Game settings
WIDTH = 800
HEIGHT = 500
FPS = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# Player Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):        
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 50:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# Initialize
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Template")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input
    screen.fill(RED)

    # Update
    all_sprites.update()

    # Draw / render
    all_sprites.draw(screen)
    pygame.display.flip()


    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()