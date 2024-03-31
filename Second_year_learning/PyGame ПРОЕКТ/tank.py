"""
Данный класс предназначен для создания модели танка и управления им
"""


import pygame
# импортируем класс пуль
from bullet import Bullet

from lists_of_objects import objects, bullets

# импорт размера танка и направления
from settings import SIZE, DIRECTS, WIDTH, HEIGHT, img_tanks


class Tank:
    def __init__(self, color, px, py, direct, key_list):
        # добавим танк в список объектов
        objects.append(self)
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
        # здоровье танка
        self.hp = 5
        # уровень мощности танка (меняется,
        # когда танк улучшает характеристики)
        self.rank = 0
        # в зависимости от направления танка картинка
        # должна поворачиваться
        self.image = pygame.transform.rotate(img_tanks[self.rank], (self.direct + 1) * 90)
        # область привязки картинки танка
        # self.img_rect = self.image.get_rect(center=self.rect.center)

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
        # танк не должен наезжать на стену и другой танк
        # если танк столкнулся с другим объектом, то возвращаем
        # его координаты на прежнюю позицию
        x_before, y_before = self.rect.topleft

        if keys[self.key_left]:
            # при нажатии влево координата по х изменяется на self.move_speed
            self.rect.x -= self.move_speed
            # направление изменяется в зависимости от нажатия клавиши
            # это индекс в DIRECTS
            self.direct = 0
            # поворот танка
            self.image = pygame.transform.rotate(img_tanks[self.rank], (-self.direct + 1) * 90)
        elif keys[self.key_right]:
            self.rect.x += self.move_speed
            self.direct = 1
            # поворот танка
            self.image = pygame.transform.rotate(img_tanks[self.rank], -self.direct * 90)
        elif keys[self.key_up]:
            self.rect.y -= self.move_speed
            self.direct = 2
            # поворот танка
            self.image = pygame.transform.rotate(img_tanks[self.rank], (self.direct + 2) * 90)
        elif keys[self.key_down]:
            self.rect.y += self.move_speed
            self.direct = 3
            # поворот танка
            self.image = pygame.transform.rotate(img_tanks[self.rank], (self.direct - 1) * 90)
            # print("move")
        # сожмем немного картинку, т.к. размеры танка немного меньше размеров картинки
        # self.image = self.image.convert_alpha()
        # print(type(self.image))
        # print(self.image.get_width(), self.image.get_height())
        # self.image = pygame.transform.scale(self.image,
        #                                     size=(self.image.get_width() - 2, self.image.get_height() - 2))
        # self.img_rect = self.image.get_rect(center=self.rect.center)

        # ограничение движения танка
        for obj in objects:
            # 0 + 30, чтобы не наезжать на поле информации
            if obj is not self and self.rect.colliderect(obj.rect) \
                    or not (0 <= self.rect.x <= WIDTH - SIZE) or not (0 + 30 <= self.rect.y <= HEIGHT - SIZE):
                self.rect.topleft = x_before, y_before
                # print(self.rect.x, WIDTH, self.rect.y, HEIGHT)

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
        #
        # pygame.draw.rect(surface=screen, color=self.color, rect=self.rect)
        #
        # # отрисовываем дуло, которое будет поворачиваться в зависимости от направления
        # x, width = self.rect.centerx, DIRECTS[self.direct][0] * 30
        # y, height = self.rect.centery, DIRECTS[self.direct][1] * 30
        # pygame.draw.line(surface=screen, color="white",
        #                  start_pos=(x, y), end_pos=(x + width, y + height),
        #                  width=2)

        screen.blit(self.image, self.rect)

    # метод уменьшения здоровья при попадании пули
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
            print(self.color, "dead")
