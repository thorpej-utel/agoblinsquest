import json
import pygame
from src.ui.item_renderer import ItemSpriteRenderer

class ItemPickup:
    def __init__(self, item_id, x, y, definitions):
        self.item_id = item_id
        self.defs = definitions.get(item_id, {})
        self.sprite_index = self.defs.get("sprite_index", 0)
        self.color = tuple(self.defs.get("color", [180, 120, 200]))
        self.rect = pygame.Rect(x, y, 12, 12)
        self.collected = False

    def render(self, surface, camera):
        if self.collected:
            return
        rect = camera.apply(self.rect)
        ItemSpriteRenderer.render(surface, self.sprite_index, rect.x, rect.y, rect.w)
