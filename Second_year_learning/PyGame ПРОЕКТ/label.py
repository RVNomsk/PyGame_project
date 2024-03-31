"""
Данный класс необходим для создания указателя в меню
"""

import pygame
from settings import img_tanks
from lists_of_objects import objects


class Label:
    def __init__(self, px, py):
        objects.append(self)
        self.px = px
        self.py = py
        self.type = 'label'
        # размер изображения метки танка
        self.image = pygame.transform.rotate(img_tanks[0], -90)
        self.size = self.image.get_size()
        self.rect = pygame.Rect(self.px, self.py, *self.size)

        self.k_up = pygame.K_UP
        self.k_down = pygame.K_DOWN

    def update(self, keys):
        # if keys[self.k_up]:
        #     self.py -= 100
        # elif keys[self.k_down]:
        #     self.py += 100
        pass

    def draw(self, screen):
        # screen.blit(self.image, self.rect)
        pass
