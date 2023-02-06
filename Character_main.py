import pygame
from load_image import load_image

FPS = 50


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.images_damaged = None
        self.images_ult = None
        self.images_win = None
        self.images_lose = None
        self.images_intro = None
        self.images_strong_attack = None
        self.images_attack = None
        self.images_walk = None
        self.images_guard = None
        self.images_jump = None

        self.count = 0
        self.intro_images = []
        self.lose_images = []
        self.win_images = []
        self.ult_images = []
        self.base = load_image('empty.png', colorkey=-1)
        self.image = self.base
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.is_flipped = False
        self.is_damaged = False
        self.is_ulting = False
        self.is_winning = False
        self.is_losing = False
        self.is_intro = False
        self.is_strong_attacking = False
        self.is_attacking = False
        self.is_walking = False
        self.is_guarding = False
        self.is_jumping = False
        self.images = {
            0: {'base': load_image('empty.png', colorkey=-1),
                'jump': [load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                         load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                         load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1)],
                'guard': [load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                          load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1)],
                'walk': [load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                         load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                         load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1)],
                'attack': [load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                           load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1)],
                'strong_attack': [load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                                  load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                                  load_image('empty.png', colorkey=-1), load_image('empty.png', colorkey=-1),
                                  load_image('empty.png', colorkey=-1)],
                'intro': self.intro_images,
                'lose': self.lose_images,
                'win': self.win_images,
                'ult': self.ult_images,
                'damaged': [load_image('empty.png', flipped=1, colorkey=-1),
                            load_image('empty.png', flipped=1, colorkey=-1)]},
            1: {'base': load_image('empty.png', flipped=1, colorkey=-1),
                'jump': [load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1)],
                'guard': [load_image('empty.png', flipped=1, colorkey=-1),
                          load_image('empty.png', flipped=1, colorkey=-1),
                          load_image('empty.png', flipped=1, colorkey=-1),
                          load_image('empty.png', flipped=1, colorkey=-1)],
                'walk': [load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1),
                         load_image('empty.png', flipped=1, colorkey=-1)],
                'attack': [load_image('empty.png', flipped=1, colorkey=-1),
                           load_image('empty.png', flipped=1, colorkey=-1),
                           load_image('empty.png', flipped=1, colorkey=-1),
                           load_image('empty.png', flipped=1, colorkey=-1)],
                'strong_attack': [load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1),
                                  load_image('empty.png', flipped=1, colorkey=-1)],
                'intro': self.intro_images,
                'lose': self.lose_images,
                'win': self.win_images,
                'ult': self.ult_images,
                'damaged': [load_image('empty.png', flipped=1, colorkey=-1),
                            load_image('empty.png', flipped=1, colorkey=-1)]}
        }

    def jump(self):
        self.is_jumping = True

    def guard(self):
        self.is_guarding = True

    def walk(self):
        self.base = self.images[0]['base']
        self.is_walking = True
        self.is_flipped = False

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
        self.is_flipped = True
        self.base = self.images[1]['base']
        self.is_walking = True

    def update(self, *args, **kwargs):
        if self.is_jumping:
            if not self.is_flipped:
                self.images_jump = self.images[0]['jump']
            else:
                self.images_jump = self.images[1]['jump']
            self.count += 1
            if self.count >= len(self.images_jump):
                self.count = 0
                self.image = self.base
                self.is_jumping = False
            else:
                clock.tick(10)
                self.image = self.images_jump[self.count]

        if self.is_guarding:
            if not self.is_flipped:
                self.images_guard = self.images[0]['guard']
            else:
                self.images_guard = self.images[1]['guard']
            self.count += 1
            if self.count >= len(self.images_guard):
                self.count = 0
                self.image = self.base
                self.is_guarding = False
            else:
                clock.tick(5)
                self.image = self.images_guard[self.count]

        if self.is_walking:
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

        if self.is_attacking:
            if not self.is_flipped:
                self.images_attack = self.images[0]['attack']
            else:
                self.images_attack = self.images[1]['attack']
            self.count += 1
            if self.count >= len(self.images_attack):
                self.count = 0
                self.image = self.base
                self.is_attacking = False
            else:
                clock.tick(5)
                self.image = self.images_attack[self.count]

        if self.is_strong_attacking:
            if not self.is_flipped:
                self.images_strong_attack = self.images[0]['strong_attack']
            else:
                self.images_strong_attack = self.images[1]['strong_attack']
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
                self.image = self.base
                self.is_ulting = False
            else:
                clock.tick(5)
                self.image = self.images_ult[self.count]

        if self.is_damaged:
            if not self.is_flipped:
                self.images_damaged = self.images[0]['damaged']
            else:
                self.images_damaged = self.images[1]['damaged']
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

    chr = MainCharacter(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
