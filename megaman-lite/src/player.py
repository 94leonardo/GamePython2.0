# Controla el movimiento del personaje.

# src/player.py
import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 48))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Salto
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

        # Gravedad
        self.vel_y += 1
        self.rect.y += self.vel_y

        # Colisión con el suelo
        if self.rect.bottom >= 430:
            self.rect.bottom = 430
            self.vel_y = 0
            self.on_ground = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)
