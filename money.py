class money:
    def __init__(self, argument):
        self.args = argument

    def profit(self, bool, _money, days):

        if bool and _money != 0 and _money:
            dailyMoney = float(_money) / float(days)
            profit = self.CalcWinnings(dailyMoney)
            adprofit = self.CalcWinningsAdAcc(dailyMoney)
            balprofit = self.CalcWinningsBalance(dailyMoney)
            mn = self.CalcWinnings(float(_money))
            print("Today your profit was " + str(profit) + " dollar")
            print("Today your advertising account profit was " + str(adprofit) + " dollar")
            print("Today your balance profit was " + str(balprofit) + " dollar")
            if days != 1:
                print("Your total profit was " + str(mn) + " dollar")

    def CalcWinnings(self, amount):
        sustaining = 0.0
        if self.args.holiday:
            sustaining = (((amount * 0.1) / 6.0) * 5.0)
            amount = amount * 0.9
        return (amount / 6.0) - sustaining

    def CalcBalance(self,amount):
        adacc = self.CalcWinningsAdAcc(amount)
        if self.args.holiday:
            amount = amount * 0.9
        return amount - adacc

    def CalcWinningsAdAcc(self, amount):
        if self.args.holiday:
            amount = amount * 0.9
        return  (amount / 60.0) * 3.0

    def CalcWinningsBalance(self, amount):
        sustaining = 0.0
        if self.args.holiday:
            sustaining = (((amount * 0.1) / 6.0) * 5.0)
            amount = amount * 0.9
            #return profit equally but we have to substract sustaining profit
        return ((amount / 60.0) * 7.0) - sustaining

    def CalcWinningsBalanceNOHd(self, amount):
        return ((amount / 60.0) * 7.0)

    def CalcWinningsAdAccNOHd(self, amount):
        return  (amount / 60.0) * 3.0




    def EarningOnePack(self):
        return self.CalcWinnings(float(self.args.course))

    def profitOnePack(self):
        return self.CalcWinningsBalance(float(self.args.course))


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