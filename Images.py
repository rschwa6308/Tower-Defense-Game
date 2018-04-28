import pygame as pg
import os


def load(name):
    return pg.image.load(os.path.join("Assets", name + ".png"))


base_image = load("base")

archer_image = load("archer_tower")
mage_image = load("fire_mage_tower")
sniper_image = load("sniper_tower")
wall_image = load("wall")

orc_image = load("orc")
tank_image = load("tank")

arrow_image = load("arrow")
beam_image = load("beam")
bullet_image = load("bullet")
