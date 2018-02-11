import pygame

pygame.init()

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
fontSub = pygame.font.Font(None, 50)
fontTitle = pygame.font.Font(None, 150)

black = (0, 0, 0)
white = (255, 255, 255)

background = pygame.image.load("/home/carter/PycharmProjects/cosi_tbs/cosi_tbs/images/white.jpg")

maxNameLength = 15

players = []
threads = []


def init():
    players.clear()
    threads.clear()


def text_render(font_type, text, window, x, y, border, center):
    text_outline = font_type.render(text, True, black)

    if center:
        xSub = text_outline.get_width() / 2
    else:
        xSub = 0

    window.blit(text_outline, [x - xSub - border, y + border])
    window.blit(text_outline, [x - xSub + border, y - border])
    window.blit(text_outline, [x - xSub - border, y - border])
    window.blit(text_outline, [x - xSub + border, y + border])
    window.blit(text_outline, [x - xSub - border, y])
    window.blit(text_outline, [x - xSub + border, y])
    window.blit(text_outline, [x - xSub, y - border])
    window.blit(text_outline, [x - xSub, y + border])
