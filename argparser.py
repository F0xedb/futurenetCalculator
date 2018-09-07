import argparse
class argparser:
    def __init__(self, date):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('-u', '--usage', help='Display the usage menu', action='store_true', default=False)
        self.parser.add_argument('-m', '--money', help='amount of money in dollar', default=0)
        self.parser.add_argument('-d', '--days', help='the amount of days you have accumulated the money', default=1)
        self.parser.add_argument('-p', '--profit', help='the amount of profit you have accumulated', action='store_true',
                            default=True)
        self.parser.add_argument('-c', '--count', help='count floats', nargs='*')
        self.parser.add_argument('-cp', '--countprofit', help='the amount of profit you have accumulated',
                            action='store_true', default=False)
        self.parser.add_argument('-D', '--date', help='Enddate in the format YYYY-MM-DD including leading zeros',
                            default=date)
        self.parser.add_argument('-r', '--reinvest', help='reinvest adpack', action='store_true', default=False)
        self.parser.add_argument('-pb', '--printbalance', help='print balance', action='store_true', default=False)
        self.parser.add_argument('-pa', '--printadvert', help='print advertising balance', action='store_true',
                            default=False)
        self.parser.add_argument('-a', '--adpacks', help='Enter amount of adpacks', default=1)
        self.parser.add_argument('-ap', '--adpackprofit', help='print balance', action='store_true', default=False)
        self.parser.add_argument('-e', '--extra', help='print the amount of days,hours, minutes before getting a new adpack',
                            action='store_true', default=False)
        self.parser.add_argument('-b', '--balance', help='Enter your current balance', default=0.0)
        self.parser.add_argument('-t', '--total', help='Total accumulated balance', action='store_true', default=False)
        self.parser.add_argument('-hd', '--holiday', help='Calculate everything acorrding to the holiday settings',
                            action='store_true', default=False)
        self.parser.add_argument('-chd', '--convertholiday', help='convert holiday profit in a file to normal profit', action='store_true', default=False)
        self.parser.add_argument('-tp', '--targetprofit',
                            help='Calculate the amount of adpacks necesery to achieve your profit')
        self.parser.add_argument('-f', '--file', help='the file where to save your profit earned from friends')
        self.parser.add_argument('-fe', '--friendearnings', help='Earnings from your friends', nargs='*')
        self.parser.add_argument('-de', '--dailyearnings', help='Earnings from your friends', nargs='*')
        self.parser.add_argument('--fuse', help='Earnings from your friends', nargs='*')
        self.parser.add_argument('--totalprofit', help='The total profit you gain when reinvesting',
                                 action='store_true', default=False)
        self.parser.add_argument('-pp', '--payoutprofit', help='When earning payout your profit',
                                 action='store_true', default=False)
        self.parser.add_argument('-tb', '--totalbought', help='Count the total amount of adpacks bought',
                                 action='store_true', default=False)
        self.parser.add_argument('--course', help='the amount one adpack generates in one day', default=0.45)

        self.args = self.parser.parse_args()

    def usage(self):
            print("")
            print("Usage")
            print("    Calculate the amount of profit in one day:")
            print("        <name> -m [amount]")
            print("    Calculate the amount of profit in one day when a holiday is active:")
            print("        <name> -m [amount] -hd")
            print("    Calculate the amount of profit spread over n days:")
            print("        <name> -m [amount] -d [number of days]")
            print("    Calculate the amount of money x adpacks generate in one day:")
            print("        <name> -a [adpacks] -ap")
            print("    Calculate the amount of days it takes to gain 1 adpack:")
            print("        <name> -a [adpacks] -e")
            print("    Calculate the amount of adpacks needed to achieve x amount of profit:")
            print("        <name> -tp [profit in dollars]")
            print("    Calculate total revenue from x days:")
            print("        <name> -c [Number1] [Number2] [Number3] ... [Number N]")
            print("    Calculate total revenue from x days and print revenue information:")
            print("        <name> -c [Number1] [Number2] [Number3] ... [Number N] -cp")
            print("    Calculate amount of adpack in x days")
            print("        <name> -D [YYYY-MM-DD] -a [Adpacks] -b [Balance] -r -pb")
            print("    Calculate amount of adpacks in x days and print the balance also print your advertising balance")
            print("        <name> -D [YYYY-MM-DD] -a [Adpacks] -b [Balance] -r -pb -pa")
            print("    Calculate amount of balance in x days and print the balance")
            print("        <name> -D [YYYY-MM-DD] -a [Adpacks] -b [Balance] -pb")
            print("    Calculate amount of balance in x days and print the total accumulated balance (if you kept the balance from the beginning) ")
            print("        <name> -D [YYYY-MM-DD] -a [Adpacks] -b [Balance] -r -t")
            print("    Calculate amount of profit in x days and print the total balance profit each day")
            print("        <name> -D [YYYY-MM-DD] -a [Adpacks] -b [Balance] -r --totalprofit")
            print("    Calculate profit your friends have given you listed in a file:")
            print("        <name> -f file")
            print("    Calculate profit your friends have given you listed in a file and append new information:")
            print("        <name> -f file -fe [Winst1] [Winst2] [Winst3] ... [WinstN]")
            print("    Add multiple files together:")
            print("        <name> -f [output] -fuse [file1] [file2] [file3] ... [fileN]")
