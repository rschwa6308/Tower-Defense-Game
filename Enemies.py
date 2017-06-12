import pygame as pg
from pygame.math import Vector2 as V2


class Enemy:
    pass


class Orc(Enemy):
    image = pg.Surface((50, 50))

    health = 20
    damage = 2
    speed = 1

    def __init__(self, pos):
        self.pos = V2(pos)
