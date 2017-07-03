from random import *

from Enemies import *

test_wave = [Orc((randint(0, 1400), 0), (uniform(-1, 1), uniform(0, 10))) for _ in range(100)]