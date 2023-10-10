import random

#region constructor

class Dice:
    def __init__(self) -> None:
        self.__min = 1
        self.__max = 0

#endregion

#region prop's

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max

#endregion

#region method

    def throw_dice(self, value):
        result = random.randint(self.__min, value)
        # print(result)
        return result

#endregion