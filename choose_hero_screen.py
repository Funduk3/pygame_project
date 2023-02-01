import pygame
from load_image import load_image
import sys
import os

FPS = 50

pygame.init()
size = width, height = 800, 450
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
objects = []

f1 = pygame.font.Font('C:/Коды/pygame/data/joystix monospace.ttf', 36)
text1 = f1.render('Выбери персонажа', True,
                  (180, 0, 0))

background = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\context.jpg"), (800, 450))
aizen_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\Aizen_ava.jpg"), (100, 100))
madara_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\madara_ava.png"), (100, 100))
dio_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\dio_ava.jpg"), (100, 100))
eren_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\eren_ava.jpg"), (100, 100))
example = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\meruem.jpg"), (100, 100))
sound_of = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\sound_of.png"), (40, 40))
sound_on = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\sound_on.png"), (40, 40))

pygame.mixer.music.load('C:\Коды\pygame\data\data_main_fight_sound.mp3')

screen.blit(background, (0, 0))
screen.blit(aizen_ava, (130, 300))
screen.blit(madara_ava, (240, 300))
screen.blit(dio_ava, (350, 300))
screen.blit(eren_ava, (460, 300))
screen.blit(example, (570, 300))
screen.blit(text1, (150, 10))

pygame.mixer.music.play()

def pers1_rect(color):
    pygame.draw.line(screen, pygame.Color(color), (130, 400), (230, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (130, 300), (230, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (130, 400), (130, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (230, 400), (230, 300), width=5)


def pers2_rect(color):
    pygame.draw.line(screen, pygame.Color(color), (240, 400), (340, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (240, 300), (340, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (240, 400), (240, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (340, 400), (340, 300), width=5)


def pers3_rect(color):
    pygame.draw.line(screen, pygame.Color(color), (350, 400), (450, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (350, 300), (450, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (350, 400), (350, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (450, 400), (450, 300), width=5)


def pers4_rect(color):
    pygame.draw.line(screen, pygame.Color(color), (460, 400), (560, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (460, 300), (560, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (460, 400), (460, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (560, 400), (560, 300), width=5)


def pers5_rect(color):
    pygame.draw.line(screen, pygame.Color(color), (570, 400), (670, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (570, 300), (670, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (570, 400), (570, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (670, 400), (670, 300), width=5)


def check_coords_color(coords, x, y, color, number_of_pers):
    if number_of_pers != first_pers and number_of_pers != second_pers:
        if x < coords[0] < x + 100 and y < coords[1] < y + 100:
            func_numbers[number_of_pers - 1](color)
        else:
            func_numbers[number_of_pers - 1]('white')


def choice_pers():
    coords = pygame.mouse.get_pos()
    pers = 0
    if 130 < coords[0] < 230 and 300 < coords[1] < 400:
        pers = 1
    elif 240 < coords[0] < 340 and 300 < coords[1] < 400:
        pers = 2
    elif 350 < coords[0] < 450 and 300 < coords[1] < 400:
        pers = 3
    elif 460 < coords[0] < 560 and 300 < coords[1] < 400:
        pers = 4
    elif 570 < coords[0] < 670 and 300 < coords[1] < 400:
        pers = 5
    return pers


func_numbers = [pers1_rect, pers2_rect, pers3_rect, pers4_rect, pers5_rect]
first_pers = False
second_pers = False

sound_of_flag = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not first_pers:
                    first_pers = choice_pers()
                    if first_pers == 1:
                        pers1_rect('red')
                    elif first_pers == 2:
                        pers2_rect('red')
                    elif first_pers == 3:
                        pers3_rect('red')
                    elif first_pers == 4:
                        pers4_rect('red')
                    elif first_pers == 5:
                        pers5_rect('red')
                elif not second_pers:
                    second_pers = choice_pers()
                    if second_pers == 1:
                        pers1_rect('blue')
                    elif second_pers == 2:
                        pers2_rect('blue')
                    elif second_pers == 3:
                        pers3_rect('blue')
                    elif second_pers == 4:
                        pers4_rect('blue')
                    elif second_pers == 5:
                        pers5_rect('blue')
                coords = pygame.mouse.get_pos()
                if 760 < coords[0] < 800 and 0 < coords[1] < 40:
                    if sound_of_flag:
                        sound_of_flag = False
                    else:
                        sound_of_flag = True

    if sound_of_flag:
        pygame.draw.rect(screen, 'white', (760, 0, 800, 40))
        screen.blit(sound_of, (760, 0))
        pygame.mixer.music.unpause()
    else:
        pygame.draw.rect(screen, 'white', (760, 0, 800, 40))
        screen.blit(sound_on, (760, 0))
        pygame.mixer.music.pause()

    coords = pygame.mouse.get_pos()
    if not first_pers:
        check_coords_color(coords, 130, 300, 'red', 1)
        check_coords_color(coords, 240, 300, 'red', 2)
        check_coords_color(coords, 350, 300, 'red', 3)
        check_coords_color(coords, 460, 300, 'red', 4)
        check_coords_color(coords, 570, 300, 'red', 5)
    elif not second_pers:
        check_coords_color(coords, 130, 300, 'blue', 1)
        check_coords_color(coords, 240, 300, 'blue', 2)
        check_coords_color(coords, 350, 300, 'blue', 3)
        check_coords_color(coords, 460, 300, 'blue', 4)
        check_coords_color(coords, 570, 300, 'blue', 5)

    all_sprites.update()
    clock.tick(30)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()