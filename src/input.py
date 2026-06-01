import pygame

class Input:
    def __init__(self):
        self.keys_down = set()
        self.keys_pressed = set()
        self.keys_just_pressed = set()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.keys_down.add(event.key)
            self.keys_just_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            self.keys_down.discard(event.key)

    def update(self):
        self.keys_just_pressed.clear()
        self.keys_pressed = self.keys_down.copy()

    def is_key_down(self, key):
        return key in self.keys_pressed

    def is_key_just_pressed(self, key):
        return key in self.keys_just_pressed
