import pygame
from load_image import load_image
from Character_main import MainCharacter

FPS = 50


class Madara(MainCharacter):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("madara_stance_1.png", hero_name='Madara', colorkey=-1)
        self.image = self.base

        self.images = {
            0: {'base': load_image("madara_stance_1.png", hero_name='Madara', colorkey=-1),

                'jump': [load_image('madara_jump_1.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_jump_2.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_jump_1.png', hero_name='Madara', colorkey=-1)],

                'guard': [load_image('madara_guard_1.png', hero_name='Madara', colorkey=-1),
                          load_image('madara_guard_1.png', hero_name='Madara', colorkey=-1),
                          load_image('madara_guard_2.png', hero_name='Madara', colorkey=-1),
                          load_image('madara_guard_2.png', hero_name='Madara', colorkey=-1)],

                'walk': [load_image('madara_walk_1.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_walk_2.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_walk_3.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_walk_4.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_walk_5.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_walk_6.png', hero_name='Madara', colorkey=-1)],

                'attack': [load_image('madara_attack_combo1_1.png', hero_name='Madara', colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', colorkey=-1)],

                'strong_attack': [load_image('madara_strong_attack_1.png', hero_name='Madara', colorkey=-1),
                                  load_image('madara_strong_attack_2.png', hero_name='Madara', colorkey=-1),
                                  load_image('madara_strong_attack_3.png', hero_name='Madara', colorkey=-1),
                                  load_image('madara_strong_attack_4.png', hero_name='Madara', colorkey=-1),
                                  load_image('madara_strong_attack_5.png', hero_name='Madara', colorkey=-1),
                                  load_image('madara_strong_attack_7.png', hero_name='Madara', colorkey=-1)],

                'intro': [load_image('madara_stance_2.png', hero_name='Madara', colorkey=-1),
                          load_image('madara_stance_3.png', hero_name='Madara', colorkey=-1),
                          load_image('madara_stance_4.png', hero_name='Madara', colorkey=-1)],

                'lose': [load_image('madara_lose_1.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_lose_2.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_lose_3.png', hero_name='Madara', colorkey=-1),
                         load_image('madara_lose_4.png', hero_name='Madara', colorkey=-1)],

                'win': [load_image('madara_win_1.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_win_2.png', hero_name='Madara', colorkey=-1)],

                'ult': [load_image('madara_ulting_1.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_ulting_2.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_ulting_3.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_ulting_4.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_ulting_5.png', hero_name='Madara', colorkey=-1),
                        load_image('madara_ulting_6.png', hero_name='Madara', colorkey=-1)],

                'damaged': [load_image('madara_damaged_1.png', hero_name='Madara', colorkey=-1),
                            load_image('madara_damaged_1.png', hero_name='Madara', colorkey=-1)]},

            1: {'base': load_image("madara_stance_1.png", hero_name='Madara', flipped=1, colorkey=-1),

                'jump': [load_image('madara_jump_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_jump_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_jump_1.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'guard': [load_image('madara_guard_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                          load_image('madara_guard_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                          load_image('madara_guard_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                          load_image('madara_guard_2.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'walk': [load_image('madara_walk_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_walk_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_walk_3.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_walk_4.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_walk_5.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_walk_6.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'attack': [load_image('madara_attack_combo1_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                           load_image('madara_attack_combo1_2.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'strong_attack': [load_image('madara_strong_attack_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                                  load_image('madara_strong_attack_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                                  load_image('madara_strong_attack_3.png', hero_name='Madara', flipped=1, colorkey=-1),
                                  load_image('madara_strong_attack_4.png', hero_name='Madara', flipped=1, colorkey=-1),
                                  load_image('madara_strong_attack_5.png', hero_name='Madara', flipped=1, colorkey=-1),
                                  load_image('madara_strong_attack_7.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'intro': [load_image('madara_stance_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                          load_image('madara_stance_3.png', hero_name='Madara', flipped=1, colorkey=-1),
                          load_image('madara_stance_4.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'lose': [load_image('madara_lose_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_lose_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_lose_3.png', hero_name='Madara', flipped=1, colorkey=-1),
                         load_image('madara_lose_4.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'win': [load_image('madara_win_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_win_2.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'ult': [load_image('madara_ulting_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_ulting_2.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_ulting_3.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_ulting_4.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_ulting_5.png', hero_name='Madara', flipped=1, colorkey=-1),
                        load_image('madara_ulting_6.png', hero_name='Madara', flipped=1, colorkey=-1)],

                'damaged': [load_image('madara_damaged_1.png', hero_name='Madara', flipped=1, colorkey=-1),
                            load_image('madara_damaged_1.png', hero_name='Madara', flipped=1, colorkey=-1)]}
        }


class MadaraUlt(pygame.sprite.Sprite):
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
            image_ult = [load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("madara_ulting_mokuton_1.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_2.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_3.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_4.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_5.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_6.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_7.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_8.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_9.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_10.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_11.png", hero_name='Madara', colorkey=-1),
                         load_image("madara_ulting_mokuton_13.png", hero_name='Madara', colorkey=-1),
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
            meruemult = MadaraUlt(all_sprites)
        elif keys[pygame.K_a]:
            madara.flipped()

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
