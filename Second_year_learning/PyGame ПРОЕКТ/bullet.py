"""
Данный клас предназначен для создания пули и взаимодействия
пули с другими спрайтами
"""

import pygame
# в этом модуле нужен список объектов,
# с которым будет взаимодействовать пуля
from lists_of_objects import bullets, objects

# импортируем размеры окна
from settings import WIDTH, HEIGHT

from bang import Bang


class Bullet:
    # в конструктор будем передавать ссылку parent на объект, который выпустил пулю
    # координаты px, py и направление dx, dy
    # параметр урона damage
    def __init__(self, parent, px, py, dx, dy, damage):
        # добавляем ссылку на объект в список всех пуль
        bullets.append(self)
        self.px = px
        self.py = py
        self.dx = dx
        self.dy = dy
        self.damage = damage
        self.parent = parent

    def update(self):
        # изменение координат пули (механика)
        self.px += self.dx
        self.py += self.dy

        # если пуля вылетает за край игрового поля, то удаляем ее из списка пуль
        if not 0 <= self.px <= WIDTH or not 0 <= self.py <= HEIGHT:
            bullets.remove(self)
        else:
            # если пуля попадает в объект, то,
            # исходя из урона, уничтожает объект
            for obj in objects:
                if obj is not self.parent and \
                        obj.rect.collidepoint(self.px, self.py) and obj.type != 'bang':
                    # print("ooops")
                    obj.damage(self.damage)
                    # после взаимодействия пули с объектом необходимо вызвать взрыв
                    Bang(self.px, self.py)
                    bullets.remove(self)
                    break

    # передаем в функцию ссылку на поле отрисовки screen
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="yellow",
                           center=(self.px, self.py), radius=2)
