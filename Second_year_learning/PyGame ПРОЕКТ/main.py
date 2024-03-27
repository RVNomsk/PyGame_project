import pygame
# подключаем класс танков
from tank import Tank
# подключаем класс пуль
from bullet import bullets, Bullet

# инициализация
pygame.init()

# ширина, высота экрана
WIDTH, HEIGHT = 800, 600
# частота обновления кадров в секунду
FPS = 60
# цвет экрана
SCREEN_COLOR = (0, 0, 0)

# создадим игровое окно
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
# создадим экземпляр класса Clock для учета времени
clock = pygame.time.Clock()



# создадим список всех объектов игры
objects = []
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
objects += [tank1, tank2]

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
        obj.update(keys)

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
