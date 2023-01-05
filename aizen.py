import pygame
from load_image import load_image

FPS = 50


class Aizen(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("C:\Коды\pygame\data\Aizen\Aizen_stance.png", colorkey=-1)
        self.image = self.base
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.count = -1
        self.is_jumping = False
        self.is_guarding = False
        self.is_walking = False
        self.is_attacking = False
        self.is_strong_attacking = False
        self.is_intro = False
        self.is_losing = False
        self.is_winning = False
        self.is_ulting = False
        self.is_damaged = False
        self.is_flipped = False
        self.rect = self.image.get_rect()

    def jump(self):
        self.is_jumping = True

    def guard(self):
        self.is_guarding = True

    def walk(self):
        self.is_walking = True

    def attack(self):
        self.is_attacking = True

    def strong_attack(self):
        self.is_strong_attacking = True

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
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_4.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_5.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_6.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_7.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_8.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_jumping = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_guarding:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]

            if self.is_walking:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]
                    self.rect.x += 5

            if self.is_attacking:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_attacking = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_strong_attacking:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_4.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_5.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_6.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_7.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_strong_attacking = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_intro:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_1.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = self.base
                    self.is_intro = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]

            if self.is_losing:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_lose_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_lose_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_winning:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_win_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_4.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_5.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_6.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_7.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_8.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_9.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_win_10.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_ulting:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_1.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_2.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_3.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_4.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_5.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_6.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_7.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_8.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_9.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_10.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_11.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_12.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_13.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_14.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_15.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_16.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_17.png", colorkey=-1)
                               ]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_damaged:
                image_aizen = [load_image("C:\Коды\pygame\data\Aizen\Aizen_damaged.png", colorkey=-1),
                               load_image("C:\Коды\pygame\data\Aizen\Aizen_damaged.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]
        else:
            self.image = pygame.transform.flip(self.base, True, False)
            if self.is_jumping:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_6.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_7.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_jump_7.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_jumping = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_guarding:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_guard_4.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]

            if self.is_walking:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_walk_2.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]
                    self.rect.x -= 5

            if self.is_attacking:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_attack_4.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_attacking = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_strong_attacking:
                image_aizen = [pygame.transform.flip(
                    load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_1.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_2.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_3.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_4.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_5.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_6.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Aizen\Aizen_strong_attack_7.png", colorkey=-1), True,
                        False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_strong_attacking = False
                else:
                    clock.tick(10)
                    self.image = image_aizen[self.count]

            if self.is_intro:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_intro_1.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_intro = False
                else:
                    clock.tick(5)
                    self.image = image_aizen[self.count]

            if self.is_losing:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_lose_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_lose_2.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_winning:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_6.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_7.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_8.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_9.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_win_10.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_ulting:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_6.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_7.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_8.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_9.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_10.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_11.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_12.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_13.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_14.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_15.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_16.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_first_17.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]

            if self.is_damaged:
                image_aizen = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_damaged.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Aizen\Aizen_damaged.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_aizen):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_aizen[self.count]


class AizenUlt(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 0
        self.is_ulting = True
        self.count = -1

    def update(self):
        if self.is_ulting:
            image_ult = [load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_1.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_2.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_3.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_4.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_5.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_6.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_7.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Aizen\Aizen_ult_8.png", colorkey=-1),
                         load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)]
            self.count += 1
            if self.count >= len(image_ult):
                self.count = 0
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_ult[self.count]


pygame.init()
size = width, height = 860, 520
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

aizen = Aizen(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        aizen.jump()
    elif keys[pygame.K_e]:
        aizen.guard()
    elif keys[pygame.K_d]:
        aizen.walk()
    elif keys[pygame.K_z]:
        aizen.attack()
    elif keys[pygame.K_x]:
        aizen.strong_attack()
    elif keys[pygame.K_c]:
        aizen.ult()
        aizenult = AizenUlt(all_sprites)
    elif keys[pygame.K_a]:
        aizen.flipped()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
