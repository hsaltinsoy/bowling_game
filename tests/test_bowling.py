from src.bowling import Game
import unittest
from unittest.mock import patch


class TestGameRollMethod(unittest.TestCase):
    @patch('src.bowling.randint', side_effect=[10])
    def test_first_roll_successful(self, mock_randint):
        game = Game()
        result = game.first_roll_func()
        mock_randint.assert_called_with(0, 10)
        self.assertEqual(result, 10)

