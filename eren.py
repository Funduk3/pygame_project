import pygame
from load_image import load_image
from Character_main import MainCharacter

FPS = 50


class Eren(MainCharacter):
    def __init__(self, *group):
        super().__init__(*group)
        self.base = load_image("Eren_stance_1.png", hero_name='Eren', colorkey=-1)
        self.titan_base = load_image("Titan_stance_1.png", hero_name='Eren', colorkey=-1)
        self.image = self.base

        self.is_titan = False

        self.images = {
            0: {'base': load_image("Eren_stance_1.png", hero_name='Eren', colorkey=-1),

                'jump': [load_image('Eren_jump_1.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_jump_2.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_jump_3.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_jump_4.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_jump_5.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_jump_6.png', hero_name='Eren', colorkey=-1)],

                'guard': [load_image('Eren_guard_1.png', hero_name='Eren', colorkey=-1),
                          load_image('Eren_guard_1.png', hero_name='Eren', colorkey=-1),
                          load_image('Eren_guard_2.png', hero_name='Eren', colorkey=-1),
                          load_image('Eren_guard_2.png', hero_name='Eren', colorkey=-1)],

                'walk': [load_image('Eren_walk_1.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_walk_2.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_walk_3.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_walk_4.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_walk_5.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_walk_6.png', hero_name='Eren', colorkey=-1)],

                'attack': [load_image('Eren_attack_1.png', hero_name='Eren', colorkey=-1),
                           load_image('Eren_attack_2.png', hero_name='Eren', colorkey=-1),
                           load_image('Eren_attack_3.png', hero_name='Eren', colorkey=-1),
                           load_image('Eren_attack_4.png', hero_name='Eren', colorkey=-1),
                           load_image('Eren_attack_5.png', hero_name='Eren', colorkey=-1)],

                'strong_attack': [load_image('Eren_strong_attack_1.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_2.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_3.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_3.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_4.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_4.png', hero_name='Eren', colorkey=-1),
                                  load_image('Eren_strong_attack_5.png', hero_name='Eren', colorkey=-1)],

                'intro': [load_image('Eren_stance_1.png', hero_name='Eren', colorkey=-1),
                          load_image('Eren_stance_1.png', hero_name='Eren', colorkey=-1),
                          load_image('Eren_stance_1.png', hero_name='Eren', colorkey=-1)],

                'lose': [load_image('Eren_lose_1.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_lose_2.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_lose_3.png', hero_name='Eren', colorkey=-1),
                         load_image('Eren_lose_4.png', hero_name='Eren', colorkey=-1)],

                'win': [load_image('Eren_win_1.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_win_2.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_win_3.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_win_4.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_win_5.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_win_6.png', hero_name='Eren', colorkey=-1)],

                'ult': [load_image('Eren_ult_1.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_2.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_3.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_4.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_5.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_6.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_7.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_8.png', hero_name='Eren', colorkey=-1),
                        load_image('Eren_ult_9.png', hero_name='Eren', colorkey=-1),
                        load_image('Titan_stance_1.png', hero_name='Eren', colorkey=-1)],

                'damaged': [load_image('Eren_damaged_1.png', hero_name='Eren', colorkey=-1),
                            load_image('Eren_damaged_2.png', hero_name='Eren', colorkey=-1)],

                'titan_base': load_image('Titan_stance_1.png', hero_name='Eren', colorkey=-1),

                'titan_attack': [load_image('Titan_attack_1.png', hero_name='Eren', colorkey=-1),
                                 load_image('Titan_attack_2.png', hero_name='Eren', colorkey=-1),
                                 load_image('Titan_attack_3.png', hero_name='Eren', colorkey=-1),
                                 load_image('Titan_attack_3.png', hero_name='Eren', colorkey=-1),
                                 load_image('Titan_attack_4.png', hero_name='Eren', colorkey=-1)],

                'titan_strong_attack': [load_image('Titan_strong_attack_1.png', hero_name='Eren', colorkey=-1),
                                        load_image('Titan_strong_attack_2.png', hero_name='Eren', colorkey=-1),
                                        load_image('Titan_strong_attack_3.png', hero_name='Eren', colorkey=-1),
                                        load_image('Titan_strong_attack_4.png', hero_name='Eren', colorkey=-1),
                                        load_image('Titan_strong_attack_5.png', hero_name='Eren', colorkey=-1)],

                'titan_leg_attack': [load_image('Titan_leg_attack_1.png', hero_name='Eren', colorkey=-1),
                                     load_image('Titan_leg_attack_2.png', hero_name='Eren', colorkey=-1),
                                     load_image('Titan_leg_attack_2.png', hero_name='Eren', colorkey=-1),
                                     load_image('Titan_leg_attack_3.png', hero_name='Eren', colorkey=-1)],

                'titan_guard': [load_image('Titan_guard.png', hero_name='Eren', colorkey=-1),
                                load_image('Titan_guard.png', hero_name='Eren', colorkey=-1)],

                'titan_damaged': [load_image('Titan_damaged.png', hero_name='Eren', colorkey=-1),
                                  load_image('Titan_damaged.png', hero_name='Eren', colorkey=-1)],

                'titan_walk': [load_image('Titan_walk_1.png', hero_name='Eren', colorkey=-1),
                               load_image('Titan_walk_2.png', hero_name='Eren', colorkey=-1),
                               load_image('Titan_walk_3.png', hero_name='Eren', colorkey=-1),
                               load_image('Titan_walk_5.png', hero_name='Eren', colorkey=-1),
                               load_image('Titan_walk_8.png', hero_name='Eren', colorkey=-1),
                               load_image('Titan_walk_9.png', hero_name='Eren', colorkey=-1)],

                },

            1: {'base': load_image("Eren_stance_1.png", hero_name='Eren', flipped=1, colorkey=-1),

                'jump': [load_image('Eren_jump_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_jump_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_jump_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_jump_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_jump_5.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_jump_6.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'guard': [load_image('Eren_guard_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                          load_image('Eren_guard_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                          load_image('Eren_guard_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                          load_image('Eren_guard_2.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'walk': [load_image('Eren_walk_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_walk_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_walk_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_walk_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_walk_5.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_walk_6.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'attack': [load_image('Eren_attack_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                           load_image('Eren_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                           load_image('Eren_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                           load_image('Eren_attack_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                           load_image('Eren_attack_5.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'strong_attack': [load_image('Eren_strong_attack_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Eren_strong_attack_5.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'intro': [load_image('Eren_stance_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                          load_image('Eren_stance_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                          load_image('Eren_stance_1.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'lose': [load_image('Eren_lose_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_lose_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_lose_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                         load_image('Eren_lose_4.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'win': [load_image('Eren_win_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_win_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_win_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_win_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_win_5.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_win_6.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'ult': [load_image('Eren_ult_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_5.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_6.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_7.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_8.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Eren_ult_9.png', hero_name='Eren', flipped=1, colorkey=-1),
                        load_image('Titan_stance_1.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'damaged': [load_image('Eren_damaged_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                            load_image('Eren_damaged_2.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_base': load_image('Titan_stance_1.png', hero_name='Eren', flipped=1, colorkey=-1),

                'titan_attack': [load_image('Titan_attack_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                                 load_image('Titan_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                                 load_image('Titan_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                                 load_image('Titan_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                                 load_image('Titan_attack_4.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_strong_attack': [
                    load_image('Titan_strong_attack_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                    load_image('Titan_strong_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                    load_image('Titan_strong_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                    load_image('Titan_strong_attack_4.png', hero_name='Eren', flipped=1, colorkey=-1),
                    load_image('Titan_strong_attack_5.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_leg_attack': [load_image('Titan_leg_attack_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                                     load_image('Titan_leg_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                                     load_image('Titan_leg_attack_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                                     load_image('Titan_leg_attack_3.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_guard': [load_image('Titan_guard.png', hero_name='Eren', flipped=1, colorkey=-1),
                                load_image('Titan_guard.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_damaged': [load_image('Titan_damaged.png', hero_name='Eren', flipped=1, colorkey=-1),
                                  load_image('Titan_damaged.png', hero_name='Eren', flipped=1, colorkey=-1)],

                'titan_walk': [load_image('Titan_walk_1.png', hero_name='Eren', flipped=1, colorkey=-1),
                               load_image('Titan_walk_2.png', hero_name='Eren', flipped=1, colorkey=-1),
                               load_image('Titan_walk_3.png', hero_name='Eren', flipped=1, colorkey=-1),
                               load_image('Titan_walk_5.png', hero_name='Eren', flipped=1, colorkey=-1),
                               load_image('Titan_walk_8.png', hero_name='Eren', flipped=1, colorkey=-1),
                               load_image('Titan_walk_9.png', hero_name='Eren', flipped=1, colorkey=-1)],
                }
        }

    def walk(self):
        if self.is_titan:
            self.base = self.images[0]['titan_base']
        else:
            self.base = self.images[0]['base']
        self.is_walking = True
        self.is_flipped = False

    def flipped(self):
        self.is_flipped = True
        if self.is_titan:
            self.base = self.images[1]['titan_base']
        else:
            self.base = self.images[1]['base']
        self.is_walking = True

    def update(self, *args, **kwargs):
        if self.is_jumping:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_jump = self.images[0]['jump']
                else:
                    self.images_jump = self.images[1]['jump']
            else:
                if not self.is_flipped:
                    self.images_jump = self.images[0]['titan_leg_attack']
                else:
                    self.images_jump = self.images[1]['titan_leg_attack']
            self.count += 1
            if self.count >= len(self.images_jump):
                self.count = 0
                self.image = self.base
                self.is_jumping = False
            else:
                clock.tick(10)
                self.image = self.images_jump[self.count]

        if self.is_guarding:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_guard = self.images[0]['guard']
                else:
                    self.images_guard = self.images[1]['guard']
            else:
                if not self.is_flipped:
                    self.images_guard = self.images[0]['titan_guard']
                else:
                    self.images_guard = self.images[1]['titan_guard']
            self.count += 1
            if self.count >= len(self.images_guard):
                self.count = 0
                self.image = self.base
                self.is_guarding = False
            else:
                clock.tick(5)
                self.image = self.images_guard[self.count]

        if self.is_walking:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_walk = self.images[0]['walk']
                    self.count += 1
                    if self.count >= len(self.images_walk):
                        self.count = 0
                        self.image = self.base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = self.images_walk[self.count]
                        self.rect.x += 5
                else:
                    self.images_walk = self.images[1]['walk']
                    self.count += 1
                    if self.count >= len(self.images_walk):
                        self.count = 0
                        self.image = self.base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = self.images_walk[self.count]
                        self.rect.x -= 5
            else:
                if not self.is_flipped:
                    self.images_walk = self.images[0]['titan_walk']
                    self.count += 1
                    if self.count >= len(self.images_walk):
                        self.count = 0
                        self.image = self.base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = self.images_walk[self.count]
                        self.rect.x += 5
                else:
                    self.images_walk = self.images[1]['titan_walk']
                    self.count += 1
                    if self.count >= len(self.images_walk):
                        self.count = 0
                        self.image = self.base
                        self.is_walking = False
                    else:
                        clock.tick(5)
                        self.image = self.images_walk[self.count]
                        self.rect.x -= 5

        if self.is_attacking:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_attack = self.images[0]['attack']
                else:
                    self.images_attack = self.images[1]['attack']
            else:
                if not self.is_flipped:
                    self.images_attack = self.images[0]['titan_attack']
                else:
                    self.images_attack = self.images[1]['titan_attack']
            self.count += 1
            if self.count >= len(self.images_attack):
                self.count = 0
                self.image = self.base
                self.is_attacking = False
            else:
                clock.tick(5)
                self.image = self.images_attack[self.count]

        if self.is_strong_attacking:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_strong_attack = self.images[0]['strong_attack']
                else:
                    self.images_strong_attack = self.images[1]['strong_attack']
            else:
                if not self.is_flipped:
                    self.images_strong_attack = self.images[0]['titan_strong_attack']
                else:
                    self.images_strong_attack = self.images[1]['titan_strong_attack']
            self.count += 1
            if self.count >= len(self.images_strong_attack):
                self.count = 0
                self.image = self.base
                self.is_strong_attacking = False
            else:
                clock.tick(5)
                self.image = self.images_strong_attack[self.count]

        if self.is_intro:
            self.images_intro = self.images[1]['intro']
            self.count += 1
            if self.count >= len(self.images_intro):
                self.count = 0
                self.image = self.base
                self.is_intro = False
            else:
                clock.tick(5)
                self.image = self.images_intro[self.count]

        if self.is_losing:
            self.images_lose = self.images[1]['lose']
            self.count += 1
            if self.count >= len(self.images_lose):
                self.count = 0
                self.image = self.base
                self.is_losing = False
            else:
                clock.tick(5)
                self.image = self.images_lose[self.count]

        if self.is_winning:
            self.images_win = self.images[1]['win']
            self.count += 1
            if self.count >= len(self.images_win):
                self.count = 0
                self.image = self.base
                self.is_winning = False
            else:
                clock.tick(5)
                self.image = self.images_win[self.count]

        if self.is_ulting:
            if not self.is_flipped:
                self.images_ult = self.images[0]['ult']
            else:
                self.images_ult = self.images[1]['ult']
            self.count += 1
            if self.count >= len(self.images_ult):
                self.count = 0
                self.image = self.images[0]['titan_base']
                self.is_titan = True
                self.base = self.images[0]['titan_base']
                self.is_ulting = False
            else:
                clock.tick(5)
                self.image = self.images_ult[self.count]

        if self.is_damaged:
            if not self.is_titan:
                if not self.is_flipped:
                    self.images_damaged = self.images[0]['damaged']
                else:
                    self.images_damaged = self.images[1]['damaged']
            else:
                if not self.is_flipped:
                    self.images_damaged = self.images[0]['titan_damaged']
                else:
                    self.images_damaged = self.images[1]['titan_damaged']
            self.count += 1
            if self.count >= len(self.images_damaged):
                self.count = 0
                self.image = self.base
                self.is_damaged = False
            else:
                clock.tick(5)
                self.image = self.images_damaged[self.count]


clock = pygame.time.Clock()
if __name__ == '__main__':
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
