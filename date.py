import datetime

class date:
    def __init__(self):
        self.date = str(datetime.date.today().year) + "-" + '{:02d}'.format(
            datetime.date.today().month) + "-" + '{:02d}'.format(datetime.date.today().day)
        self.currentDate = datetime.datetime.now()

    def getDaysFromNow(self,date):
        return (date - self.currentDate).days

    def getDateFromString(self,string):
        _date = datetime.datetime.strptime(string, '%Y-%m-%d')
        test = datetime.datetime.date(_date)
        return datetime.datetime.combine(test, datetime.datetime.min.time())
