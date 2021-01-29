import pygame
import os
import sys

STEP = 3


class Draw:
    def __init__(self, screen):
        pygame.display.set_caption("Гонки")
        self.screen = screen
        self.carGroup = pygame.sprite.Group()
        self.roadside = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.car = pygame.sprite.Sprite()
        self.smokeleft = pygame.sprite.Sprite()
        self.smokeright = pygame.sprite.Sprite()
        self.cactus = pygame.sprite.Sprite()
        self.tree = pygame.sprite.Sprite()
        self.loadCar()
        self.loadRoadSide()
        self.road = pygame.transform.scale(
            self.loadImage(os.path.join(os.path.join(os.getcwd(), "data"), "road.jpg")), (500, 600))
        self.grass = pygame.transform.scale(
            self.loadImage(os.path.join(os.path.join(os.getcwd(), "data"), "grass.jpg")), (160, 600))

    def loadImage(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                pass
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def drawHomeScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.road, (160, 0))
        self.screen.blit(self.grass, (0, 0))
        self.screen.blit(self.grass, (650, 0))
        pygame.draw.rect(self.screen, (35, 104, 155), (0, 0, 160, 175))
        pygame.draw.rect(self.screen, (72, 126, 149), (0, 0, 160, 175), 5)
        pygame.draw.rect(self.screen, (35, 104, 155), (300, 150, 220, 40))
        pygame.draw.rect(self.screen, (35, 104, 155), (300, 200, 220, 40))
        pygame.draw.rect(self.screen, (72, 126, 149), (300, 150, 220, 40), 3)
        pygame.draw.rect(self.screen, (72, 126, 149), (300, 200, 220, 40), 3)
        pygame.draw.rect(self.screen, (35, 104, 155), (675, 40, 120, 60))
        pygame.draw.rect(self.screen, (0, 0, 255), (675, 40, 120, 60), 5)
        self.screen.blit(pygame.font.Font(None, 50).render("Начать игру", True, (244, 245, 219)), (310, 150))
        self.screen.blit(pygame.font.Font(None, 50).render("Race", True, (217, 218, 176)), (675, 40))
        self.screen.blit(pygame.font.Font(None, 50).render("Escape", True, (217, 218, 176)), (675, 70))
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, (244, 245, 219)), (350, 200))
        self.screen.blit(pygame.font.Font(None, 30).render("Управление:", True, (217, 218, 176)), (5, 20))
        self.screen.blit(pygame.font.Font(None, 30).render("W - вперед", True, (217, 218, 176)), (5, 50))
        self.screen.blit(pygame.font.Font(None, 30).render("A - влево", True, (217, 218, 176)), (5, 80))
        self.screen.blit(pygame.font.Font(None, 30).render("D - вправо", True, (217, 218, 176)), (5, 110))
        pygame.display.flip()

    def drawPauseScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.road, (160, 0))
        self.screen.blit(self.grass, (0, 0))
        self.screen.blit(self.grass, (650, 0))
        pygame.draw.rect(self.screen, (35, 104, 155), (300, 150, 220, 40))
        self.screen.blit(pygame.font.Font(None, 35).render("Продолжить игру", True, (244, 245, 219)), (302, 155))
        pygame.draw.rect(self.screen, (72, 126, 149), (300, 150, 220, 40), 3)
        pygame.draw.rect(self.screen, (35, 104, 155), (300, 200, 220, 40))
        self.screen.blit(pygame.font.Font(None, 40).render("Выход в меню", True, (244, 245, 219)), (310, 205))
        pygame.draw.rect(self.screen, (72, 126, 149), (300, 200, 220, 40), 3)
        pygame.draw.rect(self.screen, (35, 104, 155), (300, 250, 220, 40))
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, (244, 245, 219)), (350, 252))
        pygame.draw.rect(self.screen, (72, 126, 149), (300, 250, 220, 40), 3)
        pygame.draw.rect(self.screen, (35, 104, 155), (675, 40, 120, 60))
        pygame.draw.rect(self.screen, (0, 0, 255), (675, 40, 120, 60), 5)
        self.screen.blit(pygame.font.Font(None, 50).render("Race", True, (217, 218, 176)), (675, 40))
        self.screen.blit(pygame.font.Font(None, 50).render("Escape", True, (217, 218, 176)), (675, 70))
        self.screen.blit(pygame.font.Font(None, 50).render("Pause", True, (0, 255, 0)), (160, 30))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 150, 300))
        pygame.draw.rect(self.screen, (0, 0, 255), (0, 0, 150, 300), 5)
        pygame.display.flip()

    def drawField(self):
        self.screen.blit(self.road, (160, 0))
        self.screen.blit(self.grass, (0, 0))
        self.screen.blit(self.grass, (650, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 150, 300))
        pygame.draw.rect(self.screen, (0, 0, 255), (0, 0, 150, 300), 5)
        if self.tree.rect.y >= 600:
            self.drawRoadSide(10)
        else:
            self.drawRoadSide(self.tree.rect.y + 1)

    def loadCar(self):
        self.car.image = self.loadImage("mercedes.png")
        self.smokeleft.image = self.loadImage("smoke.png")
        self.smokeright.image = self.loadImage("smoke.png")
        self.car.image = pygame.transform.scale(self.car.image, (90, 150))
        self.smokeleft.image = pygame.transform.scale(self.smokeleft.image, (50, 50))
        self.smokeright.image = pygame.transform.scale(self.smokeright.image, (50, 50))
        self.car.rect = self.car.image.get_rect()
        self.smokeleft.rect = self.smokeleft.image.get_rect()
        self.smokeright.rect = self.smokeright.image.get_rect()
        self.carGroup.add(self.smokeleft)
        self.carGroup.add(self.smokeright)
        self.carGroup.add(self.car)

    def loadRoadSide(self):
        self.cactus.image = self.loadImage("cactus.png")
        self.tree.image = self.loadImage("tree.png")
        self.cactus.image = pygame.transform.scale(self.cactus.image, (120, 120))
        self.tree.image = pygame.transform.scale(self.tree.image, (120, 120))
        self.cactus.rect = self.cactus.image.get_rect()
        self.tree.rect = self.tree.image.get_rect()
        self.roadside.add(self.tree)

    def drawRoadSide(self, y):
        self.tree.rect.x = 660
        self.tree.rect.y = y
        self.roadside.draw(self.screen)

    def drawCar(self, x, y):
        self.car.rect.x = x
        self.car.rect.y = y
        self.smokeright.rect.x = x + 40
        self.smokeright.rect.y = y + 130
        self.smokeleft.rect.x = x + 5
        self.smokeleft.rect.y = y + 130
        self.carGroup.draw(self.screen)

    def baseSpeed(self):
        self.roadside.draw(self.screen)
        # рисуем растения сбоку
        # выкатываем препятствия

    def boostSpeed(self):
        self.car.rect.y = self.car.rect.y - STEP

    def goRight(self):
        self.car.rect.x = self.car.rect.x + STEP
        self.smokeright.rect.x = self.smokeright.rect.x + STEP
        self.smokeleft.rect.x = self.smokeleft.rect.x + STEP

    def goLeft(self):
        self.car.rect.x = self.car.rect.x - STEP
        self.smokeright.rect.x = self.smokeright.rect.x - STEP
        self.smokeleft.rect.x = self.smokeleft.rect.x - STEP

    def updateScreen(self):
        self.drawField()
        self.carGroup.draw(self.screen)
