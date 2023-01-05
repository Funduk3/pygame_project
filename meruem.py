import pygame
from load_image import load_image
FPS = 50


class Meruem(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("C:\Коды\pygame\data\Meruem\meruem_stance.png", colorkey=-1)
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
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_jump_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_5.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_6.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_7.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_jump_8.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_jumping = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_guarding:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_guard_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_guard_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_guard_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_guard_2.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_walking:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_walk_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_walk_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_walk_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_walk_1.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]
                    self.rect.x += 5

            if self.is_attacking:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_attack_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_attack_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_attack_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_attack_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_attack_5.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_attacking = False
                else:
                    clock.tick(3)
                    self.image = image_meruem[self.count]

            if self.is_strong_attacking:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_3.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_intro:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_stance", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_stance", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_stance", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = self.base
                    self.is_intro = False
                else:
                    clock.tick(3)
                    self.image = image_meruem[self.count]

            if self.is_losing:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_lose_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_lose_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_lose_3.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_winning:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_win_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_win_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_win_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_win_4.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_ulting:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_ult_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_3.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_4.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_5.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_6.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_7.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_8.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_ult_9.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_damaged:
                image_meruem = [load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_1.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_2.png", colorkey=-1),
                                load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_3.png", colorkey=-1)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

        else:
            self.image = pygame.transform.flip(self.base, True, False)
            if self.is_jumping:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_4.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_5.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_6.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_7.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_jump_8.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_jumping = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_guarding:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_guard_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_guard_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_guard_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_guard_2.png", colorkey=-1),
                                          True, False)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_guarding = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_walking:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_walk_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_walk_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_walk_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_walk_4.png", colorkey=-1), True,
                                          False),
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_walking = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]
                    self.rect.x -= 5

            if self.is_attacking:
                image_meruem = [
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_attack_1.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_attack_2.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_attack_3.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_attack_4.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_attack_5.png", colorkey=-1), True, False),
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_attacking = False
                else:
                    clock.tick(3)
                    self.image = image_meruem[self.count]

            if self.is_strong_attacking:
                image_meruem = [pygame.transform.flip(
                    load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_1.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_2.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_2.png", colorkey=-1), True, False),
                    pygame.transform.flip(
                        load_image("C:\Коды\pygame\data\Meruem\meruem_strong_attack_3.png", colorkey=-1), True, False)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_strong_attacking = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_intro:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_stance.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_stance.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_stance.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.image = pygame.transform.flip(self.base, True, False)
                    self.is_intro = False
                else:
                    clock.tick(5)
                    self.image = image_meruem[self.count]

            if self.is_losing:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_lose_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_lose_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_lose_3.png", colorkey=-1), True,
                                          False)]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_losing = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_winning:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_win_1.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_win_2.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_win_3.png", colorkey=-1), True,
                                          False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_win_4.png", colorkey=-1), True,
                                          False)
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_winning = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]

            if self.is_ulting:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_3.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_4.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_5.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_6.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_7.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_8.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_ult_9.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_ulting = False
                else:
                    clock.tick(10)
                    self.image = image_meruem[self.count]

            if self.is_damaged:
                image_meruem = [
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_1.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_2.png", colorkey=-1),
                                          True, False),
                    pygame.transform.flip(load_image("C:\Коды\pygame\data\Meruem\meruem_damaged_3.png", colorkey=-1),
                                          True, False)
                ]
                self.count += 1
                if self.count >= len(image_meruem):
                    self.count = 0
                    self.is_damaged = False
                else:
                    clock.tick(4)
                    self.image = image_meruem[self.count]


class Charge(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 0
        self.is_ulting = True
        self.count = -1

    def update(self):
        if self.is_ulting:
            image_mokuton = [load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_1.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_2.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_3.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_4.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_5.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_6.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_7.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_8.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_9.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Meruem\meruem_ult_charge_10.png", colorkey=-1),
                             load_image("C:\Коды\pygame\data\Madara\empty.png", colorkey=-1)]
            self.count += 1
            if self.count >= len(image_mokuton):
                self.count = 0
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_mokuton[self.count]
                if self.count >= 4:
                    self.rect.x += 50


pygame.init()
size = width, height = 860, 520
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

meruem = Meruem(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        meruem.jump()
    elif keys[pygame.K_e]:
        meruem.guard()
    elif keys[pygame.K_d]:
        meruem.walk()
    elif keys[pygame.K_z]:
        meruem.attack()
    elif keys[pygame.K_x]:
        meruem.strong_attack()
    elif keys[pygame.K_c]:
        meruem.ult()
        charge = Charge(all_sprites)
    elif keys[pygame.K_a]:
        meruem.flipped()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
