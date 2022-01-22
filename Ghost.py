import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, type):
        super(Ghost, self).__init__()
        if type < 1 or type > 3:
            print("Invalid Ghost Type")
        else:
            self.surface = pygame.image.load("Reasources/ghost" + str(type) + ".png").convert()#holds image
            self.image = pygame.image.load("Reasources/ghost" + str(type) + ".png").convert()#display image @ the rect!
            self.rect = self.surface.get_rect()#holds coordinate data
