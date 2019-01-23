import pygame as pg
import os
from ScreenConvert import *

width = 1400 * widthRatio * 1.2
height = 900 * heightRatio

background_image = pg.Surface((width, height))

tint = (255,255,255) #This allows the color of the gradient to be changed somewhat(not fully else the function has to be changed)
# Circular gradient
# for radius in reversed(range(1, int((700**2 + 450**2)**0.5))):
#     n = radius / 900.0
#     print(n)
#     color = (int((1 - n) * 200), int((1 - n) * 200), 255)             # White -> Blue
#     pg.draw.circle(background_image, color, (700, 450), radius, 0)


# Linear gradient
for y in range(int(height)):
    n = y / height
    color = (int((1 - n) * tint[0]), int((1 - n) * tint[1]), tint[2])  # White -> Blue- now color to color editatble through tint
    pg.draw.line(background_image, color, (0, y), (width, y), 1)


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

arrow_image = load("arrow")
beam_image = load("beam")
bullet_image = load("bullet")
