import pygame as pg
import os
from ScreenConvert import *



def load(name):
    return pg.image.load(os.path.join("Assets", name + ".png"))


base_image = load("base")

archer_image = load("archer_tower")
mage_image = load("fire_mage_tower")
sniper_image = load("sniper_tower")
wall_image = load("wall")
splash_image = load("splash")

orc_image = load("orc")
# orc_image = load("orc2")
tank_image = load("tank")
bb_image = load("bb")

arrow_image = load("arrow")
beam_image = load("beam")
bullet_image = load("bullet")






class background_Image():
    width = 1400 * widthRatio * 1.2
    height = 900 * heightRatio
    background_image = pg.Surface((width, height))
    tint = (255,255,255) #This allows the color of the gradient to be changed somewhat(not fully else the function has to be changed)

    def __init__(self, type, _tint = (255,255,255)):
        self.tint = _tint
        if type == "linear":
            self.linearGradient()
        elif type == "circular":
            self.linearGradient()
        
    def changeTint(self,_tint):
        tint = _tint
    #the types of background image are just modifications of a pg surface
    def linearGradient(self):
        for y in range(int(self.height)):
            n = y / self.height
            color = (int((1 - 3*n/4) * self.tint[0]), int((1 - 3*n/4) * self.tint[1]), self.tint[2])  # White -> Blue- now color to color editatble through tint
            pg.draw.line(self.background_image, color, (0, y), (self.width, y), 1)

    def circularGradient(self):
        for radius in reversed(range(1, int((700**2 + 450**2)**0.5))):
            n = radius / 900.0
            #print(n)
            color = (int((1 - n) * 200), int((1 - n) * 200), 255)             # White -> Blue
            pg.draw.circle(self.background_image, color, (700, 450), radius, 0)
            