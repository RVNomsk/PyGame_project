import pygame

# список всех пуль
bullets = []


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