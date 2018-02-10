import pygame
from pygame.locals import *

# Fonts
font = pygame.font.Font(None, 30)

class Button(object):
    color = (0, 0, 0)
    textColor = (255, 255, 255)
    width = 250
    height = 100

    def __init__(self, window, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.window = window

    def render(self):
        textSurface = font.render(self.text, True, self.textColor)
        pygame.draw.rect(self.window, (0, 0, 0), Rect(self.x, self.y, self.width, self.height))
        self.window.blit(textSurface, [self.x + self.width / 2 - textSurface.get_width() / 2,
                                  self.y + self.height / 2 - textSurface.get_height() / 2])