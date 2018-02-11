import pygame

from cosi_tbs import globals

#pygame.init()

import cosi_tbs
from cosi_tbs.screens import *

infoWindow = pygame.display.Info()
widthWindow = 1920
heightWindow = 1080
widthRatio = infoWindow.current_w / widthWindow
heightRatio = infoWindow.current_h / heightWindow
window = pygame.Surface((widthWindow, heightWindow)) #BLIT TO THIS
scaledWin = pygame.display.set_mode((infoWindow.current_w, infoWindow.current_h), pygame.FULLSCREEN)

while True:
    main_return = main_menu(window, scaledWin, (widthRatio, heightRatio))
    if main_return == 1:
        host_game()

