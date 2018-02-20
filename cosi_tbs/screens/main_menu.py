import pygame
from pygame.locals import *

from cosi_tbs.gui_objects import *
from cosi_tbs import globals


def main_menu(window, scaled_win, win_ratio):
    text = globals.fontTitle.render("COSI Turn-Based Strategy", True, globals.white)

    buttons = [
        Button(window, window.get_width() / 2 - Button.width / 2, 300, "Host Game"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + Button.height + 50, "Join Game"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + (Button.height + 50) * 2, "Settings"),
        Button(window, window.get_width() / 2 - Button.width / 2, 300 + (Button.height + 50) * 3, "Exit")
    ]
    all_sprites = []
    all_sprites.extend(buttons)

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
                pos_mouse = pygame.mouse.get_pos()
                pos_mouse = (pos_mouse[0] / win_ratio[0], pos_mouse[1] / win_ratio[1])

                # Handle Button Clicks
                for b in buttons:
                    if (pos_mouse[0] > b.x and pos_mouse[0] < b.x + b.width) and (
                            pos_mouse[1] > b.y and pos_mouse[1] < b.y + b.height):
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
        window.blit(globals.background, (0, 0))
        globals.text_render(globals.fontTitle, "COSI Turn-Based Strategy", window, window.get_width() / 2, 20, 5, True)
        window.blit(text, [window.get_width() / 2 - text.get_width() / 2, 20])
        for s in all_sprites:
            s.render()
        pygame.transform.smoothscale(window, scaled_win.get_size(), scaled_win)
        pygame.display.update()
        globals.clock.tick(60)
