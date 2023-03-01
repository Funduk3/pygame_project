import pygame
from load_image import load_image
from Character_main import MainCharacter

FPS = 50


class Dio(MainCharacter):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("dio_stance.png", hero_name='Dio', colorkey=-1)
        self.image = self.base

        self.images = {
            0: {'base': load_image("dio_stance.png", hero_name='Dio', colorkey=-1),

                'jump': [load_image('dio_jump_1.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_jump_2.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_jump_3.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_jump_4.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_jump_5.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_jump_5.png', hero_name='Dio', colorkey=-1)],

                'guard': [load_image('dio_guard_1.png', hero_name='Dio', colorkey=-1),
                          load_image('dio_guard_2.png', hero_name='Dio', colorkey=-1),
                          load_image('dio_guard_3.png', hero_name='Dio', colorkey=-1),
                          load_image('dio_guard_4.png', hero_name='Dio', colorkey=-1)],

                'walk': [load_image('dio_walking_1.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_walking_2.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_walking_3.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_walking_4.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_walking_7.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_walking_8.png', hero_name='Dio', colorkey=-1)],

                'intro': [load_image('dio_stance.png', hero_name='Dio', colorkey=-1),
                          load_image('dio_intro_5.png', hero_name='Dio', colorkey=-1)],

                'lose': [load_image('dio_lose_1.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_lose_2.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_lose_3.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_lose_4.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_lose_5.png', hero_name='Dio', colorkey=-1),
                         load_image('dio_lose_6.png', hero_name='Dio', colorkey=-1)],

                'win': [load_image('dio_win_1.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_win_2.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_win_3.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_win_4.png', hero_name='Dio', colorkey=-1)],

                'ult': [load_image('dio_ult_1.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_ult_1.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_ult_1.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', colorkey=-1)],

                'damaged': [load_image('dio_damaged_1.png', hero_name='Dio', colorkey=-1),
                            load_image('dio_damaged_3.png', hero_name='Dio', colorkey=-1)]},

            1: {'base': load_image("dio_stance.png", hero_name='Dio', flipped=1, colorkey=-1),

                'jump': [load_image('dio_jump_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_jump_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_jump_3.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_jump_4.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_jump_5.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_jump_5.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'guard': [load_image('dio_guard_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                          load_image('dio_guard_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                          load_image('dio_guard_3.png', hero_name='Dio', flipped=1, colorkey=-1),
                          load_image('dio_guard_4.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'walk': [load_image('dio_walking_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_walking_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_walking_3.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_walking_4.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_walking_7.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_walking_8.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'intro': [load_image('dio_stance.png', hero_name='Dio', flipped=1, colorkey=-1),
                          load_image('dio_intro_5.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'lose': [load_image('dio_lose_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_lose_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_lose_3.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_lose_4.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_lose_5.png', hero_name='Dio', flipped=1, colorkey=-1),
                         load_image('dio_lose_6.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'win': [load_image('dio_win_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_win_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_win_3.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_win_4.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'ult': [load_image('dio_ult_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_ult_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_ult_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', flipped=1, colorkey=-1),
                        load_image('dio_ult_2.png', hero_name='Dio', flipped=1, colorkey=-1)],

                'damaged': [load_image('dio_damaged_1.png', hero_name='Dio', flipped=1, colorkey=-1),
                            load_image('dio_damaged_3.png', hero_name='Dio', flipped=1, colorkey=-1)]}
        }


class TheWorld(Dio, pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("empty.png", colorkey=-1)
        self.base = load_image("empty.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.is_ulting = False
        self.is_attacking = False
        self.is_strong_attacking = False
        self.is_standing = False
        self.flag = False
        self.is_walking = False
        self.is_flipped_theworld = False

        self.count = -1

        self.images = {
            0: {'base': load_image("Theworld_stance.png", hero_name='Dio', colorkey=-1),

                'attack': [load_image("Theworld_attack_1.png", hero_name='Dio', colorkey=-1),
                           load_image("Theworld_attack_2.png", hero_name='Dio', colorkey=-1),
                           load_image("Theworld_attack_3.png", hero_name='Dio', colorkey=-1),
                           load_image("Theworld_attack_4.png", hero_name='Dio', colorkey=-1)],

                'strong_attack': [load_image("Theworld_strong_attack_1.png", hero_name='Dio', colorkey=-1),
                                  load_image("Theworld_strong_attack_2.png", hero_name='Dio', colorkey=-1),
                                  load_image("Theworld_strong_attack_2.png", hero_name='Dio', colorkey=-1),
                                  load_image("Theworld_strong_attack_3.png", hero_name='Dio', colorkey=-1),
                                  load_image("Theworld_strong_attack_3.png", hero_name='Dio', colorkey=-1),
                                  load_image("Theworld_strong_attack_4.png", hero_name='Dio', colorkey=-1)],
                'ult': [load_image("Theworld_ult_1.png", hero_name='Dio', colorkey=-1),
                        load_image("Theworld_ult_1.png", hero_name='Dio', colorkey=-1),
                        load_image("Theworld_ult_1.png", hero_name='Dio', colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', colorkey=-1)]},

            1: {'base': load_image("Theworld_stance.png", hero_name='Dio', flipped=1, colorkey=-1),

                'attack': [load_image("Theworld_attack_1.png", hero_name='Dio', flipped=1, colorkey=-1),
                           load_image("Theworld_attack_2.png", hero_name='Dio', flipped=1, colorkey=-1),
                           load_image("Theworld_attack_3.png", hero_name='Dio', flipped=1, colorkey=-1),
                           load_image("Theworld_attack_4.png", hero_name='Dio', flipped=1, colorkey=-1)],

                'strong_attack': [load_image("Theworld_strong_attack_1.png", hero_name='Dio', flipped=1, colorkey=-1),
                                  load_image("Theworld_strong_attack_2.png", hero_name='Dio', flipped=1, colorkey=-1),
                                  load_image("Theworld_strong_attack_2.png", hero_name='Dio', flipped=1, colorkey=-1),
                                  load_image("Theworld_strong_attack_3.png", hero_name='Dio', flipped=1, colorkey=-1),
                                  load_image("Theworld_strong_attack_3.png", hero_name='Dio', flipped=1, colorkey=-1),
                                  load_image("Theworld_strong_attack_4.png", hero_name='Dio', flipped=1, colorkey=-1)],
                'ult': [load_image("Theworld_ult_1.png", hero_name='Dio', flipped=1, colorkey=-1),
                        load_image("Theworld_ult_1.png", hero_name='Dio', flipped=1, colorkey=-1),
                        load_image("Theworld_ult_1.png", hero_name='Dio', flipped=1, colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', flipped=1, colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', flipped=1, colorkey=-1),
                        load_image("Theworld_ult_2.png", hero_name='Dio', flipped=1, colorkey=-1)]}
        }

    def ult(self):
        self.is_ulting = True

    def attack(self):
        self.is_attacking = True

    def strong_attack(self):
        self.is_strong_attacking = True

    def walk(self):
        self.is_walking = True

    def update(self):
        if self.is_ulting:
            if not self.is_flipped:
                image_theworld = self.images[0]['ult']
            else:
                image_theworld = self.images[1]['ult']
            self.count += 1
            if self.count >= len(image_theworld):
                self.count = 0
                self.image = self.base
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_theworld[self.count]

        if self.is_attacking:
            if not self.is_flipped:
                image_theworld = self.images[0]['attack']
            else:
                image_theworld = self.images[1]['attack']
            self.count += 1
            if self.count >= len(image_theworld):
                self.count = 0
                self.image = self.base
                self.is_attacking = False
            else:
                clock.tick(5)
                self.image = image_theworld[self.count]

        if self.is_strong_attacking:
            if not self.is_flipped:
                image_theworld = self.images[0]['strong_attack']
            else:
                image_theworld = self.images[1]['strong_attack']
            self.count += 1
            if self.count >= len(image_theworld):
                self.count = 0
                self.image = self.base
                self.is_strong_attacking = False
            else:
                clock.tick(5)
                self.image = image_theworld[self.count]

        if self.is_walking:
            if not self.is_flipped:
                self.rect.x += 15
                self.is_walking = False
            else:
                self.rect.x -= 15
                self.is_walking = False


if __name__ == '__main__':

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
