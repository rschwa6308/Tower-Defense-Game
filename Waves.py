from random import *

from Enemies import *

test_wave = [Orc(pos="edge", vel="center") for _ in range(50)]

waves = [
    [Orc(pos="edge", vel="center") for _ in range(3)],
    [Orc(pos="edge", vel="center") for _ in range(10)],
    [Orc(pos="edge", vel="center") for _ in range(30)] + [Tank(pos="edge", vel="center")]
]


# TODO: make enemy spawn location aware of screen size!!!
def get_wave(number):
    wave = [Orc(pos="edge", vel="center") for _ in range(6 * number)] + \
           [Tank(pos="edge", vel="center") for _ in range(1 * number)]

    return wave
