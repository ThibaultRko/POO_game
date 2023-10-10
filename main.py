
from Models.Character import Character
from Models.Dice import Dice
from Models.Monster import Monstrer
from Models.Human import Human
from Models.Dwarf import Dwarf
from Models.Orc import Orc
from Models.Wolf import Wolf
from Models.Dragon import Dragon


if __name__ == "__main__":
    # D_4 = Dice()
    # D_4.throw_dice(4)
    # D_6 = Dice()
    # D_6.throw_dice(6)

    hero_1 = Human()
    hero_1.show_stat()
    # hero_2 = Dwarf()
    # hero_2.show_stat()
    monster_1 = Orc()
    monster_1.show_stat()
    monster_1.gen_gold()
    # monster_2 = Wolf()
    # monster_2.show_stat()
    # monster_3 = Dragon()
    # monster_3.show_stat()

    hero_1.fight(monster_1)