import pygame

from cosi_tbs import globals

import cosi_tbs
from cosi_tbs.screens import *

infoWindow = pygame.display.Info()
widthWindow = 1920
heightWindow = 1080
widthRatio = infoWindow.current_w / widthWindow
heightRatio = infoWindow.current_h / heightWindow
# Blit to this
window = pygame.Surface((widthWindow, heightWindow))
scaledWin = pygame.display.set_mode((infoWindow.current_w, infoWindow.current_h), pygame.FULLSCREEN)

# Variable to handle screen switching
screen = 0

while True:
    if screen == 0:
        screen = main_menu(window, scaledWin, (widthRatio, heightRatio))
    elif screen == 1:
        screen = host_game(window, scaledWin, (widthRatio, heightRatio))
