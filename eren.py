import pygame
from load_image import load_image

FPS = 50


class Eren(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("C:\Коды\pygame\data\Eren\Eren_stance_3.png", colorkey=-1)
        self.titan_base = load_image("C:\Коды\pygame\data\Eren\Titan_stance_1.png", colorkey=-1)
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
        self.is_titan = False
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
        self.is_titan = True

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
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_jump_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_jump_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_jump_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_jump_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_jump_5.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_jump_6.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.base
                        self.is_jumping = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_3.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_jumping = False
                    else:
                        clock.tick(3)
                        self.image = image_eren[self.count]

            if self.is_guarding:
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_guard_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_guard_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_guard_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_guard_2.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.base
                        self.is_guarding = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_guarding = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]

            if self.is_walking:
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_walk_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_walk_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_walk_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_walk_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_walk_5.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_walk_6.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                        self.rect.x += 5
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_walk_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_5.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_6.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_7.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_8.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_walk_9.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                        self.rect.x += 5

            if self.is_attacking:
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_attack_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_attack_5.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.base
                        self.is_attacking = False
                    else:
                        clock.tick(3)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_attack_4.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_attacking = False
                    else:
                        clock.tick(3)
                        self.image = image_eren[self.count]

            if self.is_strong_attacking:
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_5.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.base
                        self.is_strong_attacking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_2.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_3.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_4.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_5.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_strong_attacking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]

            if self.is_intro:
                image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_intro_1.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_2.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_3.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_4.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_5.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_6.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_intro_7.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.image = self.base
                    self.is_intro = False
                else:
                    clock.tick(3)
                    self.image = image_eren[self.count]

            if self.is_losing:
                image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_lose_1.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_lose_2.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_lose_3.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_lose_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_eren[self.count]

            if self.is_winning:
                image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_win_1.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_win_2.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_win_3.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_win_4.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_win_5.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_win_6.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_eren[self.count]

            if self.is_ulting:
                image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_ult_1.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_2.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_3.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_4.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_5.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_6.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_7.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_8.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Eren_ult_9.png", colorkey=-1),
                              load_image("C:\Коды\pygame\data\Eren\Titan_stance_1.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_titan = True
                    self.is_ulting = False
                else:
                    clock.tick(4)
                    self.image = image_eren[self.count]

            if self.is_damaged:
                if not self.is_titan:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Eren_damaged_1.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Eren_damaged_2.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.is_damaged = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [load_image("C:\Коды\pygame\data\Eren\Titan_damaged.png", colorkey=-1),
                                  load_image("C:\Коды\pygame\data\Eren\Titan_damaged.png", colorkey=-1)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = self.titan_base
                        self.is_damaged = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]

        else:
            if not self.is_titan:
                self.image = pygame.transform.flip(self.base, True, False)
            else:
                self.image = pygame.transform.flip(self.titan_base, True, False)
            if self.is_jumping:
                if not self.is_titan:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_1.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_2.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_3.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_4.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_5.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_jump_6.png", colorkey=-1), True,
                                              False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.base, True, False)
                        self.is_jumping = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_1.png", colorkey=-1), True,
                            False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_1.png", colorkey=-1), True,
                            False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_2.png", colorkey=-1), True,
                            False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_2.png", colorkey=-1), True,
                            False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_3.png", colorkey=-1), True,
                            False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_leg_attack_3.png", colorkey=-1), True,
                            False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.titan_base, True, False)
                        self.is_jumping = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]

            if self.is_guarding:
                if not self.is_titan:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_guard_1.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_guard_1.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_guard_2.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_guard_2.png", colorkey=-1),
                                              True, False)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.base, True, False)
                        self.is_guarding = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_guard.png", colorkey=-1),
                                              True, False)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.titan_base, True, False)
                        self.is_guarding = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]

            if self.is_walking:
                if not self.is_titan:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_1.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_2.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_3.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_4.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_5.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_walk_6.png", colorkey=-1), True,
                                              False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.base, True, False)
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                        self.rect.x -= 5
                else:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_1.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_2.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_3.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_4.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_5.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_6.png", colorkey=-1), True,
                                              False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_7.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_8.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_walk_9.png", colorkey=-1),
                                              True, False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.titan_base, True, False)
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                        self.rect.x -= 5

            if self.is_attacking:
                if not self.is_titan:
                    image_eren = [
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_attack_1.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_attack_2.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_attack_3.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_attack_4.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_attack_5.png", colorkey=-1), True, False),
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.base, True, False)
                        self.is_attacking = False
                    else:
                        clock.tick(3)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_attack_1.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_attack_2.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_attack_3.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_attack_4.png", colorkey=-1), True, False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.titan_base, True, False)
                        self.is_attacking = False
                    else:
                        clock.tick(3)
                        self.image = image_eren[self.count]

            if self.is_strong_attacking:
                if not self.is_titan:
                    image_eren = [pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_1.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_2.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_3.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_4.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Eren_strong_attack_5.png", colorkey=-1), True, False)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.base, True, False)
                        self.is_strong_attacking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_1.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_2.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_3.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_4.png", colorkey=-1), True, False),
                        pygame.transform.flip(
                            load_image("C:\Коды\pygame\data\Eren\Titan_strong_attack_5.png", colorkey=-1), True, False)]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.image = pygame.transform.flip(self.titan_base, True, False)
                        self.is_strong_attacking = False
                    else:
                        clock.tick(5)
                        self.image = image_eren[self.count]

            if self.is_intro:
                image_eren = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_4.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_5.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_6.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_intro_7.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.image = pygame.transform.flip(self.titan_base, True, False)
                    self.is_intro = False
                else:
                    clock.tick(5)
                    self.image = image_eren[self.count]

            if self.is_losing:
                image_eren = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_lose_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_lose_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_lose_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_lose_4.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_eren[self.count]

            if self.is_winning:
                image_eren = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_win_6.png", colorkey=-1), True,
                                          False),
                ]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_eren[self.count]

            if self.is_ulting:
                image_eren = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_4.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_5.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_6.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_7.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_8.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_ult_9.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_stance_1.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_eren):
                    self.count = 0
                    self.is_titan = True
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_eren[self.count]

            if self.is_damaged:
                if not self.is_titan:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_damaged_1.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Eren_damaged_2.png", colorkey=-1),
                                              True, False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.is_damaged = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]
                else:
                    image_eren = [
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_damaged.png", colorkey=-1),
                                              True, False),
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Eren\Titan_damaged.png", colorkey=-1),
                                              True, False)
                    ]
                    self.count += 1
                    if self.count >= len(image_eren):
                        self.count = 0
                        self.is_damaged = False
                    else:
                        clock.tick(4)
                        self.image = image_eren[self.count]


pygame.init()
size = width, height = 860, 520
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

eren = Eren(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        eren.jump()
    elif keys[pygame.K_e]:
        eren.guard()
    elif keys[pygame.K_d]:
        eren.walk()
    elif keys[pygame.K_z]:
        eren.attack()
    elif keys[pygame.K_x]:
        eren.strong_attack()
    elif keys[pygame.K_c]:
        eren.ult()
    elif keys[pygame.K_a]:
        eren.flipped()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
