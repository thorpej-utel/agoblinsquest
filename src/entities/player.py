import pygame
from settings import TILE_SIZE, PLAYER_SPEED, JUMP_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, GRAVITY
from src.systems.physics import move_and_collide, is_on_ground, is_on_oneway
from src.utils.animation import SpriteSheet, Animation

SPRITE_W = 48
SPRITE_H = 64
SPRITE_OFFSET_X = (SPRITE_W - PLAYER_WIDTH) // 2
SPRITE_OFFSET_Y = SPRITE_H - PLAYER_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.rect = pygame.Rect(int(x), int(y), PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vx = 0.0
        self.vy = 0.0
        self.grounded = False
        self.hearts = 4
        self.max_hearts = 4
        self.invincible_timer = 0.0
        self.facing_right = True

        sheet = SpriteSheet("assets/sprites/goblin.png", SPRITE_W, SPRITE_H)
        idle_frames = [sheet.get_frame(i) for i in range(2)]
        walk_frames = [sheet.get_frame(i) for i in range(2, 6)]
        jump_frames = [sheet.get_frame(6)]
        self.anims = {
            "idle": Animation(idle_frames, fps=4, loop=True),
            "walk": Animation(walk_frames, fps=8, loop=True),
            "jump": Animation(jump_frames, fps=1, loop=False),
        }
        self.anim_state = "idle"
        self.current_anim = self.anims["idle"]

    def update(self, dt, input, room):
        if self.invincible_timer > 0:
            self.invincible_timer -= dt
        self.vx = 0.0
        moving = False
        if input.is_key_down(pygame.K_LEFT) or input.is_key_down(pygame.K_a):
            self.vx = -PLAYER_SPEED
            self.facing_right = False
            moving = True
        if input.is_key_down(pygame.K_RIGHT) or input.is_key_down(pygame.K_d):
            self.vx = PLAYER_SPEED
            self.facing_right = True
            moving = True
        if (input.is_key_just_pressed(pygame.K_SPACE) or input.is_key_just_pressed(pygame.K_w) or input.is_key_just_pressed(pygame.K_UP)) and self.grounded:
            self.vy = JUMP_VELOCITY
            self.grounded = False

        self.vy = min(self.vy + GRAVITY * dt, 600.0)
        self.grounded = False
        self.vx, self.vy, self.grounded = move_and_collide(
            self.rect, self.vx, self.vy, dt, room.collision
        )
        if not self.grounded and self.vy >= 0 and is_on_ground(self.rect, room.collision):
            self.grounded = True
            self.vy = 0.0
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        if not self.grounded:
            self._set_anim("jump")
        elif moving:
            self._set_anim("walk")
        else:
            self._set_anim("idle")
        self.current_anim.update(dt)

    def _set_anim(self, name):
        if self.anim_state != name:
            self.anim_state = name
            self.current_anim = self.anims[name]
            self.current_anim.reset()

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
        frame = self.current_anim.current_frame()
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        screen_rect = camera.apply(self.rect)
        draw_x = screen_rect.x - SPRITE_OFFSET_X
        draw_y = screen_rect.y - SPRITE_OFFSET_Y
        surface.blit(frame, (draw_x, draw_y))
