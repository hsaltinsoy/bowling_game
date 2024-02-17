from src.bowling import Game
import unittest
from unittest.mock import patch


class TestGameRollMethod(unittest.TestCase):
    @patch('src.bowling.randint', side_effect=[10])
    def test_strike_roll_successful(self, mock_randint):
        game = Game()
        result = game.first_roll_func()
        self.assertEqual(result, 10)
        mock_randint.assert_called_with(0, 10)

    @patch('src.bowling.randint', side_effect=[5, 4])
    def test_normal_roll_successful(self, mock_randint):
        game = Game()
        result = game.first_roll_func()
        self.assertEqual(result, 9)
        mock_randint.assert_called_with(0, 10 - 5)

    @patch('src.bowling.randint', side_effect=[5, 5])
    def test_spare_roll_successful(self, mock_randint):
        game = Game()
        result = game.first_roll_func()
        self.assertEqual(result, 10)
        mock_randint.assert_called_with(0, 10 - 5)
