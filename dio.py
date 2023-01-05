import pygame
from load_image import load_image

FPS = 50


class Dio(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("C:\Коды\pygame\data\Dio\dio_stance.png", colorkey=-1)
        self.image = self.base
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.count = -1
        self.is_stand = False
        self.is_jumping = False
        self.is_guarding = False
        self.is_walking = False
        self.is_intro = False
        self.is_losing = False
        self.is_winning = False
        self.is_ulting = False
        self.is_damaged = False
        self.is_flipped = False
        self.rect = self.image.get_rect()

    def stand(self):
        self.is_stand = True

    def jump(self):
        self.is_jumping = True

    def guard(self):
        self.is_guarding = True

    def walk(self):
        self.is_walking = True

    def intro(self):
        self.is_intro = True

    def lose(self):
        self.is_losing = True

    def win(self):
        self.is_winning = True

    def ult(self):
        self.is_ulting = True

    def damaged(self):
        self.is_damaged = True

    def flipped(self):
        if not self.is_flipped:
            self.is_flipped = True
            print(0)
        elif self.is_flipped:
            self.is_flipped = False
            print(1)

    def update(self, *args, **kwargs):
        if not self.is_flipped:
            if self.is_jumping:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_jump_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_jump_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_jump_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_jump_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_jump_5.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_jumping = False
                else:
                    clock.tick(3)
                    self.image = image_dio[self.count]

            if self.is_guarding:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_guard_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_guard_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_guard_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_guard_3.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_dio[self.count]

            if self.is_walking:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_walking_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_5.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_6.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_7.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_walking_8.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_dio[self.count]
                    self.rect.x += 5

            if self.is_intro:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_intro_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_intro_2.jpg", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_intro_3.jpg", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_intro_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_intro_5.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_intro = False
                else:
                    clock.tick(3)
                    self.image = image_dio[self.count]

            if self.is_losing:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_lose_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_lose_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_lose_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_lose_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_lose_5.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_lose_6.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]

            if self.is_winning:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_win_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_win_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_win_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_win_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]

            if self.is_ulting:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_ult_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_ult_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_ult_3.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_dio[self.count]

            if self.is_damaged:
                image_dio = [load_image("C:\Коды\pygame\data\Dio\dio_damaged_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_damaged_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Dio\dio_damaged_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]
        else:
            self.image = pygame.transform.flip(self.base, True, False)
            if self.is_jumping:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_jump_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_jump_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_jump_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_jump_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_jump_5.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_jumping = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]

            if self.is_guarding:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_guard_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_guard_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_guard_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_guard_4.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_dio[self.count]

            if self.is_walking:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_6.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_7.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_walking_8.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_dio[self.count]
                    self.rect.x -= 5

            if self.is_losing:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_lose_6.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]

            if self.is_winning:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_win_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_win_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_win_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_win_4.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]

            if self.is_ulting:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_ult_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_ult_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_ult_3.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.image = self.base
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_dio[self.count]

            if self.is_damaged:
                image_dio = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_damaged_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_damaged_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\dio_damaged_4.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_dio):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_dio[self.count]


class TheWorld(Dio, pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)
        self.base = load_image("C:\Коды\pygame\data\Dio\Theworld_stance.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = dio.rect.x + 50
        self.rect.y = 0
        self.is_ulting = False
        self.is_attacking = False
        self.is_strong_attacking = False
        self.is_standing = False
        self.flag = False
        self.is_walking = False
        self.is_flipped_theworld = False

        self.count = -1

    def stand(self):
        self.is_standing = True

    def ult(self):
        self.is_ulting = True

    def attack(self):
        self.is_attacking = True

    def strong_attack(self):
        self.is_strong_attacking = True

    def walk(self):
        self.is_walking = True

    def update(self):
        if not self.is_flipped:
            if self.is_standing:
                self.image = self.base

            if self.is_ulting:
                image_theworld = [load_image("C:\Коды\pygame\data\Dio\Theworld_ult_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_ult_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_ult_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_theworld[self.count]

            if self.is_attacking:
                image_theworld = [load_image("C:\Коды\pygame\data\Dio\Theworld_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_attack_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_theworld[self.count]

            if self.is_strong_attacking:
                image_theworld = [load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_theworld[self.count]

            if self.is_walking:
                for i in range(8):
                    self.rect.x += 5
                self.is_walking = False
        else:
            self.base = pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_stance.png", colorkey=-1), True, False)

            if self.is_standing:
                self.image = self.base

            if self.is_ulting:
                image_theworld = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_ult_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_ult_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_ult_2.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_theworld[self.count]

            if self.is_attacking:
                image_theworld = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_attack_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_attack_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_attack_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Dio\Theworld_attack_4.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_theworld[self.count]

            if self.is_strong_attacking:
                image_theworld = [pygame.transform.flip(
                    load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_1.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_2.png", colorkey=-1),
                        True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_3.png", colorkey=-1),
                        True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Dio\Theworld_strong_attack_4.png", colorkey=-1),
                        True, False)]
                self.count += 1
                if self.count >= len(image_theworld):
                    self.count = 0
                    self.image = self.base
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_theworld[self.count]

            if self.is_walking:
                for i in range(9):
                    self.rect.x += 5
                self.is_walking = False


pygame.init()
size = width, height = 860, 520
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

dio = Dio(all_sprites)
theworld = TheWorld(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        dio.jump()
    elif keys[pygame.K_e]:
        dio.guard()
    elif keys[pygame.K_q]:
        theworld.stand()
    elif keys[pygame.K_d]:
        dio.walk()
        theworld.walk()
    elif keys[pygame.K_z]:
        theworld.attack()
    elif keys[pygame.K_x]:
        theworld.strong_attack()
    elif keys[pygame.K_c]:
        dio.ult()
        theworld.ult()
    elif keys[pygame.K_a]:
        dio.flipped()
        theworld.flipped()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
