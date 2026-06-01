import pygame
import os

ITEM_SHEET_PATH = "assets/sprites/items.png"
FRAME_W = 16
FRAME_H = 16

class ItemSpriteRenderer:
    _sheet = None
    _frames = {}

    @classmethod
    def _ensure_loaded(cls):
        if cls._sheet is not None:
            return
        if os.path.exists(ITEM_SHEET_PATH):
            cls._sheet = pygame.image.load(ITEM_SHEET_PATH).convert_alpha()
        else:
            cls._sheet = pygame.Surface((0, 0))

    @classmethod
    def get_frame(cls, index):
        cls._ensure_loaded()
        if index not in cls._frames:
            frame = pygame.Surface((FRAME_W, FRAME_H), pygame.SRCALPHA)
            if cls._sheet.get_width() > index * FRAME_W:
                frame.blit(cls._sheet, (0, 0), (index * FRAME_W, 0, FRAME_W, FRAME_H))
            cls._frames[index] = frame
        return cls._frames[index]

    @classmethod
    def render(cls, surface, index, x, y, size):
        frame = cls.get_frame(index)
        scaled = pygame.transform.scale(frame, (size, size))
        surface.blit(scaled, (x, y))
