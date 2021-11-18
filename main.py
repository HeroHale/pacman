import pygame

pygame.init()
#global variables
WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

while running:
    events = pygame.event.get()

    for whatever in events:
        if whatever.type == pygame.QUIT:
            running = False
