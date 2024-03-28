import pygame
# подключаем класс танков
from tank import Tank
# подключаем класс блоков
from block import Block

from lists_of_objects import objects, bullets

from random import randint

# импортируем ширину и высоту экрана,
# частоту обновления кадров и цвет экрана
from settings import WIDTH, HEIGHT, FPS, SCREEN_COLOR, SIZE

# инициализация
pygame.init()

# создадим игровое окно
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
# создадим экземпляр класса Clock для учета времени
clock = pygame.time.Clock()

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


# функция расстановки блоков
def create_blocks(count_of_blocks):
    for _ in range(count_of_blocks):
        # будем генерировать координаты до тех пор, пока
        # блоки не будут наслаиваться друг на друга
        while True:
            x = randint(0, WIDTH // SIZE - 1) * SIZE
            y = randint(0, HEIGHT // SIZE - 1) * SIZE
            rect = pygame.Rect(x, y, SIZE, SIZE)

            # проверим, что блок не накладывается ни
            # на какие объекты
            can_create = True
            for obj in objects:
                if rect.colliderect(obj.rect):
                    can_create = False
            if can_create:
                break

        # создадим блок
        Block(x, y, SIZE)


create_blocks(50)


# основной игровой цикл
running = True
while running:
    # перебираем все события в основновном цикле
    for event in pygame.event.get():
        # если начать на закрытие окна
        if event.type == pygame.QUIT:
            play = False

    # перехват кода нажатой кнопки
    keys = pygame.key.get_pressed()

    # обновляем список всех пуль
    for bullet in bullets:
        bullet.update()

    # обновляем список всех объектов игры
    for obj in objects:
        if obj.type == 'tank':
            obj.update(keys)
        elif obj.type == 'block':
            obj.update()

    # отрисовка экрана на каждой итерации
    screen.fill(SCREEN_COLOR)

    # отрисовка пуль
    for bullet in bullets:
        bullet.draw(screen)

    # отрисовываем все объекты
    for obj in objects:
        obj.draw(screen)

    pygame.display.update()
    # будем применять двойную буферизацию
    pygame.display.flip()
    # метод возвращает количество миллисекунд, прошедших с момента последнего вызова
    clock.tick(FPS)
pygame.quit()
