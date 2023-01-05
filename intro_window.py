import pygame
from load_image import load_image
import sys
import os

FPS = 50


class StartedScreen(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        main_fon = pygame.transform.scale(load_image('C:\Коды\pygame\data\main_fon\main_fon.png'), (width, height))
        spaceships_fon = pygame.transform.scale(load_image('C:\Коды\pygame\data\main_fon\spaceships_fon.png'),
                                                (width, height))
        self.rect = spaceships_fon.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        planet_fon = pygame.transform.scale(load_image('C:\Коды\pygame\data\main_fon\planet_fon.png'), (width, height))

        screen.blit(main_fon, (0, 0))
        screen.blit(spaceships_fon, (0, 60))
        screen.blit(planet_fon, (0, 0))

    def update(self, *args):
        self.rect.x += 1
        print(self.rect.x)
        pygame.display.flip()


class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.font = pygame.font.Font('C:\Коды\pygame\data\joystix monospace.ttf', 20)

        self.fillColors = {
            'normal': '#851115',
            'hover': '#f4a460',
            'pressed': '#fad2b0',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

    def get_pressed(self):
        return self.alreadyPressed


def quitFunction():
    pygame.quit()


def myFunction():
    print(22)


# --------------------------------------------------------------------------------

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
objects = []

# dartvader = DartVader(all_sprites)
# spiderman = SpiderMan(all_sprites)

play_mode_button = Button(width / 2 - 900, height / 2 - 50, 300, 80, 'PLAY', myFunction)
options_button = Button(width / 2 - 900, height / 2 + 50, 300, 80, 'OPTIONS', myFunction, True)
quit_game_button = Button(width / 2 - 900, height / 2 + 150, 300, 80, 'QUIT', quitFunction)

screens_sound = pygame.mixer.Sound(file=os.path.join("data", 'main_fight_sound.mp3'))
screens_sound.set_volume(0.5)
screens_sound.play(loops=-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        start_screen = StartedScreen()
        all_sprites.update(event)
    for obj in objects:
        obj.process()
    all_sprites.update()
    clock.tick(30)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
