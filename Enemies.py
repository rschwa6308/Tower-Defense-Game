from pygame.math import Vector2 as V2


class Enemy:
    pass


class Orc(Enemy):
    health = 20
    damage = 2
    speed = 1

    def __init__(self, pos):
        self.pos = V2(pos)
