import pygame 
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill(color["wall"])
        self.rect = self.image.get_rect(topleft=pos)