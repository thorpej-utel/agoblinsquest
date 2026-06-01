import pygame
from settings import TILE_SIZE, PLAYER_SPEED, JUMP_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, GRAVITY
from src.systems.physics import move_and_collide

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.rect = pygame.Rect(int(x), int(y), PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vx = 0.0
        self.vy = 0.0
        self.grounded = False
        self.color = (80, 180, 80)
        self.hearts = 4
        self.max_hearts = 4
        self.invincible_timer = 0.0

    def update(self, dt, input, room):
        if self.invincible_timer > 0:
            self.invincible_timer -= dt
        self.vx = 0.0
        if input.is_key_down(pygame.K_LEFT) or input.is_key_down(pygame.K_a):
            self.vx = -PLAYER_SPEED
        if input.is_key_down(pygame.K_RIGHT) or input.is_key_down(pygame.K_d):
            self.vx = PLAYER_SPEED
        if (input.is_key_just_pressed(pygame.K_SPACE) or input.is_key_just_pressed(pygame.K_w) or input.is_key_just_pressed(pygame.K_UP)) and self.grounded:
            self.vy = JUMP_VELOCITY
            self.grounded = False

        self.vy = min(self.vy + GRAVITY * dt, 600.0)
        self.grounded = False
        self.vx, self.vy, self.grounded = move_and_collide(
            self.rect, self.vx, self.vy, dt, room.collision
        )
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_exit(self, room):
        for exit_data in room.exits:
            direction = exit_data["direction"]
            if direction == "right" and self.rect.right >= room.width:
                return exit_data
            if direction == "left" and self.rect.left <= 0:
                return exit_data
            if direction == "down" and self.rect.bottom >= room.height:
                return exit_data
            if direction == "up" and self.rect.top <= 0:
                return exit_data
        return None

    def render(self, surface, camera):
        rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, rect)
        head = pygame.Rect(rect.x + 4, rect.y - 4, rect.w - 8, 8)
        eye_color = (255, 255, 200)
        pygame.draw.rect(surface, (60, 140, 60), head)
        pygame.draw.circle(surface, eye_color, (rect.x + 7, rect.y - 1), 2)
        pygame.draw.circle(surface, eye_color, (rect.x + 13, rect.y - 1), 2)
