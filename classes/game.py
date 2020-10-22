import random
import math
import pprint
from .spellbook import spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94n'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4n'


class make_person:
    def __init__(self, name, hp, mp, atk, df, mtk, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.atkh = int(math.ceil(atk*1.5))
        self.atkl = int(math.floor(atk*0.5))
        self.df = df
        self.mtk = mtk
        self.magic = magic
        self.items = items
        self.action = "Attack", "Magic", "Defense!", "Items"

    def choose_action(self):
        print("Actions:")
        i = 0
        for item in self.action:
            print("    " + str(i+1) + ":", item)
            i += 1

    def choose_magic(self):
        print("Magics:")
        i = 1
        for spell in self.magic:
            print("    " + str(i), ":", spell.name, "// COST MP:", spell.cost, "// DAMAGE ~ ", spell.damage)
            i += 1

    def choose_item(self):
        print("Items:")
        i = 1
        for item in self.items:
            print(str(i), ":", "x"+ str(item["quantity"]), item["which"].name, "//", item["which"].description)
            i += 1

    def choose_target(self, enemies):
        i = 1
        for enemy in enemies:
            print("        "+str(i) + ": " + enemy.name)
            i += 1

    def gen_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self, heal):
        self.hp += heal
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def heal_mp(self, heal):
        self.mp += heal
        if self.mp >= self.max_mp:
            self.mp = self.max_mp
        return self.mp

    def get_hp(self):
        return self.hp
    
    def get_mp(self):
        return self.mp

    def get_atk(self):
        return self.atk
    
    def get_def(self):
        return self.df

    def get_mtk(self):
        return self.mtk

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_atkh(self):
        return self.atkh

    def get_stats(self):
        #HP BAR
        hp_bar = ""
        bar_tick = math.floor(((self.hp / self.max_hp)*100)/4)
        for bars in range(bar_tick):
            hp_bar += "█"
        while len(hp_bar) < 25:
            hp_bar += " "

        #MP BAR
        mp_bar = ""
        mp_tick = math.floor(((self.mp / self.max_mp)*100)/10)
        for bars in range(mp_tick):
            mp_bar += "█"
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        mp_string = str(self.mp) + "/" + str(self.max_mp)
        if len(hp_string) < 7:
            while len(hp_string) < 7:
                hp_string += " "
        if len(mp_string) < 5:
            while len(mp_string) < 5:
                mp_string += " "

        print(self.name+"  :     " + hp_string + "  |" + hp_bar + "|      " + mp_string + "  |" + mp_bar +"|")

    def get_enemy_stats(self):
        hp_bar = ""
        hp_tick = ((self.hp / self.max_hp) * 100) / 2
        while hp_tick > 0:
            hp_bar += "█"
            hp_tick -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        if len(hp_string) < 9:
            while len(hp_string) < 9:
                hp_string += " "
        print(self.name + "  :   " + hp_string + "  |" + hp_bar + "|      ")









