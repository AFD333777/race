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
        self.condDrive = False
        self.clock = pygame.time.Clock()
        self.draw = Draw(self.screen)
        self.homeScreen = pygame.surface.Surface((800, 600))
        self.pauseScreen = pygame.surface.Surface((800, 600))
        self.draw.drawHomeScreen()

    def run(self):
        while self.running:
            self.main_loop()
        pygame.quit()

    def startGame(self):
        self.condStart = True
        self.draw.drawField()
        self.draw.drawCar(400, 400)
        # рисуем поле
        pass

    def resumeGame(self):
        # вернуть текущий результат
        self.draw.drawField()
        self.draw.drawCar(self.draw.car.rect.x, self.draw.car.rect.y)
        self.condStart = True
        self.condPause = False
        pass

    def pauseGame(self):
        self.draw.drawPauseScreen()
        self.condPause = True
        self.condStart = False
        # рисуем заставку
        # сохраняем текущий результат
        pass

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
                    self.condDrive = True
                if event.key == pygame.K_a:
                    self.draw.goLeft()
                if event.key == pygame.K_d:
                    self.draw.goRight()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.condDrive = False
        if self.condStart:
            if self.condDrive:
                self.draw.boostSpeed()
            else:
                self.draw.baseSpeed()
        pygame.display.flip()
        self.clock.tick(30)
