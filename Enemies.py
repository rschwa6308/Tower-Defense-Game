from pygame.math import Vector2 as V2
import math
from random import uniform

from Images import *


class Enemy:
    last_attack_time = 0

    def __init__(self, pos=None, vel=None):
        if pos:
            self.pos = V2(pos)
        else:
            self.pos = V2(0, 0)

        if vel:
            self.vel = V2(vel)
        else:
            self.vel = V2(0, 0)

        self.starting_vel = V2(self.vel)

    def get_center(self):
        return self.pos + self.center_pos

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 50, 50)

    def aim_at(self, target):
        displacement = target.base_center - self.pos
        self.vel = displacement.normalize() * self.speed

    def refresh_target(self, towers, base):
        non_walls = [t for t in towers if t.name != "Wall"]
        new_target = min(non_walls + [base], key=lambda x: (x.pos - self.pos).length_squared())  # length_squared faster
        self.aim_at(new_target)


class Orc(Enemy):
    name = "Orc"
    image = orc_image
    center_pos = (25, 25)

    speed = 2

    max_health = 120
    health = 120
    damage = 2
    cooldown = 2
    range = 50

    value = 10


class Tank(Enemy):
    name = "Tank"
    image = tank_image
    center_pos = (25, 25)

    speed = 1

    max_health = 500
    health = 500
    damage = 5
    cooldown = 3
    range = 50

    value = 30
