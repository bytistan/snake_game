import pygame 
from settings import *

class Tail(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-2,size-2))
        self.image.fill(color["snake"])
        self.rect = self.image.get_rect(topleft=pos)