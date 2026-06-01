import json
import os
import pygame

class NpcManager:
    def __init__(self):
        self._cache = {}

    def load_npc(self, npc_id):
        if npc_id in self._cache:
            return self._cache[npc_id]
        path = f"data/npcs/{npc_id}/data.json"
        if not os.path.exists(path):
            return None
        with open(path) as f:
            data = json.load(f)
        self._cache[npc_id] = data
        return data

    def load_dialogue(self, npc_id):
        path = f"data/npcs/{npc_id}/dialogue.json"
        if not os.path.exists(path):
            return {}
        with open(path) as f:
            return json.load(f)


class Npc:
    def __init__(self, npc_id, x, y, manager):
        self.id = npc_id
        data = manager.load_npc(npc_id)
        self.name = data["name"]
        self.color = tuple(data["color"])
        self.size = tuple(data["size"])
        self.face_right = data.get("face_right", True)
        self.interact_range = data.get("interact_range", 24)
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.dialogue_id = None

    def render(self, surface, camera):
        rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, rect)
        darker = tuple(max(0, c - 40) for c in self.color)
        pygame.draw.rect(surface, darker, rect, 1)
        head = pygame.Rect(rect.x + 4, rect.y - 3, rect.w - 8, 6)
        pygame.draw.rect(surface, darker, head)
        eye_x = rect.x + 7 if self.face_right else rect.x + rect.w - 9
        pygame.draw.circle(surface, (255, 255, 240), (eye_x, rect.y + 2), 2)
        pygame.draw.circle(surface, (0, 0, 0), (eye_x, rect.y + 2), 1)
