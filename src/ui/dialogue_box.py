import pygame
from settings import INTERNAL_WIDTH, INTERNAL_HEIGHT

BOX_MARGIN = 8
BOX_HEIGHT = 52
BOX_Y = INTERNAL_HEIGHT - BOX_HEIGHT - BOX_MARGIN
TEXT_X = BOX_MARGIN + 8
TEXT_Y = BOX_Y + 8
TEXT_WIDTH = INTERNAL_WIDTH - BOX_MARGIN * 2 - 16
LINE_HEIGHT = 14

class DialogueBox:
    def __init__(self):
        self.font = pygame.font.SysFont("Consolas", 11)
        self.name_font = pygame.font.SysFont("Consolas", 11, bold=True)

    def render(self, surface, speaker_name, text, text_complete, awaiting_input):
        box_rect = pygame.Rect(BOX_MARGIN, BOX_Y, INTERNAL_WIDTH - BOX_MARGIN * 2, BOX_HEIGHT)
        pygame.draw.rect(surface, (20, 18, 30), box_rect)
        pygame.draw.rect(surface, (100, 90, 70), box_rect, 2)

        name_surf = self.name_font.render(speaker_name, True, (220, 200, 140))
        surface.blit(name_surf, (TEXT_X, TEXT_Y - 2))

        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test = current_line + (" " if current_line else "") + word
            if self.font.size(test)[0] <= TEXT_WIDTH:
                current_line = test
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, (230, 225, 210))
            surface.blit(text_surf, (TEXT_X, TEXT_Y + 14 + i * LINE_HEIGHT))

        if text_complete and awaiting_input:
            arrow_x = INTERNAL_WIDTH - BOX_MARGIN - 16
            arrow_y = BOX_Y + BOX_HEIGHT - 14
            pygame.draw.polygon(surface, (200, 190, 170), [
                (arrow_x, arrow_y), (arrow_x + 8, arrow_y), (arrow_x + 4, arrow_y + 6)
            ])
