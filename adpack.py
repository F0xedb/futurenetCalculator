import math
import money

class adpackmoney:
    def __init__(self, bal, advert):
        self.advert = advert
        self.balance = bal


class adpack:
    def __init__(self, worth, course, args):
        self.worth = worth
        self.course = course
        self.args = args
        self.earning = adpackmoney(0.0, 0.0)

    def getDistrbutedEarnings(self, amount):
        dollars = money.money(self.args)
        self.earning = adpackmoney(dollars.CalcBalance(amount), dollars.CalcWinningsAdAcc(amount))
        return self.earning

    def GetDailyEarning(self):
        if self.worth >= self.course:
            self.worth -= self.course
            return self.getDistrbutedEarnings(self.course)
        holder = self.worth
        self.worth = 0
        return  self.getDistrbutedEarnings(holder)

class adpacks:

    def __init__(self, adpacks, bal, advert, worth, course, args, date):
        self.balance = float(bal)
        self.total = float(bal)
        self.advert = float(advert)
        self.date = date
        self.worth = float(worth)
        self.course = float(course)
        self.args = args
        self.adpacks = self.genAdpacks(int(adpacks))
        self.totalsub = 0
        self.totalBought = int(adpacks)

    def genAdpacks(self, amount):
        i = 0
        arr = []
        while i < amount:
            arr.append(adpack(self.worth, self.course, self.args))
            i += 1
        return arr

    def getAdpacksInXDays(self, days):
        self.SimulateXDaysReinvest(days)
        return len(self.adpacks)


    def SimulateXDaysReinvest(self, days):
        i = 0
        self.total = self.balance
        _money = money.money(self.args)


        while i < days:

            # gain the money.money from your adpacks
            j = 0
            while j < len(self.adpacks):
                earnings = self.adpacks[j].GetDailyEarning()
                self.balance += earnings.balance
                self.advert += earnings.advert
                self.total += earnings.balance
                if self.args.payoutprofit:
                    substract = _money.CalcWinningsBalance(earnings.balance)
                    self.balance -= substract
                    self.totalsub += substract
                if self.adpacks[j].worth <= 0:
                    del self.adpacks[j]
                j += 1

            # check to see if you can buy a new adpack
            if self.balance > 50:

                amount = math.floor(self.balance / 50)
                if amount > (1000 - len(self.adpacks)):
                    amount = 1000 - len(self.adpacks)
                k = 0
                while k < amount:
                    self.adpacks.append(adpack(self.worth, self.course, self.args))
                    self.totalBought+=1
                    k += 1
                self.balance -= (50.0 * amount)

            i += 1
        self.printInfo()

    def SimulateXDaysNoReinvest(self, days):
            i = 0
            while i < days:
                # gain the money.money from your adpacks
                j = 0
                while j < len(self.adpacks):
                    earnings = self.adpacks[j].GetDailyEarning()
                    self.balance += earnings.balance
                    self.advert += earnings.advert
                    self.total += earnings.balance
                    if self.adpacks[j].worth == 0:
                        del self.adpacks[j]
                    j += 1
                i += 1
            return self.balance

    def predictAdpacks(self):
        if self.args.days and self.args.adpacks and self.args.balance:
            f_date = self.args.date
            Newdate = self.date.getDateFromString(f_date)
            days = self.date.getDaysFromNow(Newdate)
            if self.args.reinvest:
                amount = self.getAdpacksInXDays(days)
                print("You will have " + str(amount) + " adpacks in " + str(days) + " days")
                self.TotalDailyProfit(int(self.args.adpacks),amount)
            elif self.args.printbalance:
                amount = self.SimulateXDaysNoReinvest(days)
                print("After " + str(days) + " days you will have earned " + str(amount) + " dollar")
                if self.args.total:
                    print("And your total accumulated balance is the same")
                money.money(self.args).profit(True, amount, days)

    def TotalDailyProfit(self,original,now):
        if self.args.totalprofit:
            MoneyVar = money.money(self.args)
            delta = now - original #adpacks that purely generate profit
            originalBal = MoneyVar.CalcWinningsBalance(self.calcAmountFromAdpack(original)) #calculate the profit the original adpacks generate
            deltaBal = self.calcAmountFromAdpack(delta) - MoneyVar.CalcWinningsAdAcc(self.calcAmountFromAdpack(delta))
            total = originalBal + deltaBal
            print("The total profit you gain each day is " + str(total) + " dollars know that this will slowly remove your adpacks until you have " + str(original) + " left.")


    def AdpackProfit(self):
        moneyVar = money.money(self.args)
        if self.args.adpacks:
            adpacks = int(self.args.adpacks)
            winnings = self.calcAmountFromAdpack(adpacks)
            bal = winnings - moneyVar.CalcWinningsAdAcc(winnings)
            add = moneyVar.CalcWinningsAdAcc(winnings)
            print("Your daily profit will be " + str(winnings) + " dollars")
            print("Your daily advertising account profit will be " + str(add) + " dollars")
            money.money(self.args).profit(self.args.profit, bal, 1)

    def CalcBalancefromWinning(self, winning):
        moneyVar = money.money(self.args)
        # profit of one adpack
        winst_one = moneyVar.profitOnePack()
        return int(winning / winst_one) + 1

    def calcAmountFromAdpack(self, packs):
        if self.args.holiday:
            return packs * float(self.args.course) * 0.9
        return  packs * float(self.args.course)

    def calcAmountFromAdpackNOHd(self, packs):
        return  packs * float(self.args.course)

    def targetProfit(self):
        moneyVar = money.money(self.args)
        if self.args.targetprofit:
            #adpacks = float(self.args.targetprofit) / (((((float(self.args.course)-h) / 60.0) * (57.0)) / 120) * (20.0-h2))
            adpacks = self.CalcBalancefromWinning(float(self.args.targetprofit))
            winnings = self.calcAmountFromAdpackNOHd(adpacks)
            bal = winnings - moneyVar.CalcWinningsAdAcc(winnings)
            profit = moneyVar.CalcWinningsBalance(winnings)
            print("You will need a minimum of " + str((adpacks)) + " adpacks this will generate " + str(
                self.calcAmountFromAdpack(adpacks)) + " dollars and " + str(profit) + " dollars of profit daily")

    def amountOver(self, value, earning):
        rest = value / earning
        Irest = int(rest)
        over = rest - float(Irest)
        reverse = 1.0 - over
        return earning * reverse

    def predictTime(self):
        h = 0.0
        if self.args.holiday:
            h = float(self.args.course) * 0.1
        if self.args.extra and self.args.adpacks:
            adpacks = int(self.args.adpacks)
            required = 50.0
            DailyProfit = adpacks * ((float(self.args.course) - h) / 60.0) * 57.0
            amount = math.floor(required / DailyProfit) + 1

            if DailyProfit < 50.0:
                rest = self.amountOver(50.0, DailyProfit)
            else:
                rest = DailyProfit - 50.0
            print("In " + str(amount) + " days you will be able to buy an extra adpack and will have " + str(
                rest) + " spare dollars")

    def printInfo(self):
        if self.args.printbalance:
            print("your balance is " + str(self.balance))
        if self.args.total:
            print("your total accumulated balance is: " + str(self.total))
        if self.args.printadvert:
            print("Your advertisment balance is: " + str(self.advert))
        if self.args.payoutprofit:
            print("Your payout is " + str(self.totalsub))
        if self.args.totalbought:
            print("The total amount of adpacks you have bought is: " + str(self.totalBought))
