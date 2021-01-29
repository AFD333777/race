import pygame
from Draw import Draw

FPS = 30


class Logic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.condStart = False
        self.condPause = False
        self.condBoost = False
        self.condLeft = False
        self.condRight = False
        self.clock = pygame.time.Clock()
        self.draw = Draw(self.screen)
        self.draw.drawHomeScreen()

    def run(self):
        while self.running:
            self.main_loop()
        pygame.quit()

    def startGame(self):
        self.condStart = True
        self.draw.drawField()
        self.draw.drawCar(400, 400)

    def resumeGame(self):
        self.draw.drawField()
        self.draw.drawCar(self.draw.car.rect.x, self.draw.car.rect.y)
        self.condStart = True
        self.condPause = False

    def pauseGame(self):
        self.draw.drawPauseScreen()
        self.condPause = True
        self.condStart = False

    def main_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if self.condPause:
                    if 300 <= xMouse <= 520 and 150 <= yMouse <= 190:
                        self.resumeGame()
                    if 300 <= xMouse <= 520 and 200 <= yMouse <= 240:
                        self.condStart = False
                        self.condPause = False
                        self.draw.drawHomeScreen()
                    if 300 <= xMouse <= 520 and 250 <= yMouse <= 290:
                        self.running = False
                elif self.condStart:
                    pass
                else:
                    if 300 <= xMouse <= 520 and 150 <= yMouse <= 190:
                        self.startGame()
                    if 300 <= xMouse <= 520 and 200 <= yMouse <= 240:
                        self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.condStart:
                        self.pauseGame()
                    elif self.condPause:
                        self.resumeGame()
                if event.key == pygame.K_w:
                    self.condBoost = True
                if event.key == pygame.K_a:
                    self.condLeft = True
                if event.key == pygame.K_d:
                    self.condRight = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.condBoost = False
                if event.key == pygame.K_a:
                    self.condLeft = False
                if event.key == pygame.K_d:
                    self.condRight = False
        if self.condStart:
            if self.condBoost:
                self.draw.boostSpeed()
            else:
                self.draw.baseSpeed()
            if self.condRight:
                self.draw.goRight()
            if self.condLeft:
                self.draw.goLeft()
            self.draw.updateScreen()
        pygame.display.flip()
        self.clock.tick(60)
