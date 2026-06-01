import pygame
import os

FRAME_W = 48
FRAME_H = 64
SHEET_PATH = "assets/sprites/goblin.png"

SKIN = (96, 188, 76)
SKIN_LT = (120, 215, 95)
SKIN_SH = (72, 150, 55)
SKIN_DK = (50, 110, 38)
TUNIC = (160, 100, 55)
TUNIC_LT = (185, 120, 70)
TUNIC_SH = (120, 70, 35)
BELT = (55, 30, 12)
BUCKLE = (210, 185, 45)
DARK = (30, 18, 8)
WHITE = (240, 240, 230)
PUPIL = (20, 20, 20)
EAR_IN = (165, 120, 95)
MOUTH = (55, 30, 18)
SATCHEL = (100, 60, 30)
SATCHEL_LT = (130, 80, 45)
TRANSPARENT = (0, 0, 0, 0)

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

def _darken(c, amount=0.6):
    return (int(c[0] * amount), int(c[1] * amount), int(c[2] * amount))


def draw_body(surf, leg_offset=0, arm_swing=0):
    _fill_rect(surf, 15, 28, 18, 14, TUNIC)
    _fill_rect(surf, 16, 28, 16, 14, TUNIC_LT)
    _fill_rect(surf, 11, 28, 5, 10, TUNIC_SH)
    _fill_rect(surf, 32, 28, 5, 10, TUNIC_SH)
    _fill_rect(surf, 17, 37, 14, 3, BELT)
    _set(surf, 23, 38, BUCKLE)
    _set(surf, 24, 38, BUCKLE)

    leg_l = 14 + leg_offset
    leg_r = 24 - leg_offset
    _fill_rect(surf, leg_l, 41, 8, 14, SKIN)
    _fill_rect(surf, leg_l, 41, 4, 14, SKIN_LT)
    _fill_rect(surf, leg_l + 6, 41, 2, 14, SKIN_SH)
    _fill_rect(surf, leg_r, 41, 8, 14, SKIN)
    _fill_rect(surf, leg_r, 41, 4, 14, SKIN_LT)
    _fill_rect(surf, leg_r + 6, 41, 2, 14, SKIN_SH)

    for leg_x in (leg_l - 1, leg_r - 1):
        _fill_rect(surf, leg_x + 1, 53, 10, 4, (60, 40, 25))
        _fill_rect(surf, leg_x + 1, 55, 10, 2, (80, 55, 35))

    arm_l_x = 8 + arm_swing
    arm_r_x = 32 - arm_swing
    _fill_rect(surf, arm_l_x, 29, 4, 12, SKIN)
    _set(surf, arm_l_x, 29, SKIN_SH)
    _fill_rect(surf, arm_r_x, 29, 4, 12, SKIN)
    _set(surf, arm_r_x + 3, 29, SKIN_SH)

    satchel_x = 30
    satchel_y = 30
    _fill_rect(surf, satchel_x, satchel_y, 8, 10, SATCHEL)
    _fill_rect(surf, satchel_x + 1, satchel_y + 1, 6, 4, SATCHEL_LT)
    _fill_rect(surf, satchel_x + 3, satchel_y - 1, 2, 2, SATCHEL_LT)
    _set(surf, satchel_x, satchel_y, DARK)
    _set(surf, satchel_x + 7, satchel_y, DARK)

def draw_head(surf, blink=False, look_x=0, look_y=0):
    _fill_ellipse(surf, 24, 16, 15, 14, SKIN)
    _fill_ellipse(surf, 24, 15, 14, 13, SKIN_LT)

    for ex, ey in ((10, 12), (38, 12)):
        pts = [(ex, ey), (ex - 5 if ex < 20 else ex + 5, ey + 2), (ex, ey + 10)]
        for p in pts:
            _set(surf, p[0], p[1], SKIN_SH)
        _fill_ellipse(surf, ex, ey + 5, 3, 6, SKIN)
        _fill_ellipse(surf, ex, ey + 5, 2, 5, EAR_IN)

    _fill_circle(surf, 17 + look_x, 16 + look_y, 5, WHITE)
    _fill_circle(surf, 31 + look_x, 16 + look_y, 5, WHITE)
    _set(surf, 16 + look_x, 16 + look_y, WHITE)
    _set(surf, 30 + look_x, 16 + look_y, WHITE)

    if blink:
        _fill_rect(surf, 13, 16, 8, 2, SKIN)
        _fill_rect(surf, 27, 16, 8, 2, SKIN)
    else:
        _fill_circle(surf, 18 + look_x, 17 + look_y, 2, PUPIL)
        _fill_circle(surf, 32 + look_x, 17 + look_y, 2, PUPIL)
        _set(surf, 17 + look_x, 16 + look_y, WHITE)
        _set(surf, 31 + look_x, 16 + look_y, WHITE)

    for ey in (13, 14):
        _set(surf, 17 + look_x, ey, SKIN_LT)
        _set(surf, 31 + look_x, ey, SKIN_LT)

    _set(surf, 24, 24, MOUTH)

    for bx in range(20, 29):
        for by in range(8, 10):
            _set(surf, bx, by, (0, 0, 0, 0))

    _fill_ellipse(surf, 24, 8, 10, 4, SKIN_LT)
    _fill_ellipse(surf, 20, 8, 3, 2, SKIN_LT)
    _fill_ellipse(surf, 28, 8, 3, 2, SKIN_LT)

    _set(surf, 22, 9, SKIN_DK)
    _set(surf, 26, 9, SKIN_DK)


def frame_idle(frame_num):
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    bob = 1 if frame_num == 1 else 0
    draw_body(surf, leg_offset=0, arm_swing=0)
    draw_head(surf, blink=(frame_num == 1))
    return surf

def frame_walk(frame_num):
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    offsets = [(3, -1), (0, 0), (-3, 1), (0, 0)]
    swings = [(2, 0), (0, 0), (-2, 0), (0, 0)]
    leg_off, arm_sw = offsets[frame_num][0], swings[frame_num][0]
    draw_body(surf, leg_offset=leg_off, arm_swing=arm_sw)
    draw_head(surf)
    return surf

def frame_jump():
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    draw_body(surf, leg_offset=0, arm_swing=4)
    draw_head(surf)
    for ax in (4, 36):
        _fill_rect(surf, ax, 20, 5, 3, SKIN)
        _set(surf, ax + 2, 19, SKIN_LT)
    return surf


def main():
    pygame.init()
    frames = []

    for i in range(2):
        frames.append(frame_idle(i))
    for i in range(4):
        frames.append(frame_walk(i))
    frames.append(frame_jump())

    sheet_w = FRAME_W * len(frames)
    sheet = pygame.Surface((sheet_w, FRAME_H), pygame.SRCALPHA)
    for i, f in enumerate(frames):
        sheet.blit(f, (i * FRAME_W, 0))

    os.makedirs(os.path.dirname(SHEET_PATH), exist_ok=True)
    pygame.image.save(sheet, SHEET_PATH)
    print(f"Saved sprite sheet: {SHEET_PATH} ({len(frames)} frames, {sheet_w}x{FRAME_H})")
    pygame.quit()


if __name__ == "__main__":
    main()
