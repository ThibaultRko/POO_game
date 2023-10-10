from Models.Character import Character
from Models.Dice import Dice

#region constructor

class Monstrer(Character):
    def __init__(self):
        super().__init__()
        self.__gold = 0
        self.__leather = 0


#endregion

#region prop's

    @property
    def gold(self):
        return self.__gold
    @gold.setter
    def gold(self, value):
        self.__gold = value

    @property
    def leather(self):
        return self.__leather
    @leather.setter
    def leather(self, value):
        self.__leather = value

#endregion

#region method

    def gen_gold(self):
        D_6 = Dice()
        gold = D_6.throw_dice(6)
        print(f"or :{gold}")
        return gold
    
    def gen_leather(self):
        D_4 = Dice()
        leather = D_4.throw_dice(4)
        print(leather)
        return leather

#endregion