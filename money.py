class money:
    def __init__(self, argument):
        self.args = argument

    def profit(self, bool, _money, days):

        if bool and _money != 0 and _money:
            dailyMoney = _money / float(days)
            profit = self.CalcWinnings(dailyMoney)
            mn = self.CalcWinnings(_money)
            print("Today your profit was " + str(profit) + " dollar")
            if days != 1:
                print("Your total profit was " + str(mn) + " dollar")

    def CalcWinnings(self, amount):
        if self.args.holiday:
            return (amount / 60.0) * 8.0
        return  amount / 6.0

    def CalcWinningsAdAcc(self, amount):
        if self.args.holiday:
            return (amount / 60.0) * 2.7
        return  amount / 20.0

    def CalcWinningsBalance(self, amount):
        if self.args.holiday:
            return (amount / 60.0) * (57.0 - 5.7)
        return  (amount / 60.0) * 57.0

class counter:
    def __init__(self, arr):
        self.arr = arr

    def calculate(self):
        if not self.arr:
            return 0.0

        i = 0
        total = 0.0
        while i < len(self.arr):
            total += float(self.arr[i])
            i += 1
        print("Total amount of money is " + str(total))
        print("Amount of numbers is " + str(i))
        return total