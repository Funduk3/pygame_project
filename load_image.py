import pygame
import os
import sys


def load_image(name, hero_name=None, flipped=0, colorkey=None):
    if not hero_name:
        fullname = os.path.join('data', name)
    else:
        fullname = os.path.join('data', hero_name, name)
    if not os.path.isfile(fullname):
        print(f'Файл {name} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if flipped == 1:
        pygame.transform.flip(image, True, False)
    if colorkey is None:
        image = image.convert_alpha()
    elif colorkey == -1:
        image.set_colorkey(image.get_at((0, 0)))
    else:
        image.set_colorkey(colorkey)
    return image

