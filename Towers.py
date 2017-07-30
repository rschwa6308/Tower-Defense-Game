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
    kills = 0

    hover = False
    selected = False

    aim_mode = "closest"

    def get_upgrade_cost(self, attribute):
        if attribute == "health":
            return int(round(30 * self.health_level + 1.3 ** (self.health_level - 1), -1)) # 30x + 1.3^(x - 1)
        elif attribute == "damage":
            return int(round(30 * self.damage_level + 1.3 ** (self.damage_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "speed":
            return int(round(30 * self.speed_level + 1.3 ** (self.speed_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "range":
            return int(round(30 * self.range_level + 1.3 ** (self.range_level - 1), -1))  # 30x + 1.3^(x - 1)


class Archer(Tower):
    name = "Archer"
    image = archer_image
    dims = (70, 120)
    base_center_pos = (35, 104)

    max_health = 20
    health = 20
    damage = 100
    cooldown = 1
    range = 250
    damage_types = ['single']
    projectile = Arrow

    cost = 40

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
            self.max_health *= 1.1
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
    dims = (70, 120)
    base_center_pos = (35, 100)

    max_health = 15
    health = 15
    damage = 200
    cooldown = 1
    range = 150
    damage_types = ['splash']
    projectile = Beam

    cost = 60

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
            self.max_health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
            self.cooldown *= 0.9
        elif attribute == "range":
            self.range_level += 1
            self.range = int(self.range * 1.1)


class Artillery(Tower):
    name = "Artillery"
    image = None

    max_health = 50
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
            self.max_health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
            self.cooldown *= 0.9
        elif attribute == "range":
            self.range_level += 1
            self.range = int(self.range * 1.1)


class Sniper(Tower):
    name = "Sniper"
    image = sniper_image
    dims = [180, 96]
    base_center_pos = (0, 15)

    max_health = 10
    health = 10
    damage = 200
    cooldown = 2
    range = 1000
    damage_types = ['single']
    projectile = Bullet

    cost = 500

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if attribute == "health":
            self.health_level += 1
            self.health *= 1.1
            self.max_health *= 1.1
        elif attribute == "damage":
            self.damage_level += 1
            self.damage *= 1.1
        elif attribute == "speed":
            self.speed_level += 1
            self.cooldown *= 0.9
        elif attribute == "range":
            self.range_level += 1
            self.range = int(self.range * 1.1)


tower_types = [Archer, Mage, Artillery, Sniper]
