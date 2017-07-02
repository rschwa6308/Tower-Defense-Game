import pygame.image as pgi
import os


def load(name):
    return pgi.load(os.path.join("Assets", name + ".png"))

archer_image = load("archer_tower")
mage_image = load("fire_mage_tower")

orc_image = load("orc")

arrow_image = load("arrow")
beam_image = load("beam")