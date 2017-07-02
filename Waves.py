from random import *

from Enemies import *

test_wave = [Orc((randint(0, 1400), -50), (uniform(-1, 1), uniform(0, 1))) for _ in range(5)]