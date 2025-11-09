# src/player.py
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Rutas
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sprites_path = os.path.join(base_dir, "..", "assets", "sprites", "player")

        # Cargar sprites
        self.idle_frame = self.load_image("Sprite-0000.png")
        self.run_frames = self.load_frames(prefix="Sprite-", start=1, end=10)

        # Configuración inicial
        self.image = self.idle_frame
        self.rect = self.image.get_rect(topleft=(x, y))

        # Movimiento
        self.vel_y = 0
        self.on_ground = True
        self.direction = 0
        self.flip = False

        # Físicas
        self.gravity = 0.8
        self.jump_power = -15
        self.speed = 5

        # Animación
        self.current_frame = 0
        self.animation_speed = 0.15

    def load_image(self, filename):
        path = os.path.join(self.sprites_path, filename)
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (48, 48))
        else:
            # Cuadro blanco por defecto
            temp = pygame.Surface((48, 48))
            temp.fill((255, 255, 255))
            return temp

    def load_frames(self, prefix, start, end):
        frames = []
        for i in range(start, end + 1):
            filename = f"{prefix}{i:04d}.png"
            path = os.path.join(self.sprites_path, filename)
            if os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (48, 48))
                frames.append(img)
        return frames

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.direction = 0

        # Movimiento horizontal
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 1
            self.flip = False
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = -1
            self.flip = True

        # Salto
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Suelo
        if self.rect.bottom >= 430:
            self.rect.bottom = 430
            self.vel_y = 0
            self.on_ground = True

    def animate(self):
        if not self.on_ground:
            # Mientras salta, usa un frame fijo
            self.image = self.run_frames[0]
        elif self.direction != 0:
            # Si se mueve, animar frames de correr
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.run_frames):
                self.current_frame = 0
            self.image = self.run_frames[int(self.current_frame)]
        else:
            # Si está quieto, usar sprite-0000
            self.image = self.idle_frame

        # Voltear sprite si va a la izquierda
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
