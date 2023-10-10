from Models.Dice import Dice

class Character:

    #region constructor
    def __init__(self):
        self.__strength = 0
        self.__endurance = 0
        self.__pv = self.__endurance
    #endregion

    #region prop's

    @property
    def strength(self):
        return self.__strength
    
    @property
    def endurance(self):
        return self.__endurance
    
    @property
    def pv(self):
        return self.__pv
    

    #endregion

    #region method

    # def test(self):
    #     print(self.__strength)
    
    def stat_calc(self):
        i = 0
        D_6 = Dice()
        result = []
        while i < 4:
            result.append(D_6.throw_dice(6))
            i+=1
        result.remove(min(result))
        result = sum(result)
        # print(result)
        return result

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
        # print(value)
        value +=pv_bonus
        return value
    
    def show_stat(self):
        msg = "force :"+str(self.__strength)+"\n"
        msg += "endurance :"+str(self.__endurance)+"\n"
        msg += "self.__pv :"+str(self.__pv)+"\n"

        print(msg)
        return msg
    
    def give_damage(self):
        pass

    def take_damage(self, value):
        pass

    def fight(self, AI):
        print(f"le combat commence")
        while self.current_pv > 0 and AI.current_pv > 0:
                AI.take_damage(self.give_damage())
                AI.show_stat()
                if AI.current_pv <= 0:
                    print("MONSTER IS DEAD")
                    self.retrieve(AI)
                    break
                self.take_damage(AI.give_damage())
                self.show_stat()
                if self.current_pv <= 0:
                    print("GAME OVER")

    def retrieve(self, AI):
        self.__gold += AI
        self.__leather += AI
        return self.__gold, self.__leather


    #endregion