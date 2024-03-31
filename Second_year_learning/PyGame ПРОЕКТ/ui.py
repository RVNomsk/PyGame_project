"""
Данный класс предназначен для вывода информации в поле игры
"""

import pygame
from lists_of_objects import objects
from settings import FONT_UI


class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        i = 0  # индекс игрока
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(surface=screen, color=obj.color, rect=(5 + i * 70, 5, 22, 22))

                text = FONT_UI.render(str(obj.hp), True, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
                screen.blit(text, rect)
                i += 1

