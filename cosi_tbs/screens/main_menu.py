import pygame
from pygame.locals import *

import cosi_tbs
from cosi_tbs.gui_objects import *

def main_menu(window, scaledWin):
    clock = pygame.time.Clock()

    winSize = window.get_size()

    buttons = [
        Button(0, 0, "Exit")
    ]

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
                posMouse = (posMouse[0] / winSize[0], posMouse[1] / winSize[1])

                # Handle Button Clicks
                for b in buttons:
                    if b.rect.collidepoint(posMouse):
                        if b.text == "Exit":
                            return

        # Updating
        window.fill((255, 255, 255))
        pygame.transform.smoothscale(window, scaledWin.get_size(), scaledWin)
        pygame.display.update()
        clock.tick(60)