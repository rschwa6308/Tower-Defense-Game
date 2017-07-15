from random import *

from Enemies import *


test_wave = [Orc(pos="edge", vel="center") for _ in range(50)]


waves = [
    [Orc(pos="edge", vel="center") for _ in range(3)],
    [Orc(pos="edge", vel="center") for _ in range(10)],
    [Orc(pos="edge", vel="center") for _ in range(30)]
]
