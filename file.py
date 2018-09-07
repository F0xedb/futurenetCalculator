import money
class file:
    def __init__(self, args):
        self.args = args
        self.filename = args.file
        self.earnings = args.friendearnings

    def ReadEarnings(self, filename):
        arr = []
        if self.filename:
            File = open(filename, 'r')
            arr2 = File.readlines()
            for var in arr2:
                rep = var.replace('\n', '')
                arr.append(rep)
            File.close()

        return arr

    def appendEarnings(self, earnings):
        if self.filename and earnings:
            File = open(self.filename, 'a')
            for var in earnings:
                File.write(var + '\n')
            File.close()

    def appendDailyEarnings(self):
        if self.filename and self.args.dailyearnings:
            File = open(self.filename, 'a')
            for var in self.args.dailyearnings:
                profit = money.money(self.args).CalcWinningsBalance(float(var))
                File.write(str(profit) + '\n')
            File.close()

    def clearFile(self):
        File = open(self.filename, 'w')
        File.write('')
        File.close()

    def merge(self):
        if self.filename and self.args.fuse:
            self.clearFile()
            for File in self.args.fuse:
                array = self.ReadEarnings(File)
                self.appendEarnings(array)


    def TotalEarnings(self):
        self.merge()
        self.appendEarnings(self.earnings)
        self.appendDailyEarnings()
        arr = self.ReadEarnings(self.filename)
        total = 0.0
        for var in arr:
            total += float(var)
        if self.filename and not self.args.convertholiday:
            print("Your total amount earned is " + str(total) + " dollars")
        elif self.filename and self.args.convertholiday:
            # TODO: get profit difference via calculation
            mon = money.money(self.args)
            profit = mon.CalcWinningsBalance(total)
            ultimate = mon.CalcWinningsBalanceNOHd(total)
            print("Your total amount earned is " + str(total*(ultimate/profit)) + " dollars") # number is calculated from output of (profit/progit of holiday)
