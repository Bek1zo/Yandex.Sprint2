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
            return(current_limit // 70 - current_today_summ // 70)
        elif currency == 'Euro':
            return(current_limit // 80 - current_today_summ // 80)
        elif currency == 'Rouble':
            return(current_limit - current_today_summ)

    def get_today_cash_remained(self, currency):
        if self.today_summ == self.limit:
            print('Денег нет, держись!')
        elif self.today_summ > self.limit:
                print('Денег нет, держись: твой долг', self.courses(currency), currency)
        else:
                print('На сегодня осталось:', self.courses(currency), currency)


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=150, comment="чай"))
cash_calculator.add_record(Record(amount=150, comment="пиво", date="2021-10-15"))
cash_calculator.get_today_stats()
cash_calculator.get_today_cash_remained('USD')
cash_calculator.get_today_cash_remained('Euro')
cash_calculator.get_today_cash_remained('Rouble')
print(cash_calculator.records)