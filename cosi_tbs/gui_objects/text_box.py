import pygame
from pygame.locals import *

from cosi_tbs import globals


class TextBox(pygame.sprite.Sprite):
    width = 500
    height = 50

    def __init__(self, window, x, y, label):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        self.text = ""
        self.x = x
        self.y = y
        self.window = window
        self.is_typing = False
        self.label = label
        self.window = window
        self.title = globals.fontSub.render(self.label, True, globals.white)

    def typing(self, event):
            if self.is_typing:
                if event.type == pygame.KEYDOWN:
                    mods = pygame.key.get_mods()

                    if len(self.text) < globals.maxNameLength:
                        if mods & pygame.KMOD_SHIFT or mods & pygame.KMOD_CAPS:
                            if event.key == K_a:
                                self.text += "A"
                            if event.key == K_b:
                                self.text += "B"
                            if event.key == K_c:
                                self.text += "C"
                            if event.key == K_d:
                                self.text += "D"
                            if event.key == K_e:
                                self.text += "E"
                            if event.key == K_f:
                                self.text += "F"
                            if event.key == K_g:
                                self.text += "G"
                            if event.key == K_h:
                                self.text += "H"
                            if event.key == K_i:
                                self.text += "I"
                            if event.key == K_j:
                                self.text += "J"
                            if event.key == K_k:
                                self.text += "K"
                            if event.key == K_l:
                                self.text += "L"
                            if event.key == K_m:
                                self.text += "M"
                            if event.key == K_n:
                                self.text += "N"
                            if event.key == K_o:
                                self.text += "O"
                            if event.key == K_p:
                                self.text += "P"
                            if event.key == K_q:
                                self.text += "Q"
                            if event.key == K_r:
                                self.text += "R"
                            if event.key == K_s:
                                self.text += "S"
                            if event.key == K_t:
                                self.text += "T"
                            if event.key == K_u:
                                self.text += "U"
                            if event.key == K_v:
                                self.text += "V"
                            if event.key == K_w:
                                self.text += "W"
                            if event.key == K_x:
                                self.text += "X"
                            if event.key == K_y:
                                self.text += "Y"
                            if event.key == K_z:
                                self.text += "Z"
                            if mods & pygame.KMOD_CAPS:
                                if event.key == K_BACKQUOTE:
                                    self.text += "`"
                                if event.key == K_1:
                                    self.text += "1"
                                if event.key == K_2:
                                    self.text += "2"
                                if event.key == K_3:
                                    self.text += "3"
                                if event.key == K_4:
                                    self.text += "4"
                                if event.key == K_5:
                                    self.text += "5"
                                if event.key == K_6:
                                    self.text += "6"
                                if event.key == K_7:
                                    self.text += "7"
                                if event.key == K_8:
                                    self.text += "8"
                                if event.key == K_9:
                                    self.text += "9"
                                if event.key == K_0:
                                    self.text += "0"
                                if event.key == K_UNDERSCORE:
                                    self.text += "_"
                                if event.key == K_EQUALS:
                                    self.text += "="
                                if event.key == K_LEFTBRACKET:
                                    self.text += "["
                                if event.key == K_RIGHTBRACKET:
                                    self.text += "]"
                                if event.key == K_BACKSLASH:
                                    self.text += "\\"
                                if event.key == K_SEMICOLON:
                                    self.text += ";"
                                if event.key == K_QUOTE:
                                    self.text += "'"
                                if event.key == K_COMMA:
                                    self.text += ","
                                if event.key == K_PERIOD:
                                    self.text += "."
                                if event.key == K_SLASH:
                                    self.text += "/"
                            if mods & pygame.KMOD_SHIFT:
                                if event.key == K_BACKQUOTE:
                                    self.text += "~"
                                if event.key == K_1:
                                    self.text += "!"
                                if event.key == K_2:
                                    self.text += "@"
                                if event.key == K_3:
                                    self.text += "#"
                                if event.key == K_4:
                                    self.text += "$"
                                if event.key == K_5:
                                    self.text += "%"
                                if event.key == K_6:
                                    self.text += "^"
                                if event.key == K_7:
                                    self.text += "&"
                                if event.key == K_8:
                                    self.text += "*"
                                if event.key == K_9:
                                    self.text += "("
                                if event.key == K_0:
                                    self.text += ")"
                                if event.key == K_UNDERSCORE:
                                    self.text += "_"
                                if event.key == K_EQUALS:
                                    self.text += "+"
                                if event.key == K_LEFTBRACKET:
                                    self.text += "{"
                                if event.key == K_RIGHTBRACKET:
                                    self.text += "}"
                                if event.key == K_BACKSLASH:
                                    self.text += "|"
                                if event.key == K_SEMICOLON:
                                    self.text += ":"
                                if event.key == K_QUOTE:
                                    self.text += "\""
                                if event.key == K_COMMA:
                                    self.text += "<"
                                if event.key == K_PERIOD:
                                    self.text += ">"
                                if event.key == K_SLASH:
                                    self.text += "?"
                        else:
                            if event.key == K_a:
                                self.text += "a"
                            if event.key == K_b:
                                self.text += "b"
                            if event.key == K_c:
                                self.text += "c"
                            if event.key == K_d:
                                self.text += "d"
                            if event.key == K_e:
                                self.text += "e"
                            if event.key == K_f:
                                self.text += "f"
                            if event.key == K_g:
                                self.text += "g"
                            if event.key == K_h:
                                self.text += "h"
                            if event.key == K_i:
                                self.text += "i"
                            if event.key == K_j:
                                self.text += "j"
                            if event.key == K_k:
                                self.text += "k"
                            if event.key == K_l:
                                self.text += "l"
                            if event.key == K_m:
                                self.text += "m"
                            if event.key == K_n:
                                self.text += "n"
                            if event.key == K_o:
                                self.text += "o"
                            if event.key == K_p:
                                self.text += "p"
                            if event.key == K_q:
                                self.text += "q"
                            if event.key == K_r:
                                self.text += "r"
                            if event.key == K_s:
                                self.text += "s"
                            if event.key == K_t:
                                self.text += "t"
                            if event.key == K_u:
                                self.text += "u"
                            if event.key == K_v:
                                self.text += "v"
                            if event.key == K_w:
                                self.text += "w"
                            if event.key == K_x:
                                self.text += "x"
                            if event.key == K_y:
                                self.text += "y"
                            if event.key == K_z:
                                self.text += "z"
                            if event.key == K_BACKQUOTE:
                                self.text += "`"
                            if event.key == K_1:
                                self.text += "1"
                            if event.key == K_2:
                                self.text += "2"
                            if event.key == K_3:
                                self.text += "3"
                            if event.key == K_4:
                                self.text += "4"
                            if event.key == K_5:
                                self.text += "5"
                            if event.key == K_6:
                                self.text += "6"
                            if event.key == K_7:
                                self.text += "7"
                            if event.key == K_8:
                                self.text += "8"
                            if event.key == K_9:
                                self.text += "9"
                            if event.key == K_0:
                                self.text += "0"
                            if event.key == K_UNDERSCORE:
                                self.text += "_"
                            if event.key == K_EQUALS:
                                self.text += "="
                            if event.key == K_LEFTBRACKET:
                                self.text += "["
                            if event.key == K_RIGHTBRACKET:
                                self.text += "]"
                            if event.key == K_BACKSLASH:
                                self.text += "\\"
                            if event.key == K_SEMICOLON:
                                self.text += ";"
                            if event.key == K_QUOTE:
                                self.text += "'"
                            if event.key == K_COMMA:
                                self.text += ","
                            if event.key == K_PERIOD:
                                self.text += "."
                            if event.key == K_SLASH:
                                self.text += "/"

                        if mods & pygame.KMOD_NUM:
                            if event.key == K_KP0:
                                self.text += "0"
                            if event.key == K_KP1:
                                self.text += "1"
                            if event.key == K_KP2:
                                self.text += "2"
                            if event.key == K_KP3:
                                self.text += "3"
                            if event.key == K_KP4:
                                self.text += "4"
                            if event.key == K_KP5:
                                self.text += "5"
                            if event.key == K_KP6:
                                self.text += "6"
                            if event.key == K_KP7:
                                self.text += "7"
                            if event.key == K_KP8:
                                self.text += "8"
                            if event.key == K_KP9:
                                self.text += "9"
                            if event.key == K_KP_EQUALS:
                                self.text += "="
                            if event.key == K_KP_PERIOD:
                                self.text += "."

                        if event.key == K_SPACE:
                            self.text += " "
                        if event.key == K_KP_DIVIDE:
                            self.text += "/"
                        if event.key == K_KP_MULTIPLY:
                            self.text += "*"
                        if event.key == K_KP_MINUS:
                            self.text += "-"
                        if event.key == K_KP_PLUS:
                            self.text += "+"
                    if event.key == K_BACKSPACE:
                        self.text = self.text[0:len(self.text) - 1]
                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        self.is_typing = False

    def render(self):
        globals.text_render(globals.fontSub, self.label, self.window, self.window.get_width() / 2, self.y - self.title.get_height() - 10, 2, True)
        self.window.blit(self.title, [self.window.get_width() / 2 - self.title.get_width() / 2, self.y - self.title.get_height() - 10])
        text_surface = globals.font.render(self.text, True, globals.black)
        pygame.draw.rect(self.window, globals.black, Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.window, globals.white, Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        self.window.blit(text_surface, [self.x + self.width / 2 - text_surface.get_width() / 2,
                                        self.y + self.height / 2 - text_surface.get_height() / 2])
