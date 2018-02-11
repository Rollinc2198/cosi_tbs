import pygame
from pygame.locals import *

from cosi_tbs.gui_objects import *
from cosi_tbs import globals

def main_menu(window, scaledWin, winRatio):
    background = pygame.image.load("/home/carter/PycharmProjects/cosi_tbs/cosi_tbs/images/white.jpg")

    textTitle = globals.fontTitle.render("COSI Turn-Based Strategy", True, globals.white)
    textTitleOutline = globals.fontTitle.render("COSI Turn-Based Strategy", True, globals.black)

    buttons = [
        Button(window, window.get_width() / 2 - Button.width / 2, 300, "Host Game"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + Button.height + 50, "Join Game"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + (Button.height + 50) * 2, "Settings"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + (Button.height + 50) * 3, "Exit")
    ]
    allsprites = []
    allsprites.extend(buttons)

    while True:
        # Events
        for event in pygame.event.get():
            # Emergency Exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            # Checking Mouse Click
            if event.type == MOUSEBUTTONDOWN:
                # Detect Mouse Position
                posMouse = pygame.mouse.get_pos()
                posMouse = (posMouse[0] / winRatio[0], posMouse[1] / winRatio[1])

                # Handle Button Clicks
                for b in buttons:
                    if (posMouse[0] > b.x and posMouse[0] < b.x + b.width) and (posMouse[1] > b.y and posMouse[1] < b.y + b.height):
                        if b.text == "Host Game":
                            return 1
                        if b.text == "Join Game":
                            return 2
                        if b.text == "Settings":
                            return 3
                        if b.text == "Exit":
                            pygame.quit()
                            exit()

        # Updating
        window.blit(background, (0,0))
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 - 5, 25])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 + 5, 15])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 - 5, 15])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 + 5, 25])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 - 5, 20])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2 + 5, 20])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2, 15])
        window.blit(textTitleOutline, [window.get_width() / 2 - textTitleOutline.get_width() / 2, 25])
        window.blit(textTitle, [window.get_width() / 2 - textTitle.get_width() / 2, 20])
        for s in allsprites:
            s.render()
        pygame.transform.smoothscale(window, scaledWin.get_size(), scaledWin)
        pygame.display.update()
        globals.clock.tick(60)