import pygame
import sys
import random
from Ghost import Ghost
from Point import Point
from Player import Player


def main():

    width = 464
    hight = 512
    window = pygame.display.set_mode((width, hight))
    pygame.display.set_caption('PacMan')
    FPS = 60
    clock = pygame.time.Clock()
    player_controls = {

        "W" : False,
        "A" : False,
        "S" : False,
        "D" : False,

    }

    player_controls["W"]

    background = pygame.image.load("Reasources/Background.jpg")



    all_sprites = pygame.sprite.Group()
    ghost = Ghost(2)
    player = Player()
    ghost.rect.x = 130
    ghost.rect.y = 120
    player.rect.x = 130
    player.rect.y = 30
    all_sprites.add(player)
    all_sprites.add(ghost)
    while True:
        #allows user to exit the screen
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

        #if event.type == pygame.KEY_DOWN:
            #then turn the sprite
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                player_controls["W"]
                #reference value of the dictionary

            if event.type == pygame.K_DOWN:
                player_controls["S"]

            if event.type == pygame.K_LEFT:
                player_controls["A"]

            if event.type == pygame.K_RIGHT:
                player_controls["D"]



        if event.type == pygame.KEYUP:
            if event.type == pygame.K_UP:


            if event.type == pygame.K_DOWN:


            if event.type == pygame.K_LEFT:


            if event.type == pygame.K_RIGHT:



        window.blit(background, (0, 0))
        clock.tick(60)
        all_sprites.update(0.25)#the number is there to change the speed of the animation of pacman
        all_sprites.draw(window)
        player.draw()
        pygame.display.flip()
        pygame.display.update()











if __name__ == "__main__":
    main()
