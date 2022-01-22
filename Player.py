import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_position = 0
        self.y_position = 0
        self.movespeed = 5
        self.sprites = []
        self.sprites.append(pygame.image.load('Reasources/pacman_1.gif'))
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

        self.x_position += self.movespeed * (Player_D - Player_A)
        self.y_position += self.movespeed * (Player_S - Player_W)


    def draw(self):
        window.blit(self.image, (self.x_position, self.y_position))
