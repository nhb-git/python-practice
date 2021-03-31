class TestData:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_month(self):
        return self.month

    @classmethod
    def format_time(cls, kk):
        day, month, year = map(int, kk.split('-'))
        date1 = cls(day, month, year)
        return date1


data2 = TestData.format_time('11-09-2012')
print(data2.get_month())
