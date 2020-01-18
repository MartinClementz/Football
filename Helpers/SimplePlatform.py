import pygame
class Platform():
    def __init__(self, width, height, x, y, name):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
