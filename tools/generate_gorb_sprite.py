import pygame
import os

FRAME_W = 48
FRAME_H = 64
SHEET_PATH = "assets/sprites/gorb.png"

SKIN = (140, 175, 75)
SKIN_LT = (170, 205, 95)
SKIN_SH = (105, 135, 55)
SKIN_DK = (70, 95, 35)
VEST = (140, 55, 65)
VEST_LT = (170, 70, 80)
VEST_SH = (105, 35, 45)
SHIRT = (220, 195, 155)
SHIRT_SH = (185, 160, 120)
BELT = (55, 30, 12)
BUCKLE = (210, 185, 45)
DARK = (30, 18, 8)
WHITE = (240, 240, 230)
PUPIL = (20, 20, 20)
EAR_IN = (175, 140, 100)
MOUTH = (55, 30, 18)
HAT = (110, 70, 40)
HAT_SH = (80, 50, 28)
HAT_LT = (140, 95, 55)
HAT_BAND = (60, 120, 60)
COIN = (210, 185, 45)
COIN_SH = (160, 135, 30)
GOLD_TOOTH = (210, 185, 45)
APRON = (110, 85, 55)
APRON_LT = (135, 110, 75)
APRON_SH = (80, 60, 35)

def _set(surf, x, y, color):
    if 0 <= x < FRAME_W and 0 <= y < FRAME_H:
        surf.set_at((x, y), color)

def _fill_rect(surf, x, y, w, h, color):
    for dy in range(h):
        for dx in range(w):
            _set(surf, x + dx, y + dy, color)

def _fill_circle(surf, cx, cy, r, color):
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r:
                _set(surf, cx + dx, cy + dy, color)

def _fill_ellipse(surf, cx, cy, rx, ry, color):
    for dy in range(-ry, ry + 1):
        for dx in range(-rx, rx + 1):
            if (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry) <= 1:
                _set(surf, cx + dx, cy + dy, color)

def draw_hat(surf):
    _fill_rect(surf, 14, 3, 20, 6, HAT)
    _fill_rect(surf, 15, 3, 18, 3, HAT_LT)
    _fill_ellipse(surf, 24, 10, 15, 4, HAT)
    _fill_ellipse(surf, 24, 10, 14, 3, HAT_LT)
    _fill_rect(surf, 14, 8, 20, 2, HAT_BAND)
    _fill_rect(surf, 35, 6, 8, 5, HAT)
    _fill_rect(surf, 35, 6, 7, 3, HAT_SH)

def draw_apron(surf):
    _fill_rect(surf, 17, 36, 14, 16, APRON)
    _fill_rect(surf, 18, 36, 12, 16, APRON_LT)
    _fill_rect(surf, 15, 36, 3, 10, APRON_SH)
    _fill_rect(surf, 30, 36, 3, 10, APRON_SH)

    _set(surf, 22, 42, COIN)
    _set(surf, 23, 42, COIN)
    _set(surf, 24, 42, COIN_SH)
    _set(surf, 22, 43, COIN_SH)
    _set(surf, 24, 43, COIN)

def draw_coin_pouch(surf, side):
    px = 7 if side < 0 else 33
    py = 34
    _fill_rect(surf, px, py, 5, 6, APRON_SH)
    _fill_rect(surf, px + 1, py + 1, 3, 4, APRON)
    _set(surf, px + 2, py - 1, DARK)
    _set(surf, px + 2, py, APRON_LT)

def draw_body(surf):
    _fill_rect(surf, 10, 22, 28, 18, SHIRT)
    _fill_rect(surf, 11, 22, 26, 18, SHIRT)
    _fill_rect(surf, 9, 28, 5, 8, VEST_SH)
    _fill_rect(surf, 34, 28, 5, 8, VEST_SH)

    _fill_rect(surf, 11, 28, 4, 12, VEST)
    _fill_rect(surf, 33, 28, 4, 12, VEST)
    _fill_rect(surf, 12, 28, 3, 12, VEST_LT)
    _fill_rect(surf, 33, 28, 3, 12, VEST_LT)

    _fill_rect(surf, 16, 37, 16, 3, BELT)
    _set(surf, 23, 38, BUCKLE)
    _set(surf, 24, 38, BUCKLE)

    leg_l = 15
    leg_r = 25
    _fill_rect(surf, leg_l, 41, 8, 14, SKIN)
    _fill_rect(surf, leg_l, 41, 4, 14, SKIN_LT)
    _fill_rect(surf, leg_l + 6, 41, 2, 14, SKIN_SH)
    _fill_rect(surf, leg_r, 41, 8, 14, SKIN)
    _fill_rect(surf, leg_r, 41, 4, 14, SKIN_LT)
    _fill_rect(surf, leg_r + 6, 41, 2, 14, SKIN_SH)

    for leg_x in (leg_l - 1, leg_r - 1):
        _fill_rect(surf, leg_x + 1, 53, 10, 4, (60, 40, 25))
        _fill_rect(surf, leg_x + 1, 55, 10, 2, (80, 55, 35))

    arm_l_x = 7
    arm_r_x = 35
    _fill_rect(surf, arm_l_x, 27, 5, 14, SKIN)
    _set(surf, arm_l_x, 27, SKIN_SH)
    _fill_rect(surf, arm_r_x, 27, 5, 14, SKIN)
    _set(surf, arm_r_x + 4, 27, SKIN_SH)

    draw_apron(surf)
    draw_coin_pouch(surf, 1)

def draw_face(surf, blink=False):
    _fill_ellipse(surf, 24, 16, 16, 15, SKIN)
    _fill_ellipse(surf, 24, 15, 15, 14, SKIN_LT)

    for ex, ey in ((9, 12), (39, 12)):
        _fill_ellipse(surf, ex, ey + 5, 3, 6, SKIN)
        _fill_ellipse(surf, ex, ey + 5, 2, 5, EAR_IN)

    _fill_circle(surf, 17, 16, 5, WHITE)
    _fill_circle(surf, 31, 16, 5, WHITE)

    if blink:
        _fill_rect(surf, 13, 16, 8, 2, SKIN)
        _fill_rect(surf, 27, 16, 8, 2, SKIN)
    else:
        _fill_circle(surf, 18, 17, 2, PUPIL)
        _fill_circle(surf, 32, 17, 2, PUPIL)
        _set(surf, 17, 16, WHITE)
        _set(surf, 31, 16, WHITE)

    _set(surf, 22, 25, GOLD_TOOTH)
    _set(surf, 23, 25, GOLD_TOOTH)
    _set(surf, 24, 25, MOUTH)
    _set(surf, 25, 25, GOLD_TOOTH)

    for bx in range(19, 30):
        for by in range(7, 10):
            _set(surf, bx, by, (0, 0, 0, 0))

    _fill_ellipse(surf, 24, 8, 11, 5, SKIN_LT)
    _fill_ellipse(surf, 20, 8, 4, 3, SKIN_LT)
    _fill_ellipse(surf, 28, 8, 4, 3, SKIN_LT)
    _set(surf, 22, 9, SKIN_DK)
    _set(surf, 26, 9, SKIN_DK)

def draw_head(surf, blink=False):
    draw_hat(surf)
    draw_face(surf, blink=blink)

def frame_idle(frame_num):
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    draw_body(surf)
    draw_head(surf, blink=(frame_num == 1))
    return surf

def main():
    pygame.init()
    frames = []
    for i in range(2):
        frames.append(frame_idle(i))

    sheet_w = FRAME_W * len(frames)
    sheet = pygame.Surface((sheet_w, FRAME_H), pygame.SRCALPHA)
    for i, f in enumerate(frames):
        sheet.blit(f, (i * FRAME_W, 0))

    os.makedirs(os.path.dirname(SHEET_PATH), exist_ok=True)
    pygame.image.save(sheet, SHEET_PATH)
    print(f"Saved: {SHEET_PATH} ({len(frames)} frames, {sheet_w}x{FRAME_H})")
    pygame.quit()

if __name__ == "__main__":
    main()
