import pygame
# импортируем класс пуль
from bullet import Bullet

# размер картинки в пикселях
SIZE = 32
# направления по осям х и y
DIRECTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Tank:
    def __init__(self, color, px, py, direct, key_list):
        # тип
        self.type = "tank"
        # цвет
        self.color = color
        # позиция
        self.rect = pygame.Rect(px, py, SIZE, SIZE)
        # направление
        self.direct = direct
        # скорость танка по умолчанию
        self.move_speed = 2

        # урон пули танка
        self.bullet_damage = 1
        # скорость полета пули
        self.bullet_speed = 5
        # задержка между выстрелами
        # равна 60 кадрам в секунду (FPS)
        self.shot_delay = 60
        # счетчик времени с момента выстрела
        self.shot_timer = 0

        # кнопки (влево/вправо/вверх/вниз/выстрел)
        self.key_left = key_list[0]
        self.key_right = key_list[1]
        self.key_up = key_list[2]
        self.key_down = key_list[3]
        self.key_shot = key_list[4]

    # обновление
    def update(self, keys):
        if keys[self.key_left]:
            # при нажатии влево координата по х изменяется на self.move_speed
            self.rect.x -= self.move_speed
            # направление изменяется в зависимости от нажатия клавиши
            # это индекс в DIRECTS
            self.direct = 0
        elif keys[self.key_right]:
            self.rect.x += self.move_speed
            self.direct = 1
        elif keys[self.key_up]:
            self.rect.y -= self.move_speed
            self.direct = 2
        elif keys[self.key_down]:
            self.rect.y += self.move_speed
            self.direct = 3
            # print("move")
        # стрельба происходит независимо от передвижения танка
        if keys[self.key_shot] and self.shot_timer == 0:
            # print("shot")
            # dx, dy - направление полета пули
            # оно совпадает с напралением дула танка
            dx = DIRECTS[self.direct][0] * self.bullet_speed
            dy = DIRECTS[self.direct][1] * self.bullet_speed
            Bullet(self, self.rect.centerx + 1, self.rect.centery + 1,
                   dx, dy, self.bullet_damage)
            # print(dx, dy)
            # после выстрела меняем значение счетчика времени
            self.shot_timer = self.shot_delay

        # если выстрел произведен, то уменьшаем параметр счетчика
        # в итоге он должен обнулиться, чтобы производить новый выстрел
        if self.shot_timer:
            self.shot_timer -= 1

    # метод отрисовки на экране, экран передаем извне
    def draw(self, screen):
        pygame.draw.rect(surface=screen, color=self.color, rect=self.rect)

        # отрисовываем дуло, которое будет поворачиваться в зависимости от направления
        x, width = self.rect.centerx, DIRECTS[self.direct][0] * 30
        y, height = self.rect.centery, DIRECTS[self.direct][1] * 30
        pygame.draw.line(surface=screen, color="white",
                         start_pos=(x, y), end_pos=(x + width, y + height),
                         width=2)
