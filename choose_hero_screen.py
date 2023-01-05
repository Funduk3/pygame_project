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

aizen_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\Aizen_ava.jpg"), (100, 100))
madara_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\madara_ava.png"), (100, 100))
dio_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\dio_ava.jpg"), (100, 100))
eren_ava = pygame.transform.scale(load_image("C:\Коды\pygame\data\started_screen\eren_ava.jpg"), (100, 100))

aizen_rect = aizen_ava.get_rect()
aizen_rect.x, aizen_rect.y = 100, 100

madara_rect = madara_ava.get_rect()
madara_rect.x, madara_rect.y = 100, 100

dio_rect = dio_ava.get_rect()
dio_rect.x, dio_rect.y = 100, 100

eren_rect = eren_ava.get_rect()
eren_rect.x, eren_rect.y = 100, 100

screen.blit(aizen_ava, (130, 300))
screen.blit(madara_ava, (240, 300))
screen.blit(dio_ava, (350, 300))
screen.blit(eren_ava, (460, 300))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    clock.tick(30)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
