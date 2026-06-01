import pygame
from settings import INTERNAL_WIDTH, INTERNAL_HEIGHT

class InventoryScreen:
    def __init__(self):
        self.font = pygame.font.SysFont("Consolas", 12)
        self.title_font = pygame.font.SysFont("Consolas", 14, bold=True)
        self.selected = 0

    def render(self, surface, inventory, items_def):
        overlay = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((10, 10, 20))
        surface.blit(overlay, (0, 0))

        title = self.title_font.render("INVENTORY", True, (200, 190, 160))
        surface.blit(title, (INTERNAL_WIDTH // 2 - title.get_width() // 2, 12))

        slot_size = 40
        gap = 8
        cols = 3
        rows = (inventory.MAX_SIZE + cols - 1) // cols
        grid_w = cols * (slot_size + gap) - gap
        grid_h = rows * (slot_size + gap) - gap
        start_x = (INTERNAL_WIDTH - grid_w) // 2
        start_y = 40

        for i in range(inventory.MAX_SIZE):
            col = i % cols
            row = i // cols
            sx = start_x + col * (slot_size + gap)
            sy = start_y + row * (slot_size + gap)
            rect = pygame.Rect(sx, sy, slot_size, slot_size)
            selected = (i == self.selected)
            bg = (50, 48, 60) if selected else (30, 28, 40)
            border = (180, 170, 140) if selected else (80, 75, 65)
            pygame.draw.rect(surface, bg, rect)
            pygame.draw.rect(surface, border, rect, 2)

            if i < len(inventory.items):
                item_id = inventory.items[i]
                item_def = items_def.get(item_id, {})
                color = tuple(item_def.get("color", [180, 120, 200]))
                inner = rect.inflate(-8, -8)
                pygame.draw.rect(surface, color, inner)
                name = item_def.get("name", item_id)
                name_surf = self.font.render(name, True, (220, 215, 200))
                surface.blit(name_surf, (rect.x + 4, rect.y + rect.h + 2))

        if inventory.items and self.selected < len(inventory.items):
            selected_id = inventory.items[self.selected]
            item_def = items_def.get(selected_id, {})
            desc = item_def.get("description", "")
            desc_surf = self.font.render(desc, True, (180, 175, 160))
            surface.blit(desc_surf, (20, INTERNAL_HEIGHT - 40))
            item_type = item_def.get("type", "")
            type_surf = self.font.render(f"Type: {item_type}", True, (140, 135, 120))
            surface.blit(type_surf, (20, INTERNAL_HEIGHT - 24))
