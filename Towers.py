
class Tower:
    def __init__(self):
        self.health_level = 1
        self.damage_level = 1
        self.speed_level = 1
        self.damage_types = []


class Arrow(Tower):
    name = "Arrow"

    def __init__(self):
        super(Arrow, self).__init__()
        self.health = 20
        self.damage = 100
        self.speed = 5
        self.damage_types = ['single']


<<<<<<< HEAD
class Mage(Tower):
=======
class Mage:
    name = "Mage"

>>>>>>> f33808cc6a0c500694d1e87c332780404a715011
    def __init__(self):
        super(Mage, self).__init__()
        self.health = 15
        self.damage = 150
        self.speed = 4
        self.damage_types = ['splash']

class EarthMage(Mage):
    def __init__(self):
        super(EarthMage, self).__init__()


<<<<<<< HEAD
class Artillery(Tower):
=======
class Artillery:
    name = "Artillery"

>>>>>>> f33808cc6a0c500694d1e87c332780404a715011
    def __init__(self):
        super(Artillery, self).__init__()
        self.health = 50
        self.damage = 200
        self.speed = 2


tower_types = [Arrow, Mage, Artillery]

if __name__ == "__main__":
    test_arrow = Arrow()
    print(test_arrow.health)