from Models.Character import Character

#region constructor

class Hero(Character):
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

def retrieve(self):
    pass

#endregion