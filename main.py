import pygame

pygame.init()
#global variables
WIDTH = 1820
HEIGHT = 980

color = (255, 0, 0)#RGB


screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True




while running:
    events = pygame.event.get()
    screen.fill((0,0,0))
    for whatever in events:
        if whatever.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, color, pygame.Rect(WIDTH/2, HEIGHT/2, 123, 456))

    #pygame.draw.rect()



#draw rectangle
