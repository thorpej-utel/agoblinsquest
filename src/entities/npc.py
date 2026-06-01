import json
import os
import pygame
from src.utils.animation import SpriteSheet, Animation


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
        self._sprite = None
        self._anim = None
        self._offset_x = 0
        self._offset_y = 0
        sprite_path = data.get("sprite")
        if sprite_path and os.path.exists(sprite_path):
            fw = data.get("sprite_frame_w", 48)
            fh = data.get("sprite_frame_h", 64)
            n_idle = data.get("idle_frames", 2)
            sheet = SpriteSheet(sprite_path, fw, fh)
            frames = [sheet.get_frame(i) for i in range(n_idle)]
            self._anim = Animation(frames, fps=4, loop=True)
            self._offset_x = data.get("sprite_offset_x", (fw - self.size[0]) // 2)
            self._offset_y = data.get("sprite_offset_y", fh - self.size[1])
            self._sprite = True

    def update(self, dt):
        if self._anim:
            self._anim.update(dt)

    def render(self, surface, camera):
        if self._sprite and self._anim:
            frame = self._anim.current_frame()
            if not self.face_right:
                frame = pygame.transform.flip(frame, True, False)
            rect = camera.apply(self.rect)
            surface.blit(frame, (rect.x - self._offset_x, rect.y - self._offset_y))
            return
        rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, rect)
        darker = tuple(max(0, c - 40) for c in self.color)
        pygame.draw.rect(surface, darker, rect, 1)
        head = pygame.Rect(rect.x + 4, rect.y - 3, rect.w - 8, 6)
        pygame.draw.rect(surface, darker, head)
        eye_x = rect.x + 7 if self.face_right else rect.x + rect.w - 9
        pygame.draw.circle(surface, (255, 255, 240), (eye_x, rect.y + 2), 2)
        pygame.draw.circle(surface, (0, 0, 0), (eye_x, rect.y + 2), 1)
