"""
Данный класс предназначен для создания взрыва не игровом поле
"""

from lists_of_objects import objects
from settings import img_bangs


class Bang:
    def __init__(self, px, py):
        # добавляем в класс обектов
        objects.append(self)
        # сами задаем тип объекта
        self.type = 'bang'
        # отслеживаем координаты взрыва
        self.px = px
        self.py = py
        # поле времени жизни взрыва
        self.frame = 0
        # загрузка и переход между картинками взрыва
        self.image = img_bangs[int(self.frame)]
        self.rect = self.image.get_rect(center=(self.px, self.py))

    def update(self):
        self.frame += 0.2
        if self.frame >= 3:
            objects.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
