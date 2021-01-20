import pygame


class Draw:
    def __init__(self):
        pygame.display.set_caption("Гонки")

    def change_color(self, screen):
        screen.fill(pygame.Color("Red"))
