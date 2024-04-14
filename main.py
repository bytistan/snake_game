import pygame
from settings import *
from menu import Menu

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.menu = Menu()

    def animation(self):
        self.screen.fill(color["page_background"])

    def update(self):
        self.menu.update()

    def run(self):
        while True:
            self.clock.tick(fps)
            self.animation()
            self.update()
            pygame.display.flip()

if __name__ == "__main__":
    main = Main()
    main.run()