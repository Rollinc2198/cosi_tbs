import pygame
import os

pygame.init()

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
fontSub = pygame.font.Font(None, 50)
fontTitle = pygame.font.Font(None, 150)

black = (0, 0, 0)
white = (255, 255, 255)

background = pygame.image.load(os.path.join("images", "white.jpg"))

maxNameLength = 15

players = []
threads = []


def init():
    players.clear()
    threads.clear()


def text_render(font_type, text, window, x, y, border, center):
    text_outline = font_type.render(text, True, black)

    if center:
        x_sub = text_outline.get_width() / 2
    else:
        x_sub = 0

    window.blit(text_outline, [x - x_sub - border, y + border])
    window.blit(text_outline, [x - x_sub + border, y - border])
    window.blit(text_outline, [x - x_sub - border, y - border])
    window.blit(text_outline, [x - x_sub + border, y + border])
    window.blit(text_outline, [x - x_sub - border, y])
    window.blit(text_outline, [x - x_sub + border, y])
    window.blit(text_outline, [x - x_sub, y - border])
    window.blit(text_outline, [x - x_sub, y + border])
