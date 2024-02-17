from numpy.random import randint


class Game:
    first_roll: int
    second_roll: int
    frame = 0

    def first_roll_func(self) -> int:
        self.first_roll = randint(0, 10)
        if self.first_roll == 10:
            self.frame += 1
            return self.first_roll
        else:
            return self.second_roll_func()

    def second_roll_func(self) -> int:
        self.second_roll = randint(0, 10 - self.first_roll)
        if self.first_roll + self.second_roll == 10:
            self.frame += 1
            return 10
        else:
            self.frame += 1
            return self.first_roll + self.second_roll

    def score(self) -> int:
        if self.first_roll != 10 and self.first_roll + self.second_roll != 10:
            return self.first_roll + self.second_roll

