from pygame.math import Vector2 as V2
import math
from random import uniform

from Images import *


class Enemy:
    last_attack_time = 0.0
    distance_traveled = 0.0
    indexRange = 0
    vel = V2(0,0)

    def __init__(self, pos, vel):
        if pos == "edge":
            angle = uniform(0, 2 * math.pi)
            self.pos = V2(700 + 1200 * math.cos(angle), 450 + 1000 * math.sin(angle))
            self.pos += V2(uniform(-200, 200), uniform(-200, 200))
        else:
            self.pos = V2(pos)

        if vel == "random":
            angle = uniform(0, 2 * math.pi)
            a = V2((math.cos(angle), math.sin(angle)))
            self.vel = a / a.length() * self.speed  # Scale unit vector
        elif vel == "center":
            rel_pos = V2(self.pos.x - 700, self.pos.y - 450)
            rel_pos += V2(uniform(-150, 150), uniform(-150, 150))  # Introduce slight random variance
            self.vel = rel_pos / rel_pos.length() * self.speed * -1
        else:
            self.vel = V2(vel)
        self.starting_vel = V2(self.vel)
        

    def get_center(self):
        return self.pos + self.center_pos

    def get_rect(self):
        return pg.Rect(self.pos.x, self.pos.y, 50, 50)

    def setIndexRange(self, num):
        indexRange = num

    def getIndexRange(self):
        return indexRange
    
    '''def kill(self, array):
        self.health =0''' #thought needed don't but using something like this would be better
    
    
            
    
class Orc(Enemy):
    name = "Orc"
    image = orc_image
    center_pos = (25, 25)

    speed = 2

    max_health = 120
    health = 120
    damage = 1
    cooldown = 2
    range = 50

    value = 10


class Tank(Enemy):
    name = "Tank"
    image = tank_image
    center_pos = (25, 25)

    speed = 1.5

    max_health = 500
    health = 500
    damage = 3
    cooldown = 3
    range = 50

    value = 30

class BigBad(Enemy):
    name = "Big Bad"
    image = bb_image
    center_pos = (25, 25)

    speed = 1.25

    max_health = 1000
    health = 1000
    damage = 4
    cooldown = 2
    range = 50

    value = 50
