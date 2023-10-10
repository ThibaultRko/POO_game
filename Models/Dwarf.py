

from Models.Character import Character

#region constructor

class Dwarf(Character):
    def __init__(self):
        super().__init__()
        self.__name = input('entrez votre nom : ')
        self.__strength = self.stat_calc()
        self.__endurance = self.stat_calc() +2
        self.__pv = self.modifier_calc(self.__endurance)
        self.__current_pv = self.__pv

#endregion

#region Porp's

    @property
    def current_pv(self):
        return self.__current_pv
    
    @current_pv.setter
    def current_pv(self, value):
        self.__current_pv -= value

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
        msg = self.__name + " le nain \n"
        msg += "force :"+str(self.__strength)+"\n"
        msg += "endurance :"+str(self.__endurance)+"\n"
        msg += "PV :"+str(self.__current_pv)+"/"+str(self.__pv) + "\n"

        print(msg)
        return msg


#endregion
