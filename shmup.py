import pygame
import random

# Game settings
WIDTH = 400
HEIGHT = 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot em up")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 5

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input
    screen.fill(WHITE)

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