import datetime
import datetime as dt

class Record():
    def __init__(self, amount, comment, date=f'{dt.date.today()}'):
        self.amount = amount
        self.comment = comment
        self.date = date


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        records = []
        self.records = records
        self.today_summ = 0
        self.week_summ = 0
        self.currency = ''


class CashCalculator(Calculator):
    def add_record(self, object):
        self.records.append((object.amount, object.comment, object.date))

    def get_today_stats(self):
        for i in range(len(self.records)):
            self.today_summ = self.today_summ + self.records[i][0]
        print(f'Сегодня потрачено: {self.today_summ} рублей')
        return(self.today_summ)

    def courses(self, currency):
        current_limit = self.limit
        current_today_summ = self.today_summ
        if currency == 'USD':
            return(current_limit / 70 - current_today_summ / 70)
        elif currency == 'Euro':
            return(current_limit / 80 - current_today_summ / 80)
        elif currency == 'Rouble':
            return(current_limit - current_today_summ)

    def get_today_cash_remained(self, currency):
        if self.today_summ == self.limit:
            print('Денег нет, держись!')
        elif self.today_summ > self.limit:
                print('Денег нет, держись: твой долг', round(self.courses(currency), 2), currency)
        else:
                print('На сегодня осталось:', round(self.courses(currency), 2), currency)

    def get_week_stats(self):
        today = dt.date.today()
        last_week = []
        #last_week = today - datetime.timedelta(days=7)

        for i in range(7):
            days = today - datetime.timedelta(days=i)
            last_week.append((f'{days}'))


        for i in range(len(self.records)):
            if self.records[i][2] in last_week:
                self.week_summ += self.records[i][0]

        print(self.week_summ)
        print(last_week)


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=150, comment="чай"))
cash_calculator.add_record(Record(amount=180, comment="пиво", date="2021-10-17"))
cash_calculator.add_record(Record(amount=200, comment="столовая", date="2021-10-18"))
cash_calculator.add_record(Record(amount=200, comment="кафе", date="2021-10-15"))
cash_calculator.get_today_stats()
cash_calculator.get_today_cash_remained('USD')
cash_calculator.get_today_cash_remained('Euro')
cash_calculator.get_today_cash_remained('Rouble')
cash_calculator.get_week_stats()



#print(cash_calculator.records)