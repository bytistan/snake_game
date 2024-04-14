import pygame 
from settings import *
from helper import read_json_file
from tail import Tail

class Snake(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-2,size-2))
        self.image.fill(color["snake"])
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.settings = read_json_file("./resources/settings/settings.json")
        self.direction.x = 1
        self.score = 2
        self.tail = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()

    def input(self):
        if self.rect.y % size == 0 and self.rect.x % size == 0:
            key = pygame.key.get_pressed()

            if key[pygame.K_UP] and self.direction.x != 0:
                self.direction.y = -1
                self.direction.x = 0
            elif key[pygame.K_DOWN] and self.direction.x != 0:
                self.direction.y = 1
                self.direction.x = 0
            elif key[pygame.K_LEFT] and self.direction.y != 0:
                self.direction.y = 0
                self.direction.x = -1
            elif key[pygame.K_RIGHT] and self.direction.y != 0:
                self.direction.y = 0
                self.direction.x = 1

    def tail_add(self):
        if self.rect.y % size == 0 and self.rect.x % size == 0:
            if len(self.tail.sprites()) < self.score:
                self.tail.add(Tail((self.rect.x,self.rect.y)))

    def tail_remove(self):
        if self.rect.y % size == 0 and self.rect.x % size == 0:
            if len(self.tail.sprites()) == self.score:
                self.tail.remove(self.tail.sprites()[0])

    def apply_speed(self):
        self.rect.x += self.direction.x * self.settings["speed"]
        self.rect.y += self.direction.y * self.settings["speed"]

    def update(self):
        self.tail_add()
        self.tail_remove()
        self.tail.draw(self.display_surface)
        self.input()
        self.apply_speed()