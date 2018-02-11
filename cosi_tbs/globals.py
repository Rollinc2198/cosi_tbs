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

def text_render(font_type, text, window, x, y, border):
    text_outline = font_type.render(text, True, black)

    window.blit(text_outline, [x - text_outline.get_width() / 2 - border, y + border])
    window.blit(text_outline, [x - text_outline.get_width() / 2 + border, y - border])
    window.blit(text_outline, [x - text_outline.get_width() / 2 - border, y - border])
    window.blit(text_outline, [x - text_outline.get_width() / 2 + border, y + border])
    window.blit(text_outline, [x - text_outline.get_width() / 2 - border, y])
    window.blit(text_outline, [x - text_outline.get_width() / 2 + border, y])
    window.blit(text_outline, [x - text_outline.get_width() / 2, y - border])
    window.blit(text_outline, [x - text_outline.get_width() / 2, y + border])
