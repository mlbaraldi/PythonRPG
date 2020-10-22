import math
import random


class spell:
    def __init__(self, index, name, cost, dtype, damage):
        self.name = name
        self.type = dtype
        self.cost = cost
        self.damage = damage
    
    def get_spell_name(self):
        return self.name

    def get_spell_cost(self):
        return self.cost

    def gen_spell_damage(self):
        magicl = int(math.floor(self.damage*0.5))
        magich = int(math.ceil(self.damage*1.5))
        return random.randrange(magicl, magich)