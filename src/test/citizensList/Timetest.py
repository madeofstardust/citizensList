import unittest
import hypothesis
import hypothesis.strategies as hs
from hypothesis import given
from hypothesis.strategies import text

class Timetest(unittest.TestCase):

    def how_much_time_left(self, p):
        i = p
        # how much time is left to 30 seconds:
        if i <= 30:
            timeLeft = 30 - i
        else:
            timeLeft = 60 - i + 30
        return timeLeft

    def test_if_howmuchtimeleft_works(self):
        l = 20
        # for a number less or equal to thirty:
        self.assertEqual(10, self.how_much_time_left(l))
        # for a number more than 30:
        l2 = 45
        self.assertEqual(45, self.how_much_time_left(l2))


if __name__ == '__main__':
    unittest.main()
