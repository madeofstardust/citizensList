# Class taking care of PESEL

class PESEL:
    def assign_PESEL(self, p):
        peselDigits = []
        for i in p:
            peselDigits.append(i)
        if len(peselDigits) != 11:
            peselDigits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        return peselDigits

    # Function that checks if the PESEL ir alright:
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
