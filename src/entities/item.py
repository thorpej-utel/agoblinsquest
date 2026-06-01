import json
import pygame

class ItemPickup:
    def __init__(self, item_id, x, y, definitions):
        self.item_id = item_id
        self.defs = definitions.get(item_id, {})
        self.color = tuple(self.defs.get("color", [180, 120, 200]))
        self.rect = pygame.Rect(x, y, 12, 12)
        self.collected = False

    def render(self, surface, camera):
        if self.collected:
            return
        rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (255, 255, 255, 128), rect, 1)
