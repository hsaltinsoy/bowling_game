from numpy.random import randint


class Game:
    def __init__(self):
        self.first_roll = 0
        self.second_roll = 0
        self.frame = 0
        self.scores = []

    def play_game(self):
        while self.frame <= 10:
            self.roll()

    def roll(self) -> int:
        # Start a new frame, reset rolls
        self.first_roll = 0
        self.second_roll = 0

        # First roll
        self.first_roll = randint(0, 11)

        # Handle strike
        if self.first_roll == 10:
            self.handle_strike()
            return 10

        # Second roll
        self._second_roll()

        # Handle spare
        if self.first_roll + self.second_roll == 10:
            self.handle_spare()
            return 10

        # Regular frame
        self.handle_regular_frame()
        return self.first_roll + self.second_roll

    def _second_roll(self) -> int:
        self.second_roll = randint(0, 10 - self.first_roll)
        return self.first_roll + self.second_roll

    def handle_strike(self):
        self.frame += 1
        self.scores.append(10)

        # Bonus for a strike is the next two rolls
        bonus_rolls = self.next_two_rolls()
        self.scores.extend(bonus_rolls)

    def handle_spare(self):
        self.scores.append(10)

        # Bonus for a spare is the next roll
        bonus_roll = self.next_roll()
        self.scores.append(bonus_roll)

    def handle_regular_frame(self):
        self.frame += 1
        self.scores.append(self.first_roll + self.second_roll)

    @staticmethod
    def next_roll() -> int:
        return randint(0, 10)

    @staticmethod
    def next_two_rolls() -> list[int]:
        return [randint(0, 10), randint(0, 10)]

    def total_score(self) -> int:
        return sum(self.scores)


if __name__ == "__main__":
    bowling_game = Game()
    bowling_game.play_game()

    total_score = bowling_game.total_score()
    print(f"Total Score: {total_score}")
