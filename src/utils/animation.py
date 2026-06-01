import pygame

class SpriteSheet:
    def __init__(self, path, frame_w, frame_h):
        self.sheet = pygame.image.load(path).convert_alpha()
        self.frame_w = frame_w
        self.frame_h = frame_h
        sheet_w = self.sheet.get_width()
        self.cols = sheet_w // frame_w

    def get_frame(self, index):
        col = index % self.cols
        rect = pygame.Rect(col * self.frame_w, 0, self.frame_w, self.frame_h)
        frame = pygame.Surface((self.frame_w, self.frame_h), pygame.SRCALPHA)
        frame.blit(self.sheet, (0, 0), rect)
        return frame


class Animation:
    def __init__(self, frames, fps=8, loop=True):
        self.frames = frames
        self.fps = fps
        self.loop = loop
        self.timer = 0.0
        self.index = 0
        self.done = False

    def update(self, dt):
        if self.done:
            return
        self.timer += dt
        frame_duration = 1.0 / self.fps
        while self.timer >= frame_duration:
            self.timer -= frame_duration
            self.index += 1
            if self.index >= len(self.frames):
                if self.loop:
                    self.index = 0
                else:
                    self.index = len(self.frames) - 1
                    self.done = True
                    return

    def current_frame(self):
        return self.frames[self.index]

    def reset(self):
        self.timer = 0.0
        self.index = 0
        self.done = False
