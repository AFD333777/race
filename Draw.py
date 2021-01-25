import pygame
import os
import sys

STEP = 10


class Draw:
    def __init__(self, screen):
        pygame.display.set_caption("Гонки")
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Sprite()

    def drawHomeScreen(self):
        self.screen.fill((0, 0, 0))
        image = self.load_image(os.getcwd() + "/data/road.jpg")
        image1 = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image1, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 150, 300))
        pygame.draw.rect(self.screen, (0, 0, 255), (0, 0, 150, 300), 5)
        pygame.draw.rect(self.screen, (255, 0, 0), (300, 150, 220, 40), 0)
        pygame.draw.rect(self.screen, (255, 0, 0), (300, 200, 220, 40), 0)
        pygame.draw.rect(self.screen, (255, 255, 255), (300, 150, 220, 40), 1)
        pygame.draw.rect(self.screen, (255, 255, 255), (300, 200, 220, 40), 1)
        self.screen.blit(pygame.font.Font(None, 50).render("Начать игру", True, (0, 0, 255)), (310, 150))
        self.screen.blit(pygame.font.Font(None, 50).render("Race Escape", True, (0, 0, 255)), (300, 80))
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, (0, 0, 255)), (350, 200))
        self.screen.blit(pygame.font.Font(None, 30).render("Управление:", True, (0, 0, 255)), (5, 20))
        self.screen.blit(pygame.font.Font(None, 30).render("W - вперед", True, (0, 0, 255)), (5, 50))
        self.screen.blit(pygame.font.Font(None, 30).render("A - влево", True, (0, 0, 255)), (5, 80))
        self.screen.blit(pygame.font.Font(None, 30).render("D - вправо", True, (0, 0, 255)), (5, 110))
        self.screen.blit(pygame.font.Font(None, 30).render("SPACE - тормоз", True, (0, 0, 255)), (5, 140))
        pygame.display.flip()

    def load_image(self, name, colorkey=None):
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

    def drawField(self):
        image = self.load_image(os.getcwd() + "/data/road.jpg")
        image1 = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image1, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 150, 300))
        pygame.draw.rect(self.screen, (0, 0, 255), (0, 0, 150, 300), 5)
        pygame.display.flip()

    def drawCar(self, x, y):
        self.car.image = self.load_image("bluecar.png")
        self.car.image = pygame.transform.scale(self.car.image, (120, 120))
        self.car.rect = self.car.image.get_rect()
        self.all_sprites.add(self.car)
        self.car.rect.x = x
        self.car.rect.y = y
        self.all_sprites.draw(self.screen)

    def drawPauseScreen(self):
        self.screen.fill((0, 0, 0))
        image = self.load_image(os.getcwd() + "/data/road.jpg")
        image1 = pygame.transform.scale(image, (800, 600))
        self.screen.blit(image1, (0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0), (300, 150, 220, 40), 0)
        self.screen.blit(pygame.font.Font(None, 35).render("Продолжить игру", True, (0, 0, 255)), (302, 155))
        pygame.draw.rect(self.screen, (255, 255, 255), (300, 150, 220, 40), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (300, 200, 220, 40), 0)
        self.screen.blit(pygame.font.Font(None, 40).render("Выход в меню", True, (0, 0, 255)), (310, 205))
        pygame.draw.rect(self.screen, (255, 255, 255), (300, 200, 220, 40), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (300, 250, 220, 40), 0)
        self.screen.blit(pygame.font.Font(None, 50).render("Выход", True, (0, 0, 255)), (350, 252))
        pygame.draw.rect(self.screen, (255, 255, 255), (300, 250, 220, 40), 1)
        self.screen.blit(pygame.font.Font(None, 50).render("Race", True, (0, 0, 0)), (650, 20))
        self.screen.blit(pygame.font.Font(None, 50).render("Escape", True, (0, 0, 0)), (650, 60))
        self.screen.blit(pygame.font.Font(None, 50).render("Pause", True, (0, 255, 0)), (50, 30))
        pygame.display.flip()

    def baseSpeed(self):
        self.drawField()
        self.car.rect.y = self.car.rect.y - 2
        self.drawField()
        self.all_sprites.draw(self.screen)

    def boostSpeed(self):
        self.drawField()
        self.car.rect.y = self.car.rect.y - STEP
        self.drawField()
        self.all_sprites.draw(self.screen)

    def goRight(self):
        self.drawField()
        self.car.rect.x = self.car.rect.x + STEP
        self.drawField()
        self.all_sprites.draw(self.screen)

    def goLeft(self):
        self.drawField()
        self.car.rect.x = self.car.rect.x - STEP
        self.drawField()
        self.all_sprites.draw(self.screen)
