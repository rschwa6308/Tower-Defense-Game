from pygame.math import Vector2 as V2
import pygame as pg

from Images import *


class Tower:
    health_level = 1
    damage_level = 1
    speed_level = 1
    range_level = 1

    last_attack_time = 0



class Archer(Tower):
    name = "Archer"
    image = archer_image
    base_center_pos = (35, 104)

    health = 20
    damage = 100
    cooldown = 1
    range = 150
    damage_types = ['single']

    def __init__(self, pos):
        self.pos = V2(pos)
        self.base_center = self.pos + self.base_center_pos
        self.rect = pg.Rect(self.pos.x, self.pos.y, 70, 120)





class Mage(Tower):
    name = "Mage"
    image = mage_image

    health = 15
    damage = 150
    cooldown = 4
    range = 150
    damage_types = ['splash']

    def __init__(self, pos):
        self.pos = V2(pos)


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

    def __init__(self, pos):
        self.pos = V2(pos)


tower_types = [Archer, Mage, Artillery]


if __name__ == "__main__":
    test_arrow = Archer((4, 7))
    test_arrow.health_level += 5
    print(test_arrow.health_level)