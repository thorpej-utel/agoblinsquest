import pygame
import os

W = 16
H = 16
SHEET_PATH = "assets/sprites/items.png"

def _set(surf, x, y, color):
    if 0 <= x < W and 0 <= y < H:
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

def _line(surf, x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy
    while True:
        _set(surf, x1, y1, color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

BROWN = (140, 100, 50)
BROWN_DK = (100, 65, 25)
BROWN_LT = (170, 130, 70)
TAN = (200, 170, 110)
RED = (200, 40, 40)
RED_DK = (140, 20, 20)
GREEN = (70, 160, 50)
GREEN_DK = (40, 110, 30)
GOLD = (220, 190, 40)
GOLD_DK = (160, 135, 20)
GOLD_LT = (250, 220, 80)
GREY = (140, 130, 120)
GREY_DK = (90, 85, 75)
GREY_LT = (180, 170, 160)
BLUE = (100, 180, 220)
BLUE_LT = (180, 220, 240)
PURPLE = (160, 80, 200)
PURPLE_LT = (200, 140, 240)
ORANGE = (220, 140, 40)
ORANGE_DK = (160, 90, 20)
YELLOW = (240, 210, 60)
WHITE = (240, 240, 230)
DARK = (30, 18, 8)
SKIN = (200, 160, 120)

def draw_rope(surf):
    _fill_rect(surf, 2, 3, 12, 3, BROWN)
    _fill_rect(surf, 2, 7, 12, 3, BROWN)
    _fill_rect(surf, 2, 11, 12, 3, BROWN)
    for x in (4, 8, 12):
        _fill_rect(surf, x, 4, 1, 11, BROWN_DK)
    _fill_rect(surf, 2, 5, 12, 1, BROWN_LT)

def draw_wooden_plank(surf):
    _fill_rect(surf, 0, 4, 16, 8, BROWN)
    _fill_rect(surf, 0, 4, 16, 3, BROWN_LT)
    _fill_rect(surf, 0, 8, 16, 2, BROWN_DK)
    _line(surf, 0, 6, 16, 6, BROWN_DK)
    for x in (3, 8, 13):
        _fill_rect(surf, x, 5, 1, 4, BROWN_DK)

def draw_giant_mushroom(surf):
    _fill_ellipse(surf, 8, 6, 8, 6, RED)
    _fill_ellipse(surf, 8, 6, 7, 5, RED_DK)
    _fill_rect(surf, 6, 10, 4, 5, TAN)
    _fill_rect(surf, 7, 10, 2, 5, (230, 210, 180))
    for sx, sy in [(4, 4), (9, 3), (12, 5), (6, 7)]:
        _set(surf, sx, sy, WHITE)
        _set(surf, sx + 1, sy, WHITE)
    _set(surf, 5, 5, WHITE)
    _fill_rect(surf, 7, 9, 2, 1, (30, 18, 8))

def draw_ancient_key(surf):
    _fill_circle(surf, 5, 5, 4, GOLD)
    _fill_circle(surf, 5, 5, 2, GOLD_DK)
    _fill_rect(surf, 7, 6, 7, 3, GOLD)
    _fill_rect(surf, 7, 6, 5, 1, GOLD_LT)
    _fill_rect(surf, 8, 3, 2, 2, GOLD_DK)
    for ty in (7, 10):
        _fill_rect(surf, 12, ty, 2, 1, GOLD_DK)

def draw_torch(surf):
    _fill_rect(surf, 7, 7, 3, 9, BROWN)
    _fill_rect(surf, 8, 7, 1, 8, BROWN_LT)
    _fill_ellipse(surf, 8, 5, 4, 5, ORANGE)
    _fill_ellipse(surf, 8, 5, 3, 4, YELLOW)
    _set(surf, 8, 2, WHITE)
    _set(surf, 9, 2, YELLOW)
    _set(surf, 6, 6, ORANGE_DK)

def draw_broken_gear(surf):
    _fill_circle(surf, 8, 8, 6, GREY)
    _fill_circle(surf, 8, 8, 4, GREY_LT)
    _fill_circle(surf, 8, 8, 2, GREY_DK)
    _fill_circle(surf, 8, 8, 1, DARK)
    for angle in range(0, 8):
        ax = 8 + int(6 * 0.7)
        ay = 8 + int(6 * 0.7)
        _fill_rect(surf, ax - 1, ay - 1, 3, 3, GREY)
    _line(surf, 11, 5, 14, 3, (0, 0, 0, 0))
    _set(surf, 12, 9, GREY_DK)
    _set(surf, 13, 8, GREY_DK)

def draw_hammer(surf):
    _fill_rect(surf, 7, 8, 3, 8, BROWN)
    _fill_rect(surf, 8, 8, 1, 8, BROWN_LT)
    _fill_rect(surf, 3, 3, 10, 6, GREY)
    _fill_rect(surf, 4, 3, 8, 3, GREY_LT)
    _fill_rect(surf, 3, 5, 10, 2, GREY_DK)
    _fill_rect(surf, 8, 1, 4, 2, GREY)
    _fill_rect(surf, 9, 1, 2, 2, GREY_LT)

def draw_golden_acorn(surf):
    _fill_ellipse(surf, 8, 9, 5, 6, GOLD)
    _fill_ellipse(surf, 8, 10, 4, 4, GOLD_LT)
    _fill_rect(surf, 4, 5, 8, 4, BROWN)
    _fill_rect(surf, 5, 5, 6, 3, BROWN_DK)
    _fill_rect(surf, 7, 1, 2, 5, BROWN)
    _fill_rect(surf, 8, 1, 1, 4, BROWN_LT)
    _set(surf, 5, 8, GOLD_DK)
    _set(surf, 10, 8, GOLD_DK)

def draw_crystal_lens(surf):
    _fill_circle(surf, 8, 8, 7, BLUE)
    _fill_circle(surf, 8, 8, 6, BLUE_LT)
    _fill_circle(surf, 8, 8, 4, (200, 235, 250))
    _fill_circle(surf, 8, 8, 2, WHITE)
    _fill_rect(surf, 0, 7, 3, 3, GREY)
    _fill_rect(surf, 13, 7, 3, 3, GREY)
    _fill_rect(surf, 7, 0, 3, 3, GREY)
    _fill_rect(surf, 7, 13, 3, 3, GREY)
    _set(surf, 5, 5, WHITE)

def draw_ancient_coin(surf):
    _fill_circle(surf, 8, 8, 7, GOLD)
    _fill_circle(surf, 8, 8, 6, GOLD_LT)
    _fill_circle(surf, 8, 8, 5, GOLD)
    _fill_circle(surf, 8, 8, 2, DARK)

def draw_gemstone(surf):
    _fill_rect(surf, 4, 1, 8, 2, PURPLE_LT)
    _fill_rect(surf, 2, 3, 12, 3, PURPLE)
    _fill_rect(surf, 1, 6, 14, 4, PURPLE)
    _fill_rect(surf, 2, 10, 12, 3, PURPLE)
    _fill_rect(surf, 4, 13, 8, 2, PURPLE)
    _fill_rect(surf, 3, 4, 10, 1, PURPLE_LT)
    _fill_rect(surf, 4, 5, 8, 1, (180, 110, 220))
    _set(surf, 8, 2, WHITE)

def draw_honey_cake(surf):
    _fill_rect(surf, 2, 4, 12, 10, BROWN_LT)
    _fill_rect(surf, 3, 4, 10, 4, TAN)
    _fill_rect(surf, 3, 8, 10, 4, BROWN_LT)
    _fill_rect(surf, 4, 5, 8, 1, GOLD)
    _fill_rect(surf, 4, 9, 8, 1, GOLD)
    _fill_rect(surf, 5, 6, 6, 2, GOLD_LT)
    _set(surf, 4, 2, GOLD)
    _set(surf, 5, 2, GOLD)
    _set(surf, 6, 1, GOLD)
    _set(surf, 10, 2, GOLD)
    _set(surf, 11, 2, GOLD)
    _set(surf, 12, 1, GOLD)

def draw_apple(surf):
    _fill_circle(surf, 8, 8, 6, RED)
    _fill_circle(surf, 8, 8, 5, (220, 50, 50))
    _fill_ellipse(surf, 7, 7, 3, 4, RED_DK)
    _fill_rect(surf, 8, 1, 2, 3, BROWN)
    _set(surf, 7, 2, GREEN)
    _set(surf, 8, 2, GREEN_DK)
    _fill_ellipse(surf, 10, 9, 3, 2, (220, 80, 80))
    _set(surf, 8, 5, (240, 100, 100))

def draw_roasted_mushroom(surf):
    _fill_ellipse(surf, 8, 5, 7, 5, BROWN)
    _fill_ellipse(surf, 8, 5, 6, 4, BROWN_LT)
    _fill_rect(surf, 6, 9, 4, 6, TAN)
    _fill_rect(surf, 7, 9, 2, 6, (220, 200, 170))
    _line(surf, 4, 3, 12, 3, BROWN_DK)
    _line(surf, 3, 5, 13, 5, BROWN_DK)
    _line(surf, 4, 7, 12, 7, BROWN_DK)
    _set(surf, 7, 8, BROWN_DK)

def draw_magic_spoon(surf):
    _fill_ellipse(surf, 6, 4, 5, 4, GREY_LT)
    _fill_ellipse(surf, 6, 4, 4, 3, WHITE)
    _fill_rect(surf, 7, 7, 3, 8, GREY_LT)
    _fill_rect(surf, 8, 7, 1, 8, WHITE)
    _set(surf, 1, 2, YELLOW)
    _set(surf, 2, 1, YELLOW)
    _set(surf, 15, 2, YELLOW)
    _set(surf, 14, 3, YELLOW)

def draw_gold_tooth(surf):
    _fill_ellipse(surf, 8, 9, 6, 6, GOLD)
    _fill_ellipse(surf, 8, 9, 5, 5, GOLD_LT)
    _fill_rect(surf, 4, 6, 8, 6, GOLD)
    _fill_rect(surf, 5, 6, 6, 5, GOLD_LT)
    _fill_rect(surf, 4, 10, 8, 3, GOLD_DK)
    _fill_rect(surf, 6, 3, 4, 4, GOLD)
    _fill_rect(surf, 7, 3, 2, 3, GOLD_LT)
    _fill_rect(surf, 6, 11, 1, 3, GOLD_DK)
    _fill_rect(surf, 9, 11, 1, 3, GOLD_DK)

DRAW_FUNCS = [
    draw_rope,
    draw_wooden_plank,
    draw_giant_mushroom,
    draw_ancient_key,
    draw_torch,
    draw_broken_gear,
    draw_hammer,
    draw_golden_acorn,
    draw_crystal_lens,
    draw_ancient_coin,
    draw_gemstone,
    draw_honey_cake,
    draw_apple,
    draw_roasted_mushroom,
    draw_magic_spoon,
    draw_gold_tooth,
]

ITEM_IDS = [
    "rope",
    "wooden_plank",
    "giant_mushroom",
    "ancient_key",
    "torch",
    "broken_gear",
    "hammer",
    "golden_acorn",
    "crystal_lens",
    "ancient_coin",
    "gemstone",
    "honey_cake",
    "apple",
    "roasted_mushroom",
    "magic_spoon",
    "gold_tooth",
]

def main():
    pygame.init()
    num_items = len(DRAW_FUNCS)
    sheet_w = W * num_items
    sheet = pygame.Surface((sheet_w, H), pygame.SRCALPHA)

    for i, draw_func in enumerate(DRAW_FUNCS):
        frame = pygame.Surface((W, H), pygame.SRCALPHA)
        draw_func(frame)
        sheet.blit(frame, (i * W, 0))

    os.makedirs(os.path.dirname(SHEET_PATH), exist_ok=True)
    pygame.image.save(sheet, SHEET_PATH)
    print(f"Saved: {SHEET_PATH} ({num_items} items, {sheet_w}x{H})")
    pygame.quit()

if __name__ == "__main__":
    main()
