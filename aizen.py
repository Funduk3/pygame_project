import pygame
from load_image import load_image
from Character_main import MainCharacter

FPS = 50


class Aizen(MainCharacter):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("Aizen_stance.png", hero_name='Aizen', colorkey=-1)
        self.image = self.base

        self.images = {
            0: {'base': load_image("Aizen_stance.png", hero_name='Aizen', colorkey=-1),

                'jump': [load_image('Aizen_jump_1.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_jump_2.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_jump_4.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_jump_5.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_jump_6.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_jump_8.png', hero_name='Aizen', colorkey=-1)],

                'guard': [load_image('Aizen_guard_1.png', hero_name='Aizen', colorkey=-1),
                          load_image('Aizen_guard_2.png', hero_name='Aizen', colorkey=-1),
                          load_image('Aizen_guard_3.png', hero_name='Aizen', colorkey=-1),
                          load_image('Aizen_guard_4.png', hero_name='Aizen', colorkey=-1)],

                'walk': [load_image('Aizen_walk_1.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_walk_1.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_walk_1.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', colorkey=-1)],

                'attack': [load_image('Aizen_attack_1.png', hero_name='Aizen', colorkey=-1),
                           load_image('Aizen_attack_2.png', hero_name='Aizen', colorkey=-1),
                           load_image('Aizen_attack_3.png', hero_name='Aizen', colorkey=-1),
                           load_image('Aizen_attack_4.png', hero_name='Aizen', colorkey=-1)],

                'strong_attack': [load_image('Aizen_strong_attack_1.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_2.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_3.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_4.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_5.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_6.png', hero_name='Aizen', colorkey=-1),
                                  load_image('Aizen_strong_attack_7.png', hero_name='Aizen', colorkey=-1)],

                'intro': [load_image('Aizen_intro_1.png', hero_name='Aizen', colorkey=-1),
                          load_image('Aizen_intro_2.png', hero_name='Aizen', colorkey=-1),
                          load_image('Aizen_intro_3.png', hero_name='Aizen', colorkey=-1)],

                'lose': [load_image('Aizen_lose_1.png', hero_name='Aizen', colorkey=-1),
                         load_image('Aizen_lose_2.png', hero_name='Aizen', colorkey=-1)],

                'win': [load_image('Aizen_win_1.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_2.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_3.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_4.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_5.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_6.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_7.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_8.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_9.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_win_10.png', hero_name='Aizen', colorkey=-1)],

                'ult': [load_image('Aizen_ult_first_1.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_2.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_3.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_4.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_5.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_6.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_7.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_8.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_9.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_10.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_11.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_12.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_13.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_14.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_15.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_16.png', hero_name='Aizen', colorkey=-1),
                        load_image('Aizen_ult_first_17.png', hero_name='Aizen', colorkey=-1)],

                'damaged': [load_image('Aizen_damaged.png', hero_name='Aizen', colorkey=-1),
                            load_image('Aizen_damaged.png', hero_name='Aizen', colorkey=-1)]},

            1: {'base': load_image("Aizen_stance.png", hero_name='Aizen', flipped=1, colorkey=-1),

                'jump': [load_image('Aizen_jump_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_jump_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_jump_4.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_jump_5.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_jump_5.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_jump_8.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'guard': [load_image('Aizen_guard_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                          load_image('Aizen_guard_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                          load_image('Aizen_guard_3.png', hero_name='Aizen', flipped=1, colorkey=-1),
                          load_image('Aizen_guard_4.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'walk': [load_image('Aizen_walk_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_walk_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_walk_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_walk_2.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'attack': [load_image('Aizen_attack_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                           load_image('Aizen_attack_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                           load_image('Aizen_attack_3.png', hero_name='Aizen', flipped=1, colorkey=-1),
                           load_image('Aizen_attack_4.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'strong_attack': [load_image('Aizen_strong_attack_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_3.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_4.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_5.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_6.png', hero_name='Aizen', flipped=1, colorkey=-1),
                                  load_image('Aizen_strong_attack_7.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'intro': [load_image('Aizen_intro_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                          load_image('Aizen_intro_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                          load_image('Aizen_intro_3.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'lose': [load_image('Aizen_lose_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                         load_image('Aizen_lose_2.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'win': [load_image('Aizen_win_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_3.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_4.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_5.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_6.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_7.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_8.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_9.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_win_10.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'ult': [load_image('Aizen_ult_first_1.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_2.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_3.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_4.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_5.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_6.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_7.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_8.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_9.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_10.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_11.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_12.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_13.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_14.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_15.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_16.png', hero_name='Aizen', flipped=1, colorkey=-1),
                        load_image('Aizen_ult_first_17.png', hero_name='Aizen', flipped=1, colorkey=-1)],

                'damaged': [load_image('Aizen_damaged.png', hero_name='Aizen', flipped=1, colorkey=-1),
                            load_image('Aizen_damaged.png', hero_name='Aizen', flipped=1, colorkey=-1)]}
        }



class AizenUlt(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("empty.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = 400
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
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("empty.png", colorkey=-1),
                         load_image("Aizen_ult_1.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_2.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_3.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_4.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_5.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_6.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_7.png", hero_name='Aizen', colorkey=-1),
                         load_image("Aizen_ult_8.png", hero_name='Aizen', colorkey=-1),
                         load_image("empty.png", colorkey=-1)]
            self.count += 1
            if self.count >= len(image_ult):
                self.count = 0
                self.is_ulting = False
            else:
                clock.tick(10)
                self.image = image_ult[self.count]


if __name__ == '__main__':
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
