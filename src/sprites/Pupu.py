import os
import pygame

direktory_name = os.path.dirname(__file__)


class Pupu(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            direktory_name, "assets", "pupu.jpg"))
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
