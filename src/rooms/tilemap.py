import pygame
from settings import ROOM_COLS, ROOM_ROWS, TILE_SIZE

class TileMap:
    def __init__(self, tiles, color_map):
        self.tiles = tiles
        self.color_map = color_map

    def render(self, surface, camera):
        for row in range(ROOM_ROWS):
            for col in range(ROOM_COLS):
                tile_id = self.tiles[row][col]
                color = self.color_map.get(tile_id)
                if color is None:
                    continue
                x = col * TILE_SIZE - camera.x
                y = row * TILE_SIZE - camera.y
                pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))
