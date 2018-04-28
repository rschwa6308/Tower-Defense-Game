from pygame.math import Vector2 as V2
import pygame as pg

from Images import *
from Projectiles import *
from ScreenConvert import *


class Tower:
    health_level = 1
    damage_level = 1
    speed_level = 1
    range_level = 1
    regen_level = 1
    x = None
    y = None

    last_attack_time = 0
    kills = 0

    hover = False
    selected = False

    aim_mode = "first"

    def get_upgrade_cost(self, attribute):
        if attribute == "health":
            return int(round(30 * self.health_level + 1.3 ** (self.health_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "damage":
            return int(round(30 * self.damage_level + 1.3 ** (self.damage_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "speed":
            return int(round(30 * self.speed_level + 1.3 ** (self.speed_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "range":
            return int(round(30 * self.range_level + 1.3 ** (self.range_level - 1), -1))  # 30x + 1.3^(x - 1)
        elif attribute == "regen":
            return int(round(100 * self.regen_level + 1.3 ** (self.regen_level - 1), -1))  # 100x + 1.3^(x - 1)

    def setPosition(self, pos):
        x = pos[0]
        y = pos[1]

        # print("x is: " + str(x) + " y is: " + str(y))

    def getPosition(self):
        return [x, y]


class Archer(Tower):
    name = "Archer"
    image = archer_image
    dims = (70 * widthRatio, 120 * heightRatio)
    base_center_pos = (35 * widthRatio, 104 * heightRatio)

    max_health = 20
    health = 20
    damage = 100
    cooldown = 1
    range = 250
    regen = 0
    damage_types = ['single']
    projectile = Arrow

    cost = 40

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if self.getLevel(attribute) < 15:
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
            elif attribute == "regen":
                self.regen_level += 1
                self.regen += 1
        else:
            print("Cannot upgrade " + attribute + " anymore")

    def getLevel(self, attribute):
        if attribute == "health":
            return self.health_level
        elif attribute == "damage":
            return self.damage_level
        elif attribute == "speed":
            return self.speed_level
        elif attribute == "range":
            return self.range_level
        elif attribute == "regen":
            return self.regen_level

    def get_loot_value(self):
        return self.cost + \
               10 * (self.health_level + self.damage_level + self.speed_level + self.range_level - 4) + \
               100 * (self.regen_level - 1)


class Mage(Tower):
    name = "Mage"
    image = mage_image
    dims = (70 * widthRatio, 120 * heightRatio)
    base_center_pos = (35 * widthRatio, 100 * heightRatio)

    max_health = 15
    health = 15
    damage = 200
    cooldown = 1
    range = 150
    regen = 0
    damage_types = ['splash']
    projectile = Beam

    cost = 60

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if self.getLevel(attribute) < 15:
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
            elif attribute == "regen":
                self.regen_level += 1
                self.regen += 1
        else:
            print("Cannot upgrade " + attribute + " anymore")

    def getLevel(self, attribute):
        if attribute == "health":
            return self.health_level
        elif attribute == "damage":
            return self.damage_level
        elif attribute == "speed":
            return self.speed_level
        elif attribute == "range":
            return self.range_level
        elif attribute == "regen":
            return self.regen_level

    def get_loot_value(self):
        return self.cost + \
               10 * (self.health_level + self.damage_level + self.speed_level + self.range_level - 4) + \
               100 * (self.regen_level - 1)


class Artillery(Tower):
    name = "Artillery"
    image = splash_image
    dims = (150 * widthRatio, 40 * heightRatio)
    base_center_pos = (int(119 / 2), int(35 / 2))

    max_health = 50
    health = 50
    damage = 200
    cooldown = 2
    range = 275
    regen = 0
    damage_types = ['splash']
    projectile = Beam

    cost = 100

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if self.getLevel(attribute) < 15:
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
            elif attribute == "regen":
                self.regen_level += 1
                self.regen += 1
        else:
            print("Cannot upgrade " + attribute + " anymore")

    def getLevel(self, attribute):
        if attribute == "health":
            return self.health_level
        elif attribute == "damage":
            return self.damage_level
        elif attribute == "speed":
            return self.speed_level
        elif attribute == "range":
            return self.range_level
        elif attribute == "regen":
            return self.regen_level

    def get_loot_value(self):
        return self.cost + \
               10 * (self.health_level + self.damage_level + self.speed_level + self.range_level - 4) + \
               100 * (self.regen_level - 1)


class Sniper(Tower):
    name = "Sniper"
    image = sniper_image
    dims = [180 * widthRatio, 96 * heightRatio]
    base_center_pos = (0, 15)

    max_health = 50
    health = 50
    damage = 200
    cooldown = 2
    range = 1000
    regen = 0
    damage_types = ['single']
    projectile = Bullet

    cost = 500

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def upgrade(self, attribute):
        if self.getLevel(attribute) < 15:
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
            elif attribute == "regen":
                self.regen_level += 1
                self.regen += 1
        else:
            print("Cannot upgrade " + attribute + " anymore")

    def getLevel(self, attribute):
        if attribute == "health":
            return self.health_level
        elif attribute == "damage":
            return self.damage_level
        elif attribute == "speed":
            return self.speed_level
        elif attribute == "range":
            return self.range_level
        elif attribute == "regen":
            return self.regen_level

    def get_loot_value(self):
        return self.cost + \
               10 * (self.health_level + self.damage_level + self.speed_level + self.range_level - 4) + \
               100 * (self.regen_level - 1)


class Wall(Tower):
    name = "Wall"
    image = wall_image
    dims = [20 * widthRatio, 20 * heightRatio]
    base_center_pos = (10, 10)

    max_health = 20
    health = 20
    damage = 0
    cooldown = 10000000000000000000
    range = 17
    regen = 0
    damage_types = ['single']
    projectile = None

    cost = 2

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.dims[0], self.dims[1])

    def get_loot_value(self):
        return 2


tower_types = [Archer, Mage, Artillery, Sniper, Wall]
