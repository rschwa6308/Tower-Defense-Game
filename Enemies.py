import pygame as pg
from pygame.math import Vector2 as V2

from Images import *

class Enemy:
    last_attack_time = 0


class Orc(Enemy):
    name = "Orc"
    image = orc_image
    center_pos = (25, 25)

    max_health = 600
    health = 600
    damage = 2
    cooldown = 1
    range = 50

    def __init__(self, pos):
        self.pos = V2(pos)
        self.vel = V2((1, 1))

    def get_center(self):
        return self.pos + self.center_pos
