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

    def __init__(self, type, _tint = (255,255,255), center = (700,450)):
        self.tint = _tint
        if type == "linearb":
            self.linearGradientBlue()
        elif type == "linearg":
            self.linearGradientGreen()
        elif type == "linearr":
            self.linearGradientRed()
        elif type == "circularb":
            self.circularGradientBlue(center)
        elif type == "circularg":
            self.circularGradientGreen(center)
        elif type == "circularr":
            self.circularGradientRed(center)
            
    def changeTint(self,_tint):
        tint = _tint
    def getImage(self):
        return self.background_image
    #the types of background image are just modifications of a pg surface
    def linearGradientBlue(self):
        for y in range(0, int(self.height)):
            n = y / self.height
            color = (int((1 - 3*n/4) * self.tint[0]), int((1 - 3*n/4) * self.tint[1]), self.tint[2])  # White -> Blue- now color to color editable through tint
            pg.draw.line(self.background_image, color, (0, y), (self.width, y), 1)
    
    def linearGradientGreen(self):
        for y in range(0, int(self.height)):
            n = y / self.height
            color = (int((1 - 3*n/4) * self.tint[0]),self.tint[1] , int((1 - 3*n/4) * self.tint[2]))  # White -> Green- now color to color editable through tint
            pg.draw.line(self.background_image, color, (0, y), (self.width, y), 1)
    def linearGradientRed(self):
        for y in range(0, int(self.height)):
            n = y / self.height
            color = (self.tint[1], int((1 - 3*n/4) * self.tint[1]), int((1 - 3*n/4) * self.tint[2]))  # White -> Red- now color to color editable through tint
            pg.draw.line(self.background_image, color, (0, y), (self.width, y), 1)
    
    def circularGradientBlue(self, basecenter):
        for radius in reversed(range(1, int((self.width +self.height)/2))):  #(700**2 + 450**2)**0.5)
            n = radius / ((self.width +self.height)/2)
            #print(n)
            color = (int((1 - n) * self.tint[0]), int((1 - n) * self.tint[1]), self.tint[2])             # White -> Blue
            pg.draw.circle(self.background_image, color, basecenter, radius, 0)
            
    def circularGradientGreen(self, basecenter):
        for radius in reversed(range(1, int((self.width +self.height)/2))):  #(700**2 + 450**2)**0.5)
            n = radius / ((self.width +self.height)/2)
            #print(n)
            color = (int((1 - n) * self.tint[0]), self.tint[1], int((1 - n) * self.tint[2]))             # White -> Green
            pg.draw.circle(self.background_image, color, basecenter, radius, 0)
            
    def circularGradientRed(self, basecenter):
        for radius in reversed(range(1, int((self.width +self.height)/2))):  #(700**2 + 450**2)**0.5)
            n = radius / ((self.width +self.height)/2)
            #print(n)
            color = (self.tint[0], int((1 - n) * self.tint[1]), int((1 - n) * self.tint[2]))             # White -> Blue
            pg.draw.circle(self.background_image, color, basecenter, radius, 0)
            