import json
import pygame
from settings import ROOM_COLS, ROOM_ROWS, TILE_COLORS, TILE_SIZE
from src.rooms.tilemap import TileMap
from src.entities.npc import Npc, NpcManager
from src.entities.item import ItemPickup

class Room:
    def __init__(self, room_id, npc_manager, item_defs):
        self.id = room_id
        self.name = ""
        self.tiles = [[0] * ROOM_COLS for _ in range(ROOM_ROWS)]
        self.collision = [[0] * ROOM_COLS for _ in range(ROOM_ROWS)]
        self.exits = []
        self.checkpoint = False
        self.npcs = []
        self.items = []
        self.tilemap = None
        self._load(npc_manager, item_defs)

    def _load(self, npc_manager, item_defs):
        path = f"data/rooms/{self.id}.json"
        with open(path) as f:
            data = json.load(f)
        self.name = data.get("name", "")
        self.tiles = data["tiles"]
        self.collision = data.get("collision", data["tiles"])
        self.exits = data.get("exits", [])
        self.checkpoint = data.get("checkpoint", False)
        self.tilemap = TileMap(self.tiles, TILE_COLORS)

        self.npcs = []
        self.items = []
        for obj in data.get("objects", []):
            obj_type = obj["type"]
            if obj_type == "npc":
                npc = Npc(obj["id"], obj["x"], obj["y"], npc_manager)
                self.npcs.append(npc)
            elif obj_type == "item":
                item = ItemPickup(obj["id"], obj["x"], obj["y"], item_defs)
                self.items.append(item)

    def get_exit(self, direction):
        for e in self.exits:
            if e["direction"] == direction:
                return e
        return None

    def render(self, surface, camera):
        self.tilemap.render(surface, camera)
        for item in self.items:
            item.render(surface, camera)
        for npc in self.npcs:
            npc.render(surface, camera)

    @property
    def width(self):
        return ROOM_COLS * TILE_SIZE

    @property
    def height(self):
        return ROOM_ROWS * TILE_SIZE
