import pygame as pg
from pygame.math import Vector2 as V2
import math
from random import uniform

from Images import *


class Enemy:
    last_attack_time = 0


class Orc(Enemy):
    name = "Orc"
    image = orc_image
    center_pos = (25, 25)

    speed = 1

    max_health = 600
    health = 600
    damage = 2
    cooldown = 1
    range = 50

    value = 30

    def __init__(self, pos, vel=None):
        self.pos = V2(pos)
        if vel is not None:
            self.vel = V2(vel)
        else:
            angle = uniform(0, 2 * math.pi)
            a = V2((math.cos(angle), math.sin(angle)))
            self.vel = a / a.length() * self.speed          # Scale unit vector

    def get_center(self):
        return self.pos + self.center_pos

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 50, 50)
