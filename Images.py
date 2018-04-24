import pygame as pg
import os

background_image = pg.Surface((1400, 900))
# Circular gradient
# for radius in reversed(range(1, int((700**2 + 450**2)**0.5))):
#     n = radius / 900.0
#     print(n)
#     color = (int((1 - n) * 200), int((1 - n) * 200), 255)             # White -> Blue
#     pg.draw.circle(background_image, color, (700, 450), radius, 0)
# Linear gradient
for y in range(900):
    n = y / 900.0
    color = (int((1 - n) * 200), int((1 - n) * 200), 255)  # White -> Blue
    pg.draw.line(background_image, color, (0, y), (1400, y), 1)


def load(name):
    return pg.image.load(os.path.join("Assets", name + ".png"))


base_image = load("base")

archer_image = load("archer_tower")
mage_image = load("fire_mage_tower")
sniper_image = load("sniper_tower")
wall_image = load("wall")
splash_image = load("splash")

orc_image = load("orc")
tank_image = load("tank")

arrow_image = load("arrow")
beam_image = load("beam")
bullet_image = load("bullet")
