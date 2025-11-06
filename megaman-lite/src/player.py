# src/player.py
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Carpeta de sprites
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sprites_path = os.path.join(base_dir, "..", "assets", "sprites", "player")

        # Cargar todos los sprites
        self.frames = []
        for i in range(1, 7):  # Sprite-0001.png ... Sprite-0006.png
            frame_path = os.path.join(self.sprites_path, f"Sprite-{i:04d}.png")
            if os.path.exists(frame_path):
                image = pygame.image.load(frame_path).convert_alpha()
                image = pygame.transform.scale(image, (48, 48))
                self.frames.append(image)

        if not self.frames:
            print(
                "⚠️ No se encontraron imágenes de animación, usando un rectángulo temporal."
            )
            temp = pygame.Surface((32, 32))
            temp.fill((255, 255, 255))
            self.frames = [temp]

        # Imagen inicial
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

        # Control de animación
        self.current_frame = 0
        self.animation_speed = 0.15

        # Movimiento
        self.vel_y = 0
        self.on_ground = True
        self.direction = 0  # -1 izquierda, 1 derecha

    def update(self):
        keys = pygame.key.get_pressed()
        self.direction = 0

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.direction = 1
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.direction = -1

        # Animación solo si se mueve
        if self.direction != 0:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[int(self.current_frame)]

            # Voltear sprite según dirección
            if self.direction < 0:
                self.image = pygame.transform.flip(self.image, True, False)

        # Gravedad
        if not self.on_ground:
            self.vel_y += 0.5
            self.rect.y += self.vel_y
        if self.rect.bottom >= 430:
            self.rect.bottom = 430
            self.vel_y = 0
            self.on_ground = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
