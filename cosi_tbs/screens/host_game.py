import pygame
from pygame.locals import *

from cosi_tbs.gui_objects import *
from cosi_tbs import globals


def host_game(window, scaled_win, win_ratio):
    buttons = [
        Button(window, 10, 10, "Back to Main Menu"),
        Button(window, window.get_width() / 2 - Button.width / 2, window.get_height() - 200, "Submit")
    ]
    text_boxes = [
        TextBox(window, window.get_width() / 2 - TextBox.width / 2, window.get_height() / 2 - TextBox.height / 2, "Enter your username")
    ]
    all_sprites = []
    all_sprites.extend(buttons)
    all_sprites.extend(text_boxes)

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
                # Handle Text Box Clicks
                for t in text_boxes:
                    if (pos_mouse[0] > t.x and pos_mouse[0] < t.x + t.width) and (
                            pos_mouse[1] > t.y and pos_mouse[1] < t.y + t.height):
                        t.is_typing = True
                        for tt in text_boxes:
                            if not tt == t:
                                tt.is_typing = False
            if event.type == pygame.KEYDOWN:
                for t in text_boxes:
                    t.typing(event)

        window.blit(globals.background, (0, 0))
        for s in all_sprites:
            s.render()
        pygame.transform.smoothscale(window, scaled_win.get_size(), scaled_win)
        pygame.display.update()
        globals.clock.tick(60)
