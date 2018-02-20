import threading
import pygame
import queue


class Escape(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)

        self.events = queue.Queue()

    def run(self):
        for e in self.events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    def set(self, events):
        self.events = events
