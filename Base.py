from pygame.math import Vector2 as V2
import pygame as pg

from Images import base_image


class Base:
    name = "Base"
    image = base_image
    dims = (150, 100)

    max_health = 10000
    health = 10000

    def __init__(self, center_pos):
        self.pos = V2(center_pos[0] - self.dims[0] / 2, center_pos[1] - self.dims[1] / 2)
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])