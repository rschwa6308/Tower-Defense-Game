from pygame.math import Vector2 as V2
import pygame as pg

from Images import *


class Projectile:
    def __init__(self, pos, vel, damage):
        self.pos = V2(pos)
        self.vel = V2(vel)
        self.damage = damage


class Arrow(Projectile):
    image = arrow_image
    center_pos = (10, 10)

    speed = 8

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 20, 20)


class Beam(Projectile):
    image = beam_image
    center_pos = (10, 10)

    speed = 8

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 20, 20)


class Bullet(Projectile):
    image = bullet_image
    center_pos = (10, 10)

    speed = 25

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 20, 20)
