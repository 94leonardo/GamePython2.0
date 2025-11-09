# src/main.py
import pygame
from settings import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR, GROUND_COLOR
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Megaman Lite - Stage 1")
clock = pygame.time.Clock()

player = Player(100, 380)
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fondo
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, GROUND_COLOR, (0, 430, WIDTH, 50))

    # Actualización
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
