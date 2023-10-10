
from Models.Dice import Dice
from Models.Character import Character
from Models.hero import Hero

#region constructor

class Human(Hero):
    def __init__(self):
        super().__init__()
        self.__name = input("entrez votre nom : ")
        self.__strength = self.stat_calc() +1
        self.__endurance = self.stat_calc() +1
        self.__pv = self.modifier_calc(self.__endurance)
        self.__current_pv = self.__pv
        self.__gold = 0
        self.__leather = 0

#endregion

#region Porp's

    @property
    def current_pv(self):
        return self.__current_pv
    
    @current_pv.setter
    def current_pv(self, value):
        self.__current_pv -= value

    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, value):
        self.__damage = value

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
    
    def stat_calc(self):
        return super().stat_calc()
    
    def modifier_calc(self, value):
        pv_bonus = 0
        if value < 5:
            pv_bonus -=1
        elif value < 10:
            pv_bonus += 0
        elif value < 15:
            pv_bonus +=1
        else:
            pv_bonus +=2
        value +=pv_bonus
        return value

    def show_stat(self):
        msg = self.__name + " l'humain \n"
        msg += "force :"+str(self.__strength)+"\n"
        msg += "endurance :"+str(self.__endurance)+"\n"
        msg += "PV :"+str(self.__current_pv)+"/"+str(self.__pv) + "\n"
        msg += "Or : "+str(self.__gold) + "\n"
        msg += "Cuir : "+str(self.__leather) + "\n"
        

        print(msg)
        return msg

    def give_damage(self):
        D_4 = Dice()
        self.__damage = D_4.throw_dice(4)+1
        self.modifier_calc(self.__damage)
        print(self.__name + " inflige " + str(self.__damage)+" dégats")
        return self.__damage
    
    def take_damage(self, value):
        self.__current_pv -= value
        return self.__current_pv
    
    def retrieve(self, AI):
        return super().retrieve(AI)


#endregion
