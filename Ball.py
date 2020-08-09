import pygame

class Ball:
    def __init__(self, image = pygame.image.load("cat.png"), speed = [1, 1]):
        self.image = image
        self.speed = speed
        self.rect = image.get_rect()

    def tint(self, val):
        # alphaConvImage = self.image.convert_alpha()

        switcher = {
            0: self.image.convert_alpha().fill((190, 0, 0, 100), None, pygame.BLEND_RGBA_ADD),
            1: self.image.convert_alpha().fill((0, 190, 0, 100), None, pygame.BLEND_RGBA_ADD),
            2: self.image.convert_alpha().fill((0, 0, 190, 100), None, pygame.BLEND_RGBA_ADD)
        }

        self.image = switcher.get(val)
