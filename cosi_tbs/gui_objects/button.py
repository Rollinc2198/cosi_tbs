import pygame
from pygame.locals import *

from cosi_tbs import globals


class Button(pygame.sprite.Sprite):
    width = 250
    height = 100

    def __init__(self, window, x, y, text):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.text = text
        self.window = window

    def render(self):
        text_surface = globals.font.render(self.text, True, globals.black)
        pygame.draw.rect(self.window, globals.black, Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.window, globals.white, Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        self.window.blit(text_surface, [self.x + self.width / 2 - text_surface.get_width() / 2,
                                        self.y + self.height / 2 - text_surface.get_height() / 2])
