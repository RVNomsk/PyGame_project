"""
В данном файле реализован главный игровой цикл
"""

import pygame
# подключаем класс танков
from tank import Tank
# подключаем класс блоков
from block import Block
# модуль интерфейса
from ui import UI
# импортируем метку
from label import Label

from lists_of_objects import objects, bullets

from random import randint

# импортируем ширину и высоту экрана,
# частоту обновления кадров и цвет экрана
from settings import WIDTH, HEIGHT, FPS, SCREEN_COLOR, SIZE, img_main_menu

# инициализация
pygame.init()

# создадим игровое окно
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
# создадим экземпляр класса Clock для учета времени
clock = pygame.time.Clock()


def start():
    # создадим метку
    Label(100, 200)

    # основной игровой цикл
    running = True
    while running:
        # отрисовка экрана на каждой итерации
        screen.blit(img_main_menu, (0, 0))
        # отобразим надпись
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Для продолжения нажмите SPACE",
                                   True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, int(0.8 * HEIGHT)))
        screen.blit(text_surface, text_rect)

        # перебираем все события в основновном цикле
        for event in pygame.event.get():
            # если нажать на закрытие окна
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        # если нажать на SPACE, то запускается игра
        if keys[pygame.K_SPACE]:
            game()
            running = False

        pygame.display.update()
        # будем применять двойную буферизацию
        pygame.display.flip()


def game():
    # создадим пару танков
    tank1 = Tank(color="blue",
                 px=100,
                 py=130,
                 direct=0,
                 key_list=(pygame.K_LEFT,
                           pygame.K_RIGHT,
                           pygame.K_UP,
                           pygame.K_DOWN,
                           pygame.K_SPACE))

    tank2 = Tank(color="red",
                 px=600,
                 py=130,
                 direct=0,
                 key_list=(pygame.K_a,
                           pygame.K_d,
                           pygame.K_w,
                           pygame.K_s,
                           pygame.K_v))
    # objects += [tank1, tank2]

    # создадим интерфейс
    ui = UI()

    # функция расстановки блоков
    def create_blocks(count_of_blocks):
        for _ in range(count_of_blocks):
            # будем генерировать координаты до тех пор, пока
            # блоки не будут наслаиваться друг на друга
            while True:
                x = randint(0, WIDTH // SIZE - 1) * SIZE
                # нулевой ряд по оси Oy задействуется под интерфейс информации в игре
                y = randint(1, HEIGHT // SIZE - 1) * SIZE
                rect = pygame.Rect(x, y, SIZE, SIZE)

                # проверим, что блок не накладывается ни на какие объекты
                can_create = True
                for obj in objects:
                    if rect.colliderect(obj.rect):
                        can_create = False
                if can_create:
                    break

            # создадим блок
            Block(x, y, SIZE)

    create_blocks(150)

    # основной игровой цикл
    running = True
    while running:
        # отрисовка экрана на каждой итерации
        screen.fill(SCREEN_COLOR)

        # перебираем все события в основновном цикле
        for event in pygame.event.get():
            # если нажать на закрытие окна
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # перехват кода нажатой кнопки
        keys = pygame.key.get_pressed()

        # обновляем список всех пуль
        for bullet in bullets:
            bullet.update()

        # обновляем список всех объектов игры
        # подсчитаем, сколько танков до сих пор в игре
        tank_count = 0
        for obj in objects:
            if obj.type == 'tank' or obj.type == 'label':
                obj.update(keys)
            elif obj.type == 'block':
                obj.update()
            elif obj.type == 'bang':
                obj.update()
            if obj.type == 'tank':
                tank_count += 1
        if tank_count < 2:
            running = False
            end_game()

        # обновляем интерфейс
        ui.update()

        # отрисовка пуль
        for bullet in bullets:
            bullet.draw(screen)

        # отрисовываем все объекты
        for obj in objects:
            obj.draw(screen)

        # отрисовка интерфейса (в конце сцены!)
        ui.draw(screen)

        pygame.display.update()
        # будем применять двойную буферизацию
        pygame.display.flip()
        # метод возвращает количество миллисекунд, прошедших с момента последнего вызова
        clock.tick(FPS)


def end_game():
    # основной игровой цикл
    running = True
    while running:
        # отрисовка экрана на каждой итерации
        screen.fill(SCREEN_COLOR)

        # отобразим надпись THE END
        font = pygame.font.Font(None, 50)
        text_surface = font.render("ИГРА ЗАВЕРШЕНА",
                                   True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        # перебираем все события в основновном цикле
        for event in pygame.event.get():
            # если нажать на закрытие окна
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        pygame.display.update()
        # будем применять двойную буферизацию
        pygame.display.flip()
        # метод возвращает количество миллисекунд, прошедших с момента последнего вызова
        clock.tick(FPS)


if __name__ == "__main__":
    start()
