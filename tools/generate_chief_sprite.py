import pygame
import os

FRAME_W = 48
FRAME_H = 64
SHEET_PATH = "assets/sprites/chief.png"

SKIN = (112, 170, 70)
SKIN_LT = (140, 200, 90)
SKIN_SH = (80, 130, 48)
SKIN_DK = (55, 90, 30)
TUNIC = (130, 40, 50)
TUNIC_LT = (160, 55, 65)
TUNIC_SH = (95, 25, 35)
FUR = (170, 130, 90)
FUR_LT = (195, 155, 115)
FUR_SH = (130, 95, 60)
FUR_DK = (80, 55, 30)
BELT = (55, 30, 12)
BUCKLE = (210, 185, 45)
DARK = (30, 18, 8)
WHITE = (240, 240, 230)
PUPIL = (20, 20, 20)
EAR_IN = (165, 120, 95)
CROWN = (140, 95, 45)
CROWN_SH = (105, 70, 30)
CROWN_LT = (175, 125, 60)
SCAR = (185, 140, 130)
GEM_RED = (200, 35, 35)
CAPE = (100, 35, 45)
CAPE_SH = (70, 20, 30)

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

def _fill_triangle(surf, x1, y1, x2, y2, x3, y3, color):
    min_x = max(0, min(x1, x2, x3))
    max_x = min(FRAME_W - 1, max(x1, x2, x3))
    min_y = max(0, min(y1, y2, y3))
    max_y = min(FRAME_H - 1, max(y1, y2, y3))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            def sign(ax, ay, bx, by, cx, cy):
                return (ax - cx) * (by - cy) - (bx - cx) * (ay - cy)
            d1 = sign(x, y, x1, y1, x2, y2)
            d2 = sign(x, y, x2, y2, x3, y3)
            d3 = sign(x, y, x3, y3, x1, y1)
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            if not (has_neg and has_pos):
                _set(surf, x, y, color)

def draw_cape(surf):
    _fill_rect(surf, 6, 20, 6, 28, CAPE)
    _fill_rect(surf, 36, 20, 6, 28, CAPE)
    _fill_rect(surf, 6, 20, 36, 4, CAPE)
    for dy in range(24, 48, 4):
        _fill_rect(surf, 6, dy, 4, 2, CAPE_SH)
        _fill_rect(surf, 38, dy, 4, 2, CAPE_SH)
    for dy in range(46, 50):
        _set(surf, 6, dy, FUR_DK)
        _set(surf, 41, dy, FUR_DK)

def draw_fur_collar(surf):
    for dx in range(6, 42):
        for dy in range(18, 24):
            if dx < 8 or dx >= 40:
                if (dx + dy) % 3 == 0:
                    _set(surf, dx, dy, FUR_SH)
                else:
                    _set(surf, dx, dy, FUR)
            elif dx < 12 or dx >= 36:
                _set(surf, dx, dy, FUR)
            elif (dx + dy) % 4 == 0:
                _set(surf, dx, dy, FUR_SH)
            else:
                _set(surf, dx, dy, FUR_LT if (dx + dy) % 2 == 0 else FUR)

def draw_body(surf, leg_offset=0, arm_swing=0):
    draw_cape(surf)

    _fill_rect(surf, 13, 24, 22, 18, TUNIC)
    _fill_rect(surf, 14, 24, 20, 18, TUNIC_LT)
    _fill_rect(surf, 9, 24, 5, 12, TUNIC_SH)
    _fill_rect(surf, 34, 24, 5, 12, TUNIC_SH)

    draw_fur_collar(surf)

    _fill_rect(surf, 15, 37, 18, 4, BELT)
    _set(surf, 23, 38, BUCKLE)
    _set(surf, 24, 38, BUCKLE)

    leg_l = 13 + leg_offset
    leg_r = 23 - leg_offset
    _fill_rect(surf, leg_l, 41, 10, 14, SKIN)
    _fill_rect(surf, leg_l, 41, 5, 14, SKIN_LT)
    _fill_rect(surf, leg_l + 8, 41, 2, 14, SKIN_SH)
    _fill_rect(surf, leg_r, 41, 10, 14, SKIN)
    _fill_rect(surf, leg_r, 41, 5, 14, SKIN_LT)
    _fill_rect(surf, leg_r + 8, 41, 2, 14, SKIN_SH)

    for leg_x in (leg_l - 1, leg_r - 1):
        _fill_rect(surf, leg_x + 2, 53, 10, 4, (60, 40, 25))
        _fill_rect(surf, leg_x + 2, 55, 10, 2, (80, 55, 35))

    arm_l_x = 6 + arm_swing
    arm_r_x = 36 - arm_swing
    _fill_rect(surf, arm_l_x, 25, 5, 14, SKIN)
    _set(surf, arm_l_x, 25, SKIN_SH)
    _set(surf, arm_l_x + 4, 25, SKIN_SH)
    _fill_rect(surf, arm_r_x, 25, 5, 14, SKIN)
    _set(surf, arm_r_x + 4, 25, SKIN_SH)

def draw_crown(surf):
    cx, cy = 24, 2
    _fill_rect(surf, cx - 12, cy + 5, 24, 6, CROWN)
    _fill_rect(surf, cx - 12, cy + 5, 24, 3, CROWN_LT)

    _fill_triangle(surf, cx - 10, cy + 5, cx - 7, cy - 4, cx - 4, cy + 5, CROWN)
    _fill_triangle(surf, cx - 9, cy + 5, cx - 7, cy - 3, cx - 5, cy + 5, CROWN_LT)

    _fill_triangle(surf, cx - 3, cy + 5, cx, cy - 6, cx + 3, cy + 5, CROWN)
    _fill_triangle(surf, cx - 2, cy + 5, cx, cy - 4, cx + 2, cy + 5, CROWN_LT)

    _fill_triangle(surf, cx + 4, cy + 5, cx + 7, cy - 4, cx + 10, cy + 5, CROWN)
    _fill_triangle(surf, cx + 5, cy + 5, cx + 7, cy - 3, cx + 9, cy + 5, CROWN_LT)

    _set(surf, cx - 7, cy - 3, GEM_RED)
    _set(surf, cx, cy - 5, GEM_RED)
    _set(surf, cx + 7, cy - 3, GEM_RED)

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
    else:
        _fill_circle(surf, 18, 17, 2, PUPIL)
        _set(surf, 17, 16, WHITE)
        _set(surf, 26, 16, WHITE)
        _set(surf, 25, 16, SKIN)

    _fill_rect(surf, 25, 13, 8, 4, SKIN_DK)
    _fill_rect(surf, 25, 14, 8, 2, (70, 45, 30))
    _set(surf, 24, 16, SCAR)
    _set(surf, 25, 16, SCAR)
    _set(surf, 26, 16, SCAR)
    _set(surf, 23, 17, SCAR)
    _set(surf, 24, 17, SCAR)
    _set(surf, 25, 17, SCAR)
    _set(surf, 22, 18, SCAR)
    _set(surf, 23, 18, SCAR)

    _set(surf, 24, 24, MOUTH)

    for bx in range(19, 30):
        for by in range(7, 10):
            _set(surf, bx, by, (0, 0, 0, 0))

    _fill_ellipse(surf, 24, 8, 11, 5, SKIN_LT)
    _fill_ellipse(surf, 20, 8, 4, 3, SKIN_LT)
    _fill_ellipse(surf, 28, 8, 4, 3, SKIN_LT)
    _set(surf, 22, 9, SKIN_DK)
    _set(surf, 26, 9, SKIN_DK)

def draw_scar(surf):
    scar_points = [(32, 15), (34, 16), (35, 17), (36, 18), (37, 20)]
    for i, (sx, sy) in enumerate(scar_points):
        _set(surf, sx, sy, SCAR)
        _set(surf, sx + 1, sy, SCAR)
        if i > 0:
            _set(surf, sx, sy + 1, SCAR)

def draw_head(surf, blink=False):
    draw_crown(surf)
    draw_face(surf, blink=blink)
    draw_scar(surf)

MOUTH = (55, 30, 18)


def frame_idle(frame_num):
    surf = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
    bob = 1 if frame_num == 1 else 0
    draw_body(surf, leg_offset=0, arm_swing=0)
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
