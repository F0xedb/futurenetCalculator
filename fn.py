import argparser
import money
import adpack
import date
import file



def init(argument, date):
    if argument.args.usage:
        argument.usage()
    args = argument.args

    _money = float(args.money)
    days = int(args.days)

    # calculate the given profit with the money.money you earned
    money.money(args).profit(args.profit, _money, days)

    # count command line parameter
    countmoney = money.counter(args.count).calculate()

    if args.count:
        money.money(args).profit(args.countprofit, countmoney, len(args.count))

    # predict adpack amount in x days
    packs = adpack.adpacks(args.adpacks, args.balance, 0.0, 60.0, float(args.course), args, date)
    packs.predictAdpacks()

    packs.predictTime()

    if args.adpackprofit:
        packs.AdpackProfit()

    packs.targetProfit()
    file.file(args).TotalEarnings()


if __name__ == '__main__':
    g_date = date.date()
    argument = argparser.argparser(g_date.date)
    init(argument, g_date)