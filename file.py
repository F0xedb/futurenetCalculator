class file:
    def __init__(self, args):
        self.args = args
        self.filename = args.file
        self.earnings = args.friendearnings

    def ReadEarnings(self):
        arr = []
        if self.filename:
            File = open(self.filename, 'r')
            arr = File.readlines()
            File.close()

        return arr

    def appendEarnings(self):
        if self.filename and self.earnings:
            File = open(self.filename, 'a')
            for var in self.earnings:
                File.write(var + '\n')
            File.close()

    def TotalEarnings(self):
        self.appendEarnings()
        arr = self.ReadEarnings()
        total = 0.0
        for var in arr:
            total += float(var)
        print("Your total amount earned is " + str(total) + " dollars")

