import pygame as pg
import os


background_image = pg.Surface((1400, 900))
for y in range(900):
    n = y / 900.0
    color = (int((1 - n) * 200), int((1 - n)*200), 255)
    pg.draw.line(background_image, color, (0, y), (1400, y), 1)

def load(name):
    return pg.image.load(os.path.join("Assets", name + ".png"))

archer_image = load("archer_tower")
mage_image = load("fire_mage_tower")
sniper_image = load("sniper_tower")

orc_image = load("orc")

arrow_image = load("arrow")
beam_image = load("beam")
bullet_image = load("bullet")