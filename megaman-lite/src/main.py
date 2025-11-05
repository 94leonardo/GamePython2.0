# Archivo principal del juego:
# src/main.py

import pygame
from settings import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

player = Player(100, HEIGHT - 100)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    player.update()

    # Dibujar
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 50, WIDTH, 50))
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
