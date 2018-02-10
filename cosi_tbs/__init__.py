import pygame
from pygame.locals import *

import cosi_tbs
from cosi_tbs.screens import main_menu

infoWindow = pygame.display.Info()
widthWindow = 1920
heightWindow = 1080
window = pygame.Surface((infoWindow.current_w / widthWindow, infoWindow.current_h / heightWindow)) #BLIT TO THIS
scaledWin = pygame.display.set_mode((infoWindow.current_w, infoWindow.current_h), pygame.FULLSCREEN)

main_menu(window, scaledWin)