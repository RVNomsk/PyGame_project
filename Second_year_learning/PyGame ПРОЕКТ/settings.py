import pygame
# чтобы подгружать шрифты, необходимо их инициализировать
pygame.font.init()

# ширина, высота экрана
WIDTH, HEIGHT = 800, 600
# частота обновления кадров в секунду
FPS = 60
# цвет экрана
SCREEN_COLOR = (0, 0, 0)
# размер картинки в пикселях
SIZE = 32
# направления по осям х и y
DIRECTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# шрифт
path = pygame.font.match_font('arial')  # путь к шрифту
FONT_UI = pygame.font.Font(path, size=30)
