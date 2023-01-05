import pygame
from load_image import load_image

FPS = 50


class Madara(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = pygame.transform.scale(load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                           (44, 83))
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
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_jump_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_jump_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_jump_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_jump_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_jumping = False
                else:
                    clock.tick(3)
                    self.image = image_madara[self.count]

            if self.is_guarding:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_guard_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_guard_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_guard_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_guard_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]

            if self.is_walking:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_walk_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_walk_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_walk_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_walk_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_walk_5.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_walk_6.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]
                    self.rect.x += 5

            if self.is_attacking:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_attacking = False
                else:
                    clock.tick(3)
                    self.image = image_madara[self.count]

            if self.is_strong_attacking:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_5.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_7.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_9.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]

            if self.is_intro:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = self.base
                    self.is_intro = False
                else:
                    clock.tick(3)
                    self.image = image_madara[self.count]

            if self.is_losing:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_lose_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_lose_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_lose_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_lose_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_winning:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_win_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_win_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_ulting:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_ulting_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_ulting_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_ulting_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_ulting_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_ulting_5.png", colorkey=-1),
                                pygame.transform.scale(
                                    load_image("C:\Коды\pygame\data\Madara\madara_ulting_6.png", colorkey=-1),
                                    (50, 80))]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_damaged:
                image_madara = [load_image("C:\Коды\pygame\data\Madara\madara_damaged_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_damaged_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_damaged_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Madara\madara_damaged_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]
        else:
            self.image = pygame.transform.flip(self.base, True, False)
            if self.is_jumping:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_jump_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_jump_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_jump_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_jump_2.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_jumping = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_guarding:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_guard_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_guard_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_guard_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_guard_2.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]

            if self.is_walking:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_walk_6.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]
                    self.rect.x -= 5

            if self.is_attacking:
                image_madara = [
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_1.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_1.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_2.png", colorkey=-1), True,
                        False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_attack_combo1_2.png", colorkey=-1), True,
                        False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_attacking = False
                else:
                    clock.tick(3)
                    self.image = image_madara[self.count]

            if self.is_strong_attacking:
                image_madara = [pygame.transform.flip(
                    load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_1.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_2.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_3.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_4.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_5.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_7.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Madara\madara_strong_attack_9.png", colorkey=-1), True, False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]

            if self.is_intro:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_stance_1.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_intro = False
                else:
                    clock.tick(5)
                    self.image = image_madara[self.count]

            if self.is_losing:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_lose_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_lose_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_lose_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_lose_4.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_winning:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_win_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_win_2.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]

            if self.is_ulting:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_4.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_5.png", colorkey=-1),
                                          True, False),
                    pygame.transform.scale(
                        pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_ulting_6.png", colorkey=-1),
                                              True, False), (50, 80))
                ]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_madara[self.count]

            if self.is_damaged:
                image_madara = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_damaged_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_damaged_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_damaged_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Madara\madara_damaged_4.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_madara):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_madara[self.count]


class Mokuton(pygame.sprite.Sprite):
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
            image_mokuton = [load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_5.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_6.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_7.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_8.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_9.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_10.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_11.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\madara_ulting_mokuton_13.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)]
            self.count += 1
            if self.count >= len(image_mokuton):
                self.count = 0
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_mokuton[self.count]


pygame.init()
size = width, height = 860, 520
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

madara = Madara(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        madara.jump()
    elif keys[pygame.K_e]:
        madara.guard()
    elif keys[pygame.K_d]:
        madara.walk()
    elif keys[pygame.K_z]:
        madara.attack()
    elif keys[pygame.K_x]:
        madara.strong_attack()
    elif keys[pygame.K_c]:
        madara.ult()
        mokuton = Mokuton(all_sprites)
    elif keys[pygame.K_a]:
        madara.flipped()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
