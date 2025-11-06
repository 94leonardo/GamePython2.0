# src/main.py
import pygame
from settings import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR, GROUND_COLOR
from player import Player
import os

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Megaman Lite - Stage 1")
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "..", "assets")

# Crear jugador y grupo de sprites
player = Player(100, 350)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 🎨 Dibujar en el orden correcto
    # Línea dentro del bucle principal
    screen.fill((25, 25, 35))  # fondo oscuro
    pygame.draw.rect(screen, (70, 160, 70), (0, 430, WIDTH, 50))  # suelo
    # 🎮 Actualizar lógica
    all_sprites.update()
    all_sprites.draw(screen)  # ← Jugador y otros sprites
    player.draw(screen)  # ← Asegura que el jugador se muestre

    pygame.display.flip()

pygame.quit()
