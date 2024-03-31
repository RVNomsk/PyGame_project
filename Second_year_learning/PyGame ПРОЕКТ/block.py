"""
Данный класс предназначен для создания стен на игровом поле
"""

from lists_of_objects import objects
import pygame
from settings import img_brick


class Block:
    def __init__(self, px, py, size):
        # добавим блок в список всех объектов
        objects.append(self)
        # для отличия объектов (танков и блоков)
        # для простоты создадим переменную type
        self.type = 'block'
        # впишем блок в квадрат
        self.rect = pygame.Rect(px, py, size, size)
        # параметр здоровья
        self.hp = 1

    def update(self):
        pass

    # отрисовка блока на экране screen
    def draw(self, screen):
        screen.blit(img_brick, self.rect)
        # pygame.draw.rect(surface=screen, color="green",
        #                  rect=self.rect, width=2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
