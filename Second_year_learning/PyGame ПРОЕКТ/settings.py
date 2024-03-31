"""
В данном файле хранятся общие настройки, происходит
загрузка картинок игры
"""

import pygame
# чтобы подгружать шрифты, необходимо их инициализировать
pygame.font.init()

# ширина, высота экрана
WIDTH, HEIGHT = 800, 600
# частота обновления кадров в секунду
FPS = 60
# цвет экрана
SCREEN_COLOR = (0, 0, 0)
# направления по осям х и y
DIRECTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# шрифт
path = pygame.font.match_font('arial')  # путь к шрифту
FONT_UI = pygame.font.Font(path, size=30)

# размер картинки в пикселях
SIZE = 32
# изображения игровых объектов
img_brick = pygame.image.load("images/block_brick.png")
img_tanks = [
    pygame.image.load("images/tank1.png"),
    pygame.image.load("images/tank2.png"),
    pygame.image.load("images/tank3.png"),
    pygame.image.load("images/tank4.png"),
    pygame.image.load("images/tank5.png"),
    pygame.image.load("images/tank6.png"),
    pygame.image.load("images/tank7.png"),
    pygame.image.load("images/tank8.png")
    ]
img_bangs = [
    pygame.image.load("images/bang1.png"),
    pygame.image.load("images/bang2.png"),
    pygame.image.load("images/bang3.png")
    ]

# изображения меню заставки
img_tank_label = pygame.image.load("images/tank_menu.png")
img_main_menu = pygame.image.load("images/main_menu.png")
