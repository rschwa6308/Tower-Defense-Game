from random import *

from Enemies import *


test_wave = [Orc((randint(0, 1400), 0)) for _ in range(10)]

waves = [
    [Orc((randint(0, 1400), 0)) for _ in range(3)],
    [Orc((randint(0, 1400), 0)) for _ in range(10)],
    [Orc((randint(0, 1400), 0)) for _ in range(30)]
]
