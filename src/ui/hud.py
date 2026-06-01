import pygame
from settings import INTERNAL_WIDTH, TILE_SIZE

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("Consolas", 11)
        self.heart_full = "\u2665"
        self.heart_empty = "\u2661"

    def render(self, surface, player, inventory, items_def):
        hearts_text = ""
        for i in range(4):
            hearts_text += self.heart_full if i < player.hearts else self.heart_empty
        heart_surf = self.font.render(hearts_text, True, (220, 40, 40))
        surface.blit(heart_surf, (4, 4))

        gold_def = items_def.get("gold_tooth")
        if gold_def:
            coin_color = tuple(gold_def["color"])
            pygame.draw.circle(surface, coin_color, (110, 11), 5)
            pygame.draw.circle(surface, (255, 255, 200), (110, 11), 3)
            gold_count = inventory.items.count("gold_tooth")
            count_surf = self.font.render(f"x{gold_count}", True, (240, 200, 40))
            surface.blit(count_surf, (120, 4))

        slot_size = 14
        gap = 3
        total_width = inventory.MAX_SIZE * (slot_size + gap) - gap
        start_x = INTERNAL_WIDTH - total_width - 4
        for i in range(inventory.MAX_SIZE):
            sx = start_x + i * (slot_size + gap)
            sy = 4
            rect = pygame.Rect(sx, sy, slot_size, slot_size)
            pygame.draw.rect(surface, (40, 38, 50), rect)
            pygame.draw.rect(surface, (100, 95, 80), rect, 1)
            if i < len(inventory.items):
                item_id = inventory.items[i]
                item_def = items_def.get(item_id, {})
                color = tuple(item_def.get("color", [180, 120, 200]))
                inner = rect.inflate(-4, -4)
                pygame.draw.rect(surface, color, inner)
