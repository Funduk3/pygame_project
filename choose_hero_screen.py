import pygame
from load_image import load_image
import aizen, madara, meruem, dio, eren


FPS = 50
pygame.init()
size = width, height = 800, 450
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
objects = []

pygame.draw.line(screen, pygame.Color('red'), (130, 400), (230, 400), width=5)
pygame.draw.line(screen, pygame.Color('red'), (130, 300), (230, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (130, 400), (130, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (230, 400), (230, 300), width=5)

pygame.draw.line(screen, pygame.Color('red'), (240, 400), (340, 400), width=5)
pygame.draw.line(screen, pygame.Color('red'), (240, 300), (340, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (240, 400), (240, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (340, 400), (340, 300), width=5)

pygame.draw.line(screen, pygame.Color('red'), (350, 400), (450, 400), width=5)
pygame.draw.line(screen, pygame.Color('red'), (350, 300), (450, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (350, 400), (350, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (450, 400), (450, 300), width=5)

pygame.draw.line(screen, pygame.Color('red'), (460, 400), (560, 400), width=5)
pygame.draw.line(screen, pygame.Color('red'), (460, 300), (560, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (460, 400), (460, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (560, 400), (560, 300), width=5)

pygame.draw.line(screen, pygame.Color('red'), (570, 400), (670, 400), width=5)
pygame.draw.line(screen, pygame.Color('red'), (570, 300), (670, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (570, 400), (570, 300), width=5)
pygame.draw.line(screen, pygame.Color('red'), (670, 400), (670, 300), width=5)
f1 = pygame.font.Font('data/joystix monospace.ttf', 36)
text1 = f1.render('Выбери персонажа', True, (180, 0, 0))

background = pygame.transform.scale(load_image("fon.jpg", hero_name='started_screen'), (800, 450))
aizen_ava = pygame.transform.scale(load_image("Aizen_ava.jpg", hero_name='started_screen'), (100, 100))
madara_ava = pygame.transform.scale(load_image("madara_ava.png", hero_name='started_screen'), (100, 100))
dio_ava = pygame.transform.scale(load_image("dio_ava.jpg", hero_name='started_screen'), (100, 100))
eren_ava = pygame.transform.scale(load_image("eren_ava.jpg", hero_name='started_screen'), (100, 100))
example = pygame.transform.scale(load_image("meruem.jpg", hero_name='started_screen'), (100, 100))
sound_of = pygame.transform.scale(load_image("sound_of.jpg", hero_name='started_screen', colorkey=-1), (40, 40))
sound_on = pygame.transform.scale(load_image("sound_on.jpg", hero_name='started_screen', colorkey=-1), (40, 40))

aizen_rect = aizen_ava.get_rect()
aizen_rect.x, aizen_rect.y = 100, 100

madara_rect = madara_ava.get_rect()
madara_rect.x, madara_rect.y = 100, 100

dio_rect = dio_ava.get_rect()
dio_rect.x, dio_rect.y = 100, 100

eren_rect = eren_ava.get_rect()
eren_rect.x, eren_rect.y = 100, 100
pygame.mixer.music.load('data/main_fight_sound.mp3')

screen.blit(background, (0, 0))
screen.blit(aizen_ava, (130, 300))
screen.blit(madara_ava, (240, 300))
screen.blit(dio_ava, (350, 300))
screen.blit(eren_ava, (460, 300))
screen.blit(example, (570, 300))
screen.blit(text1, (150, 10))

pygame.mixer.music.play()


def aizen_rect_f(color):
    pygame.draw.line(screen, pygame.Color(color), (130, 400), (230, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (130, 300), (230, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (130, 400), (130, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (230, 400), (230, 300), width=5)


def madara_rect_f(color):
    pygame.draw.line(screen, pygame.Color(color), (240, 400), (340, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (240, 300), (340, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (240, 400), (240, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (340, 400), (340, 300), width=5)


def dio_rect_f(color):
    pygame.draw.line(screen, pygame.Color(color), (350, 400), (450, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (350, 300), (450, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (350, 400), (350, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (450, 400), (450, 300), width=5)


def eren_rect_f(color):
    pygame.draw.line(screen, pygame.Color(color), (460, 400), (560, 400), width=5)
    pygame.draw.line(screen, pygame.Color(color), (460, 300), (560, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (460, 400), (460, 300), width=5)
    pygame.draw.line(screen, pygame.Color(color), (560, 400), (560, 300), width=5)


def meruem_rect_x(color):
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


func_numbers = [aizen_rect_f, madara_rect_f, dio_rect_f, eren_rect_f, meruem_rect_x]
first_pers = False
second_pers = False

sound_of_flag = True

running = True
while running:
    for event in pygame.event.get():
        screen.blit(background, (0, 0))
        screen.blit(aizen_ava, (130, 300))
        screen.blit(madara_ava, (240, 300))
        screen.blit(dio_ava, (350, 300))
        screen.blit(eren_ava, (460, 300))
        screen.blit(example, (570, 300))
        screen.blit(text1, (150, 10))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not first_pers:
                    first_pers = choice_pers()
                    if first_pers == 1:
                        aizen_rect_f('red')
                        aiz = aizen.Aizen(all_sprites)
                        aiz.rect.x = 230
                        aiz.rect.y = 150
                        aiz.walk()
                        aiz.intro()
                    elif first_pers == 2:
                        madara_rect_f('red')
                        madar = madara.Madara(all_sprites)
                        madar.rect.x = 230
                        madar.rect.y = 150
                        madar.walk()
                        madar.intro()
                    elif first_pers == 3:
                        dio_rect_f('red')
                        dioo = dio.Dio(all_sprites)
                        dioo.rect.x = 230
                        dioo.rect.y = 150
                        dioo.walk()
                        dioo.intro()
                    elif first_pers == 4:
                        eren_rect_f('red')
                        ere = eren.Eren(all_sprites)
                        ere.rect.x = 230
                        ere.rect.y = 150
                        ere.walk()
                        ere.intro()
                    elif first_pers == 5:
                        meruem_rect_x('red')
                        mer = meruem.Meruem(all_sprites)
                        mer.rect.x = 230
                        mer.rect.y = 150
                        mer.walk()
                        mer.intro()
                elif not second_pers:
                    second_pers = choice_pers()
                    if second_pers == 1:
                        aizen_rect_f('blue')
                        aizz = aizen.Aizen(all_sprites)
                        aizz.rect.x = 520
                        aizz.rect.y = 150
                        aizz.flipped()
                        aizz.intro()
                    elif second_pers == 2:
                        madara_rect_f('blue')
                        mada = madara.Madara(all_sprites)
                        mada.rect.x = 520
                        mada.rect.y = 150
                        mada.flipped()
                        mada.intro()
                    elif second_pers == 3:
                        dio_rect_f('blue')
                        di = dio.Dio(all_sprites)
                        di.rect.x = 520
                        di.rect.y = 150
                        di.flipped()
                        di.intro()
                    elif second_pers == 4:
                        eren_rect_f('blue')
                        erenn = eren.Eren(all_sprites)
                        erenn.rect.x = 520
                        erenn.rect.y = 150
                        erenn.flipped()
                        erenn.intro()
                    elif second_pers == 5:
                        meruem_rect_x('blue')
                        mer = meruem.Meruem(all_sprites)
                        mer.rect.x = 520
                        mer.rect.y = 150
                        mer.flipped()
                        mer.intro()
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

    clock.tick(30)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
pygame.quit()
