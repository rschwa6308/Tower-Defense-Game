from random import *

from Enemies import *

# test_wave = [Orc(pos="edge", vel="center") for _ in range(50)]
#
#
# waves = [
#     [Orc(pos="edge", vel="center") for _ in range(3)],
#     [Orc(pos="edge", vel="center") for _ in range(10)],
#     [Orc(pos="edge", vel="center") for _ in range(30)] + [Tank(pos="edge", vel="center")]
# ]
#
# def get_wave(number):
#     return [Orc(pos="edge", vel="center") for _ in range(6 * number)] + \
#            [Tank(pos="edge", vel="center") for _ in range(1 * number)]

waves = [
     "o     " * 1,
     "o     " * 2,
     "o     " * 3,
     "o     " * 4,
     "o     " * 5,
     "ooo          " * 3,
     "o     " * 6,
     "o     " * 7,
     "o     " * 8,
     "ooo          " * 4,
     "o o o     " * 4,
     "o o o     " * 5,
     "ooo          " * 5,
     "o o o     " * 6,
    "o o o t " * 3,
    "o o o t " * 4,
    "o o o t " * 5,
    "ooo          " * 5,
    "otototototototototot",
    "tttttttttttttttttttt"
]


def get_wave(number):
    if number - 1 < len(waves):
        return waves[number - 1]
    else:
        return waves[-1] * (number + 2 - len(waves))
