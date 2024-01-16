import pygame
from pygame.sprite import _Group

class Platfrom (pygame.sprite.Sprite):
    def __init__(self, *groups: _Group):
        super().__init__(*groups)






        screen.fill((0,0,0))