import pygame
import os
import sys
import random

STEP = 3
COLOR_FONT = (244, 245, 219)
COLOR_INTERNAL_RECT = (35, 104, 155)
COLOR_EXTERNAL_RECT = (72, 126, 149)


class Draw:
    def __init__(self, screen):
        pygame.display.set_caption("Race Escape")
        self.screen = screen
        self.carGroup = pygame.sprite.Group()
        self.roadside = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.car = pygame.sprite.Sprite()
        self.smokeleft = pygame.sprite.Sprite()
        self.smokeright = pygame.sprite.Sprite()
        self.cactus = pygame.sprite.Sprite()
        self.tree = pygame.sprite.Sprite()
        self.barrier = pygame.sprite.Sprite()
        self.box = pygame.sprite.Sprite()
        self.enemyCar = pygame.sprite.Sprite()
        self.score = 0
        self.countStars = 0
        self.loadCar()
        self.loadRoadSide()
        self.loadBarriers()
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
        self.drawBackground()
        self.drawHomeScreenButtons()
        self.drawTutorial()
        self.drawLogo()
        pygame.display.flip()

    def drawPauseScreen(self):
        self.drawBackground()
        self.drawPauseScreenButtons()
        self.screen.blit(pygame.font.Font(None, 30).render(f"Score - {self.score}", True, COLOR_FONT), (10, 20))
        self.screen.blit(pygame.font.Font(None, 50).render("Pause", True, (0, 255, 0)), (10, 50))
        pygame.display.flip()

    def drawBackground(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.road, (160, 0))
        self.screen.blit(self.grass, (0, 0))
        self.screen.blit(self.grass, (650, 0))

    def drawLogo(self):
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (675, 40, 120, 60))
        pygame.draw.rect(self.screen, (0, 0, 255), (675, 40, 120, 60), 5)
        self.screen.blit(pygame.font.Font(None, 50).render("Race", True, COLOR_FONT), (675, 40))
        self.screen.blit(pygame.font.Font(None, 50).render("Escape", True, COLOR_FONT), (675, 70))

    def drawHomeScreenButtons(self):
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (300, 150, 220, 40))
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (300, 200, 220, 40))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (300, 150, 220, 40), 3)
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (300, 200, 220, 40), 3)
        self.screen.blit(pygame.font.Font(None, 50).render("Начать игру", True, COLOR_FONT), (310, 150))
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, COLOR_FONT), (350, 200))

    def drawPauseScreenButtons(self):
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (300, 150, 220, 40))
        self.screen.blit(pygame.font.Font(None, 35).render("Продолжить игру", True, COLOR_FONT), (302, 155))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (300, 150, 220, 40), 3)
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (300, 200, 220, 40))
        self.screen.blit(pygame.font.Font(None, 40).render("Выход в меню", True, COLOR_FONT), (310, 205))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (300, 200, 220, 40), 3)
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (300, 250, 220, 40))
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, COLOR_FONT), (350, 252))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (300, 250, 220, 40), 3)
        self.drawLogo()
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (0, 0, 160, 100))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (0, 0, 160, 100), 5)

    def drawTutorial(self):
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (0, 0, 160, 175))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (0, 0, 160, 175), 5)
        self.screen.blit(pygame.font.Font(None, 30).render("Управление:", True, COLOR_FONT), (5, 20))
        self.screen.blit(pygame.font.Font(None, 30).render("W - вперед", True, COLOR_FONT), (5, 50))
        self.screen.blit(pygame.font.Font(None, 30).render("S - назад", True, COLOR_FONT), (5, 80))
        self.screen.blit(pygame.font.Font(None, 30).render("A - влево", True, COLOR_FONT), (5, 110))
        self.screen.blit(pygame.font.Font(None, 30).render("D - вправо", True, COLOR_FONT), (5, 140))

    def drawFinishScreen(self):
        self.drawBackground()
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (160, 100, 490, 150))
        pygame.draw.rect(self.screen, (0, 0, 255), (160, 100, 490, 150), 5)
        self.drawLogo()
        self.screen.blit(pygame.font.Font(None, 50).render("Игра закончена!", True, COLOR_FONT), (275, 110))
        self.screen.blit(pygame.font.Font(None, 30).render(f"Ваш результат - {self.score}", True, COLOR_FONT),
                         (325, 150))
        self.screen.blit(
            pygame.font.Font(None, 30).render("Для выхода в главное меню нажмите пробел..", True, COLOR_FONT),
            (175, 200))

    def drawField(self):
        self.drawBackground()
        pygame.draw.rect(self.screen, COLOR_INTERNAL_RECT, (0, 0, 160, 100))
        pygame.draw.rect(self.screen, COLOR_EXTERNAL_RECT, (0, 0, 160, 100), 5)
        self.screen.blit(pygame.font.Font(None, 30).render(f"Score - {self.score}", True, COLOR_FONT), (10, 20))
        self.screen.blit(pygame.font.Font(None, 25).render(f"Собрано звезд - {self.countStars}", True, COLOR_FONT),
                         (5, 45))

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
        self.roadside.add(random.choice([self.tree, self.cactus]))

    def loadBarriers(self):
        self.barrier.image = self.loadImage("barrier.png")
        self.box.image = self.loadImage("box.jpg")
        self.enemyCar.image = self.loadImage("redcar.png")
        self.barrier.image = pygame.transform.scale(self.barrier.image, (75, 75))
        self.box.image = pygame.transform.scale(self.box.image, (80, 80))
        self.enemyCar.image = pygame.transform.scale(self.enemyCar.image, (140, 140))
        self.barrier.rect = self.barrier.image.get_rect()
        self.box.rect = self.box.image.get_rect()
        self.enemyCar.rect = self.enemyCar.image.get_rect()
        self.getRandomCoords()
        self.barriers.add(self.barrier)
        self.barriers.add(self.box)
        self.barriers.add(self.enemyCar)

    def drawRoadSide(self, y):
        self.roadside.sprites().pop().rect.x = 660
        self.roadside.sprites().pop().rect.y = y
        self.roadside.draw(self.screen)

    def checkCollide(self):
        if not (pygame.sprite.collide_mask(self.car, self.barrier) or
                pygame.sprite.collide_mask(self.car, self.enemyCar) or
                pygame.sprite.collide_mask(self.car, self.box)):
            return True
        return False

    def getRandomCoords(self):
        coords = [(160, 10), (560, 10), (290, 10), (400, 10)]
        random.shuffle(coords)
        self.enemyCar.rect.x, self.enemyCar.rect.y = coords.pop()
        self.box.rect.x, self.box.rect.y = coords.pop()
        self.barrier.rect.x, self.barrier.rect.y = coords.pop()

    def drawBarriers(self, condNew):
        if condNew:
            self.getRandomCoords()
        else:
            for elem in self.barriers.sprites():
                elem.rect.y += 3
        self.barriers.draw(self.screen)

    def drawCar(self, x, y):
        self.car.rect.x = x
        self.car.rect.y = y
        self.smokeright.rect.x = x + 40
        self.smokeright.rect.y = y + 130
        self.smokeleft.rect.x = x + 5
        self.smokeleft.rect.y = y + 130
        self.carGroup.draw(self.screen)

    def baseSpeed(self):
        self.updateScreen()
        if self.roadside.sprites().pop().rect.y >= 600:
            self.roadside.empty()
            self.roadside.add(random.choice([self.tree, self.cactus]))
            self.drawRoadSide(10)
        else:
            self.drawRoadSide(self.roadside.sprites().pop().rect.y + 2)
        if self.enemyCar.rect.y >= 600:
            self.drawBarriers(True)
            self.score += 1
        else:
            self.drawBarriers(False)

    def goForward(self):
        if self.car.rect.y != 175:
            self.car.rect.y = self.car.rect.y - STEP
            self.smokeright.rect.y = self.smokeright.rect.y - STEP
            self.smokeleft.rect.y = self.smokeleft.rect.y - STEP

    def goRight(self):
        if self.car.rect.x != 565:
            self.car.rect.x = self.car.rect.x + STEP
            self.smokeright.rect.x = self.smokeright.rect.x + STEP
            self.smokeleft.rect.x = self.smokeleft.rect.x + STEP

    def goLeft(self):
        if self.car.rect.x != 145:
            self.car.rect.x = self.car.rect.x - STEP
            self.smokeright.rect.x = self.smokeright.rect.x - STEP
            self.smokeleft.rect.x = self.smokeleft.rect.x - STEP

    def goBack(self):
        if self.smokeright.rect.y != 560:
            self.car.rect.y = self.car.rect.y + STEP
            self.smokeright.rect.y = self.smokeright.rect.y + STEP
            self.smokeleft.rect.y = self.smokeleft.rect.y + STEP

    def updateScreen(self):
        self.drawField()
        self.carGroup.draw(self.screen)
