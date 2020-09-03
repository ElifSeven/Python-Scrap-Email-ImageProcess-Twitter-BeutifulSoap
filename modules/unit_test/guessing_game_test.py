import unittest
from unit_test.guessing_game_with_test import run_guess


class TestGuessingGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = run_guess(answer, guess)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
