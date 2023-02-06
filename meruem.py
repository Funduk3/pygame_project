import pygame
from load_image import load_image
from Character_main import MainCharacter

FPS = 50


class Meruem(MainCharacter):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("meruem_stance.png", hero_name='Meruem', colorkey=-1)
        self.image = self.base

        self.images = {
            0: {'base': load_image("meruem_stance.png", hero_name='Meruem', colorkey=-1),

                'jump': [load_image('meruem_jump_1.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_jump_2.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_jump_4.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_jump_5.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_jump_7.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_jump_8.png', hero_name='Meruem', colorkey=-1)],

                'guard': [load_image('meruem_guard_1.png', hero_name='Meruem', colorkey=-1),
                          load_image('meruem_guard_1.png', hero_name='Meruem', colorkey=-1),
                          load_image('meruem_guard_2.png', hero_name='Meruem', colorkey=-1),
                          load_image('meruem_guard_2.png', hero_name='Meruem', colorkey=-1)],

                'walk': [load_image('meruem_walk_1.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_walk_2.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_walk_2.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_walk_3.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_walk_3.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_walk_4.png', hero_name='Meruem', colorkey=-1)],

                'attack': [load_image('meruem_attack_1.png', hero_name='Meruem', colorkey=-1),
                           load_image('meruem_attack_2.png', hero_name='Meruem', colorkey=-1),
                           load_image('meruem_attack_3.png', hero_name='Meruem', colorkey=-1),
                           load_image('meruem_attack_4.png', hero_name='Meruem', colorkey=-1)],

                'strong_attack': [load_image('meruem_strong_attack_1.png', hero_name='Meruem', colorkey=-1),
                                  load_image('meruem_strong_attack_1.png', hero_name='Meruem', colorkey=-1),
                                  load_image('meruem_strong_attack_2.png', hero_name='Meruem', colorkey=-1),
                                  load_image('meruem_strong_attack_2.png', hero_name='Meruem', colorkey=-1),
                                  load_image('meruem_strong_attack_3.png', hero_name='Meruem', colorkey=-1),
                                  load_image('meruem_strong_attack_3.png', hero_name='Meruem', colorkey=-1)],

                'intro': [load_image('meruem_stance.png', hero_name='Meruem', colorkey=-1),
                          load_image('meruem_stance.png', hero_name='Meruem', colorkey=-1),
                          load_image('meruem_stance.png', hero_name='Meruem', colorkey=-1)],

                'lose': [load_image('meruem_lose_1.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_lose_2.png', hero_name='Meruem', colorkey=-1),
                         load_image('meruem_lose_3.png', hero_name='Meruem', colorkey=-1)],

                'win': [load_image('meruem_win_1.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_win_2.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_win_3.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_win_4.png', hero_name='Meruem', colorkey=-1)],

                'ult': [load_image('meruem_ult_1.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_2.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_3.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_4.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_5.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_6.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_7.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_8.png', hero_name='Meruem', colorkey=-1),
                        load_image('meruem_ult_9.png', hero_name='Meruem', colorkey=-1)],

                'damaged': [load_image('meruem_damaged_2.png', hero_name='Meruem', colorkey=-1),
                            load_image('meruem_damaged_3.png', hero_name='Meruem', colorkey=-1)]},

            1: {'base': load_image("meruem_stance.png", hero_name='Meruem', flipped=1, colorkey=-1),

                'jump': [load_image('meruem_jump_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_jump_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_jump_4.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_jump_5.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_jump_7.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_jump_8.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'guard': [load_image('meruem_guard_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                          load_image('meruem_guard_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                          load_image('meruem_guard_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                          load_image('meruem_guard_2.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'walk': [load_image('meruem_walk_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_walk_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_walk_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_walk_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_walk_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_walk_4.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'attack': [load_image('meruem_attack_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                           load_image('meruem_attack_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                           load_image('meruem_attack_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                           load_image('meruem_attack_4.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'strong_attack': [load_image('meruem_strong_attack_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                                  load_image('meruem_strong_attack_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                                  load_image('meruem_strong_attack_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                                  load_image('meruem_strong_attack_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                                  load_image('meruem_strong_attack_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                                  load_image('meruem_strong_attack_3.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'intro': [load_image('meruem_stance.png', hero_name='Meruem', flipped=1, colorkey=-1),
                          load_image('meruem_stance.png', hero_name='Meruem', flipped=1, colorkey=-1),
                          load_image('meruem_stance.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'lose': [load_image('meruem_lose_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_lose_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                         load_image('meruem_lose_3.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'win': [load_image('meruem_win_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_win_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_win_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_win_4.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'ult': [load_image('meruem_ult_1.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_3.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_4.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_5.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_6.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_7.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_8.png', hero_name='Meruem', flipped=1, colorkey=-1),
                        load_image('meruem_ult_9.png', hero_name='Meruem', flipped=1, colorkey=-1)],

                'damaged': [load_image('meruem_damaged_2.png', hero_name='Meruem', flipped=1, colorkey=-1),
                            load_image('meruem_damaged_3.png', hero_name='Meruem', flipped=1, colorkey=-1)]}
        }


class MeruemUlt(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("empty.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 0
        self.is_ulting = True
        self.count = -1

    def update(self):
        if self.is_ulting:
            image_ult = [load_image("meruem_ult_charge_1.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_2.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_3.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_4.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_5.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_6.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_7.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_8.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_9.png", hero_name='Meruem', colorkey=-1),
                         load_image("meruem_ult_charge_10.png", hero_name='Meruem', colorkey=-1),
                         load_image("empty.png", colorkey=-1)]
            self.count += 1
            if self.count >= len(image_ult):
                self.count = 0
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_ult[self.count]
                if self.count >= 4:
                    self.rect.x += 50


if __name__ == '__main__':
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
            meruemult = MeruemUlt(all_sprites)
        elif keys[pygame.K_a]:
            meruem.flipped()

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
