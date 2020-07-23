import pygame

class Ball:
    def __init__(self, image = pygame.image.load("cat.png"), speed = [1, 1]):
        self.image = image
        self.speed = speed
