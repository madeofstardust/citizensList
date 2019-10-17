from datetime import datetime
import time

# class for checking the class:
class Time:
    # Lets see the time:
    def current_time(self):
        currTime = datetime.now()
        formattedTime = int(currTime.strftime('%S'))
        return formattedTime;

    def how_much_time_left(self):
        i = self.current_time()
        # how much time is left to 30 seconds:
        if i < 30:
            timeLeft = 30 - i
        else:
            timeLeft = 60 - i + 30

        return timeLeft

    def is_it_already(self, timeLeft, startingTime, thisTime):
        if timeLeft < (thisTime - startingTime):
            print("That's enough")
            i = False
        else:
            i = True
        return i

    def time_and_stuff(self, t, sTime):
        nTime = time.time()
        tn = Time().is_it_already(t, sTime, nTime)
        i = tn
        return i
