from random import *

from Enemies import *

defined_waves = [
    [Orc() for _ in range(3)],
    [Orc() for _ in range(10)],
    [Orc() for _ in range(30)] + [Tank()]
]


# TODO: make enemy spawn location aware of screen size!!!
def get_wave(number, base, spawn_radius):
    if number <= len(defined_waves):
        wave = defined_waves[number - 1]
    else:
        wave = [Orc() for _ in range(6 * number)] + [Tank() for _ in range(1 * number)] + \
            [Runner() for _ in range(1 * number)]

    for e in wave:
        angle = uniform(0, 2 * math.pi)
        e.pos = V2(base.pos.x + spawn_radius * math.cos(angle), base.pos.y + spawn_radius * math.sin(angle))
        e.pos += V2(uniform(-200, 200), uniform(-200, 200))

    return wave
