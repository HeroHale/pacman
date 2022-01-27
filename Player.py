import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, controls):
        super().__init__()
        self.weirdcontrols = controls
        self.x_position = 0
        self.y_position = 0
        self.movespeed = 5
        self.sprites = []
        self.sprites.append(pygame.image.load('Reasources/pacman_1.png'))
        self.sprites.append(pygame.image.load('Reasources/pacman_2.gif'))
        self.sprites.append(pygame.image.load('Reasources/pacman_3.gif'))
        self.sprites.append(pygame.image.load('Reasources/pacman_4.gif'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        #self.surface = pygame.image.load("C:\\Users\\hmthe\\Desktop\\Code Ninjas Wednesday Class\\Tetris\\pacman.png").convert()#holds image
        #self.image = pygame.image.load("C:\\Users\\hmthe\\Desktop\\Code Ninjas Wednesday Class\\Tetris\\pacman.png").convert()#display image @ the rect!
        self.rect = self.image.get_rect()#holds coordinate data

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        self.x_position += self.movespeed * (self.weirdcontrols["D"] - self.weirdcontrols["A"])
        self.y_position += self.movespeed * (self.weirdcontrols["S"] - self.weirdcontrols["W"])
