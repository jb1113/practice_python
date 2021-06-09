# FourCal.py

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):
    # pass
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

#cal = FourCal()
#cal = FourCal(2, 4)
#cal.setData(2, 4)
#print(cal.add())
#print(cal.sub())
#print(cal.mul())
#print(cal.div())

#cal = MoreFourCal(4, 2)
#print(cal.pow())
cal = SafeFourCal(4, 0)
print(cal.div())
