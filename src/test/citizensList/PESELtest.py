import unittest

class PESELTest(unittest.TestCase):

    def assign_PESEL(self, p):
        peselDigits = []
        for i in p:
            peselDigits.append(i)
        return peselDigits

    def if_correct(self, p):
        peselDigits = self.assign_PESEL(p)

        sumOfNumbers = 0
        sumOfNumbers += (9 * int(peselDigits[0]) + 7 * int(peselDigits[1]) + 3 * int(peselDigits[2]) + 1 * int(
            peselDigits[3]) + 9 * int(peselDigits[4]) + 7 * int(peselDigits[5]) + 3 * int(peselDigits[6]) + 1 * int(
            peselDigits[7]) + 9 * int(peselDigits[8]) + 7 * int(peselDigits[9]))
        modulo = sumOfNumbers % 10
        if modulo == int(peselDigits[10]):
            return True
        else:
            return False

    def test_if_checker_works(self):
        correctPesel = "99102102202"
        self.assertTrue(self.if_correct(correctPesel))


if __name__ == '__main__':
    unittest.main()
