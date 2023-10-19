import pygame
import sys
from hero import MainCharacter

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("SpaceX by Karachevtsev")
    maincharacter = MainCharacter(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.rect.centerx += 1

        maincharacter.output()
        pygame.display.flip()


start_game()
