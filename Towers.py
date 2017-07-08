from pygame.math import Vector2 as V2
import pygame as pg

from Images import *
from Projectiles import *


class Tower:
    health_level = 1
    damage_level = 1
    speed_level = 1
    range_level = 1

    last_attack_time = 0

    hover = False
    selected = False

    def get_upgrade_cost(self, attribute):
        if attribute == "health":
            return self.health_level * 10
        elif attribute == "damage":
            return self.damage_level * 10
        elif attribute == "speed":
            return self.speed_level * 10
        elif attribute == "range":
            return self.range_level * 10



class Archer(Tower):
    name = "Archer"
    image = archer_image
    base_center_pos = (35, 104)

    health = 20
    damage = 100
    cooldown = 1
    range = 250
    damage_types = ['single']
    projectile = Arrow

    cost = 20

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, 70, 120)

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
            self.cooldown *= 0.9
        elif attribute == "range":
            self.range_level += 1
            self.range = int(self.range * 1.1)





class Mage(Tower):
    name = "Mage"
    image = mage_image
    base_center_pos = (35, 100)

    health = 15
    damage = 200
    cooldown = 1
    range = 150
    damage_types = ['splash']
    projectile = Beam

    cost = 40

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, 70, 120)

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
        elif attribute == "range":
            self.range_level += 1


class EarthMage(Mage):
    def __init__(self, pos):
        super().__init__(pos)


class Artillery(Tower):
    name = "Artillery"
    image = None

    health = 50
    damage = 200
    cooldown = 2
    range = 150
    damage_types = ['splash']

    cost = 100

    def __init__(self, pos):
        self.pos = V2(pos)

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
        elif attribute == "range":
            self.range_level += 1


class Sniper(Tower):
    name = "Sniper"
    image = sniper_image
    base_center_pos = (35, 104)

    health = 10
    damage = 200
    cooldown = .02
    range = 1000
    damage_types = ['single']
    projectile = Bullet

    cost = 100

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, 70, 120)

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
        elif attribute == "range":
            self.range_level += 1


tower_types = [Archer, Mage, Artillery, Sniper]


if __name__ == "__main__":
    test_arrow = Archer((4, 7))
    test_arrow.health_level += 5
    print(test_arrow.health_level)