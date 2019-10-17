# This program takes input from the user (two lines each) and inputs it to a text file, which is firstly created.
# The input line1 is City, the input line2 is name and PESEL

# necessary imports:
import os
import time
from collections import deque
# importing necessary classes:
from PESEL import PESEL
from Time import Time
from LongString import LongString
from progressbar import ProgressBar
import time


class main:
    # Maybe lets say hello first:
    print("Hello! This program writes Your input to the file citizenList.txt. \n"
          "In first line, input The city. In the second one, input the name, surname and PESEL of the citizen. \n"
          "Please be sure to type only english letters! \n"
          "The output of this program can be seen in C:/Users/weron/PycharmProjects/citizenList.txt file. Enjoy!")

    # So first, let's create a file:
    if os.path.exists("C:/Users/weron/PycharmProjects/citizenList.txt"):
        os.remove("C:/Users/weron/PycharmProjects/citizenList.txt")
    f = open("C:/Users/weron/PycharmProjects/citizenList.txt", "w+")

    # time checking
    sTime = time.time()
    t = Time().how_much_time_left()
    print("Time that is left:")
    print(t)

    # input assigning
    data = deque()
    i = True

    # now, the loop:
    while i:
        x = input()
        x = str(x)
        data.append(x)
        i = Time().time_and_stuff(t, sTime)

    # Create a new list which will be later added to the file, eg "finalList"
    finalList = []

    # Next step: reorganizing the list:
    # Check if the number of elements is even; if not, then delete the last one.
    n = len(data)
    if n % 2 == 1:
        data.pop()

    # The num. of elements divided by two is a number of iteration in a for loop:
    n2 = n / 2
    listOfPesels = []
    for i in range(int(n2)):
        tempPosition = []
        x = []
        # By using "pop", return every element of the list.
        # Every two lines are one variable
        for i in range(0, 2):
            tempPosition.append(data.popleft())

        for i in range(0, 2):
            x.append(tempPosition[i].split())

        if len(x[0]) < len(x[1]):
            firstPosition = x[0]
            secondPosition = x[1]
        else:
            firstPosition = x[1]
            secondPosition = x[0]

        # check the correctness of the pesel:
        p = PESEL()
        currPesel = (secondPosition[2])
        z = p.if_correct(currPesel)
        # z = p.ifCorrect(currPesel)

        # id correct, ad the position to the finalList
        if z:
            numl = 0
            for i in listOfPesels:
                if i == currPesel:
                    finalList.pop(numl)
                numl += 1
            listOfPesels.append(currPesel)

            fList = LongString().makingTheProperString(firstPosition[0], secondPosition[0], secondPosition[1],
                                                       secondPosition[2])

            finalList.append(fList)
        # END OF FOR LOOP

    # sort the finalList
    finalListSorted = sorted(finalList)

    print("The sorted list:")
    print(finalListSorted)
    n = len(finalListSorted)
    x = int(100 / n)
    y = int(100 / n)
    time.sleep(5)

    print("Adding to the file:")

    pbar = ProgressBar(maxval=n)
    pbar.start()
    w = 1
    # add it to the file
    for i in finalListSorted:
        f.write(i)
        pbar.update(w)
        w += 1
        time.sleep(2)

    pbar.finish()

    exit(0)
