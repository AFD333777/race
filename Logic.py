import pygame
from Draw import Draw

FPS = 30


class Logic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 700))
        self.running = True
        self.clock = pygame.time.Clock()
        self.draw = Draw()
        self.draw.change_color(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.main_loop()
        pygame.quit()

    def main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
