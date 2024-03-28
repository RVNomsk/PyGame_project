import pygame
# в этом модуле нужен список объектов,
# с которым будет взаимодействовать пуля
from lists_of_objects import bullets, objects

# импортируем размеры окна
from settings import WIDTH, HEIGHT


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
                        obj.rect.collidepoint(self.px, self.py):
                    print("ooops")
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break

    # передаем в функцию ссылку на поле отрисовки screen
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="yellow",
                           center=(self.px, self.py), radius=2)


# b = Bullet("tank", 100, 100, 1, 1, 1)
# print(*bullets)
# pygame.init()
# # ширина, высота экрана
# WIDTH, HEIGHT = 800, 600
# # частота обновления кадров в секунду
# FPS = 60
# # цвет экрана
# SCREEN_COLOR = (0, 0, 0)
#
# # создадим игровое окно
# screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
#
# running = True
# while running:
#     for bullet in bullets:
#         bullet.draw(screen)
#     for bullet in bullets:
#         bullet.update()
#     pygame.display.update()