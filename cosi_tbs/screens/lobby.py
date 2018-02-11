import pygame
from pygame.locals import *

from cosi_tbs.gui_objects import *
from cosi_tbs import globals


def lobby(window, scaled_win, win_ratio):
    lobby_name = globals.fontSub.render(globals.players[0] + "'s Game", True, globals.white)
    host_title = globals.fontSub.render("Host:", True, globals.white)
    host_name = globals.fontSub.render(globals.players[0], True, globals.black)
    players_title = globals.fontSub.render("Players:", True, globals.white)

    buttons = [
        Button(window, 10, 10, "Back to Main Menu"),
        Button(window, window.get_width() - Button.width - 10, window.get_height() - Button.height - 10, "Start Game")
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
                        if b.text == "Back to Main Menu":
                            return 0
                        if b.text == "Start Game":
                            return 5

        window.blit(globals.background, (0, 0))

        globals.text_render(globals.fontSub, globals.players[0] + "'s Game", window, window.get_width() / 2, 20, 2, True)
        window.blit(lobby_name, [window.get_width() / 2 - lobby_name.get_width() / 2, 20])

        pygame.draw.rect(window, globals.black, Rect(window.get_width() / 2 - 375, window.get_height() / 2 - 320, 750, 640))
        box = pygame.draw.rect(window, globals.white, Rect(window.get_width() / 2 - 370, window.get_height() / 2 - 315, 740, 630))

        globals.text_render(globals.fontSub, "Host:", window, box.x + 10, box.y + 10, 1, False)
        window.blit(host_title, [box.x + 10, box.y + 10])
        window.blit(host_name, [box.x + 60, box.y + 50])
        globals.text_render(globals.fontSub, "Players:", window, box.x + 10, box.y + 100, 1, False)
        window.blit(players_title, [box.x + 10, box.y + 100])

        for s in all_sprites:
            s.render()

        pygame.transform.smoothscale(window, scaled_win.get_size(), scaled_win)
        pygame.display.update()
        globals.clock.tick(60)
