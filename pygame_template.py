import pygame
import random

# Game settings
WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Template")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input
    screen.fill(WHITE)
    pygame.display.flip()

    all_sprites.update()

# Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()