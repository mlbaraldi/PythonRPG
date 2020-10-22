##tentar criar funcoes para facilitar

import math
import random
from classes.game import make_person, bcolors
from classes.spellbook import spell
from classes.inventory import Item


# functions
def is_dead():
    if enemy.hp <= 0:
        enemy.hp = 0
        print(enemy.name + "has fallen! \n")
        enemies.remove(enemy)


def is_crit(dmg, maxdmg):
    if dmg > maxdmg - 1:
        print("Thats a critical!")
        return math.ceil(dmg * 1.2)
    else:
        return dmg

def print_score():
    print("\n")
    print("PLAYER                            HP                               MP")
    for player in players:
        player.get_stats()
    print("\n")
    print("ENEMY                                            HP")
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n")


# creating magics
# black magic
fire = spell(1, "Fire", 1, "B", 3)
thunder = spell(2, "Thunder", 2, "B", 5)
blizzard = spell(3, "Blizzard", 3, "B", 7)
meteor = spell(4, "Meteor", 4, "B", 10)
quake = spell(5, "Quake", 7, "B", 15)

# White magic
cure = spell(1, "Cure", 4, "W", 8)
cura = spell(2, "Cura", 8, "W", 14)

# Items
potion = Item("Potion", "potion", "It heals 15 HP", 15)
hipotion = Item("Hi-Potion", "potion", "It heals 50 HP", 50)
superpotion = Item("Super Potion", "potion", "It heals 100HP", 100)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one member of your party", 9999)
hielixir = Item("Hi-Elixir", "elixir", "Fully restores HP/MP of the entire party", 9999)
ether = Item("Ether", "ether", "It restores 50MP", 50)
grenade = Item("Grenade", "attack", "It deals 500 damage! Kabooom", 500)
garrafadeagua = Item("Garrafadeagua", "potion", "It heals 18 HP", 18)

# Initiate spellbook and inventory
spellbook = [fire, thunder, blizzard, meteor, quake, cure, cura]
inventory = [{"which": superpotion, "quantity": 5},
             {"which": grenade, "quantity": 5},
             {"which": elixir, "quantity": 1},
             {"which": ether, "quantity": 5}]

# Instantiate NPCs
enemy1 = make_person(name="Draco  ", hp=1200, mp=15, atk=80, df=8, mtk=5, magic=[fire], items=inventory)
enemy2 = make_person(name="Boleto ", hp=150, mp=10, atk=200, df=0, mtk=0, magic=[], items=[])
enemy3 = make_person(name="Imp    ", hp=20, mp=50, atk=10, df=5, mtk=30, magic=[fire, blizzard, thunder], items=[])
player1 = make_person(name="Mark  ", hp=500, mp=20, atk=100, df=15, mtk=10, magic=spellbook, items=inventory)
player2 = make_person(name="Isa   ", hp=400, mp=40, atk=10, df=10, mtk=40, magic=spellbook, items=inventory)
player3 = make_person(name="Gretta", hp=200, mp=15, atk=50, df=7, mtk=5, magic=spellbook, items=inventory)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

# START BATTLE
for enemy in enemies:
    print(enemy.name)
print(bcolors.BOLD + "WANTS TO FIGHT!" + bcolors.ENDC)

while running:
    defense_up = False
    ##MENU 1
    print_score()
    for player in players:
        print(player.name)
        print("Its your turn!")
        player.choose_action()
        choice = int(input("    Choose action: "))

        ##PHYSICAL ATTACK
        if choice == 1:
            dmg_dealt = player.gen_damage()
            player.choose_target(enemies)
            enemy = enemies[int(input("        Choose target:")) - 1]
            final_dmg = is_crit(dmg_dealt, player.get_atkh())
            print("You hit", enemy.name, "for", final_dmg, "damage!")
            enemy.take_damage(final_dmg - enemy.df)
            is_dead()

        ## MAGIC ATTACK
        elif choice == 2:
            player.choose_magic()
            magic_number = int(input("Choose your magic: ")) - 1

            if magic_number >= len(player.magic) or magic_number <= -1:
                print("its not a valid choice")
                continue

            spell = player.magic[magic_number]
            magic_cost = spell.get_spell_cost()
            current_mp = player.get_mp()
            print("You used", str(spell.name) + "!")
            print("It costs", magic_cost, "MP")
            player.reduce_mp(magic_cost)
            magic_damage_dealt = spell.gen_spell_damage() + player.mtk

            if magic_cost > current_mp:
                print(bcolors.FAIL + "\n You don`t have enough MP, choose again. \n" + bcolors.ENDC)
                continue

            if spell.type == "W":
                player.choose_target(players)
                friend = players[int(input("        Choose target:")) - 1]
                friend.heal(magic_damage_dealt)
                print("\n" + spell.name, "heals", friend.name, "for", str(magic_damage_dealt) + ".", friend.name, "now have " + str(friend.get_hp()))
            elif spell.type == "B":
                player.choose_target(enemies)
                enemy = enemies[int(input("        Choose target:")) - 1]
                print(bcolors.OKBLUE + "You hit", enemy.name + str(magic_damage_dealt) + " as magic damage!" + bcolors.ENDC)
                enemy.take_damage(magic_damage_dealt)
                is_dead()

        # DEFENSE
        elif choice == 3:
            defense_up = True

        # ITEMS
        elif choice == 4:
            player.choose_item()
            item_number = int(input("Choose Item: ")) - 1
            item = player.items[item_number]["which"]

            if item_number >= len(player.items) or item_number <= -1:
                print("its not a valid choice")
                continue

            if player.items[item_number]["quantity"] == 0:
                print("None left... choose again")
                continue

            print("You used", str(item.name) + "!")
            player.items[item_number]["quantity"] -= 1

            if item.type == "potion":
                player.choose_target(players)
                friend = players[int(input("        Choose target:")) - 1]
                friend.heal(item.prop)
                print(+ item.name, "heals " + friend.name +" for", str(item.prop))
            elif item.type == "attack":
                player.choose_target(enemies)
                enemy = enemies[int(input("        Choose target:")) - 1]
                enemy.take_damage(item.prop)
                print(item.name, "deals", str(item.prop), "damage to " + enemy.name)
            elif item.type == "ether":
                player.heal_mp(item.prop)
                print(item.name, "recovered your MP for", str(item.prop))
            elif item.type == "elixir":
                if item.name == "Hi-Elixir":
                    for person in players:
                        person.hp = person.max_hp
                        person.mp = person.max_mp
                    else:
                        player.hp = player.max_hp
                        player.mp = player.max_mp
                print(item.name, "fully restores HP/MP")
        else:
            print("Its not an option!")
            continue

        # ENEMY COMBAT
    if len(enemies) <= 0:
        while i < 20:
            print("You won!")
            i += 1
        running = False
        break
    else:
        for enemy in enemies:
            target = random.randrange(0, len(players))
            player = players[target]
            print("=======================================================")
            print("Now its the", enemy.name, "turn! It attacks " + player.name + "!")
            if defense_up:
                print("you are defending!")
                newdef = math.ceil(player.get_def() * 3)
                enemy_damage = player.gen_damage() - newdef
            else:
                enemy_damage = player.gen_damage() - player.get_def()

            defense_up = False
            if enemy_damage < 0:
                enemy_damage = 0
            final_dmg = is_crit(enemy_damage, player.get_atkh())
            print("It hits " + player.name, final_dmg, "damage!")
            player.take_damage(final_dmg)

            if player.get_hp() <= 0:
                print(bcolors.FAIL + "You lose!" + bcolors.ENDC)
                running = False
