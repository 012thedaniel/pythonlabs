import calendar
from datetime import date, timedelta
import re


class Calendar:
    def __init__(self, value):
        try:
            date.fromisoformat(value)
        except TypeError:
            print(f'date of event value must be a string')
            exit(0)
        except ValueError:
            print(f'the value u passed can\'t be the date of event')
            exit(0)
        date_attributes = value.split('-')
        self.__year = int(date_attributes[0])
        self.__month = int(date_attributes[1])
        self.__day = int(date_attributes[2])

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u passed as a year must be an integer')
        if value < 0:
            raise Exception(f'the value, u passed as a year must be bigger than 0')
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u passed as a month must be an integer')
        try:
            date.fromisoformat(f'{self.__year}-{value}-{self.day}')
            self.__month = value
        except ValueError:
            print(f'the date with the new month value isn\'t possible')

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u passed as a month must be an integer')
        try:
            date.fromisoformat(f'{self.__year}-{self.month}-{value}')
            self.__day = value
        except ValueError:
            print(f'the date with the new day value isn\'t possible')

    def __iadd__(self, other):
        try:
            if not re.fullmatch(r"\d+[dmy]", other):
                raise ValueError
            if other[-1] == 'd':
                new_date = (str(date.fromisoformat(f'{self.year}-{self.month}-{self.day}')
                                + timedelta(days=int(other[:-1])))).split('-')
                self.__year = new_date[0]
                self.__month = new_date[1]
                self.__day = new_date[2]
                return self
            elif other[-1] == 'm':
                self.__month += int(other[:-1])
                while self.__month > 12:
                    self.__year += 1
                    self.__month -= 12
                try:
                    date.fromisoformat(f'{self.year}-{self.month}-{self.day}')
                except ValueError:
                    self.__day -= calendar.monthrange(self.year, self.month)[1]
                    self.__month += 1
                return self
            else:
                self.__year += int(other[:-1])
                return self
        except TypeError:
            print(f'exception: wrong type of the value, u\'re trying to add to the date')
        except ValueError:
            print(f'exception: wrong format of the string, when adding days/months/years to the date')

    def __isub__(self, other):
        try:
            if not re.fullmatch(r"\d+[dmy]", other):
                raise ValueError
            if other[-1] == 'd':
                new_date = (str(date.fromisoformat(f'{self.year}-{self.month}-{self.day}')
                                - timedelta(days=int(other[:-1])))).split('-')
                self.__year = new_date[0]
                self.__month = new_date[1]
                self.__day = new_date[2]
                return self
            elif other[-1] == 'm':
                self.__month -= int(other[:-1])
                while self.__month < 1:
                    self.__year -= 1
                    self.__month += 12
                try:
                    date.fromisoformat(f'{self.year}-{self.month}-{self.day}')
                except ValueError:
                    self.__day -= calendar.monthrange(self.year, self.month)[1]
                    self.__month += 1
                return self
            else:
                self.__year -= int(other[:-1])
                return self
        except TypeError:
            print(f'exception: wrong type of the value, u\'re trying to subtract from the date')
        except ValueError:
            print(f'exception: wrong format of the string, when subtracting days/months/years to the date')

    def __eq__(self, other):
        if isinstance(other, Calendar):
            return self.year == other.year and self.month == other.month and self.day == other.day
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __ne__(self, other):
        if isinstance(other, Calendar):
            return self.year != other.year and self.month != other.month and self.day != other.day
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __gt__(self, other):
        if isinstance(other, Calendar):
            return date.fromisoformat(f'{"{:03d}".format(self.year)}-{"{:02d}".format(self.month)}-'
                                      f'{"{:02d}".format(self.day)}') > \
                   date.fromisoformat(f'{"{:03d}".format(other.year)}-{"{:02d}".format(other.month)}-'
                                      f'{"{:02d}".format(other.day)}')
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __lt__(self, other):
        if isinstance(other, Calendar):
            return date.fromisoformat(f'{"{:03d}".format(self.year)}-{"{:02d}".format(self.month)}-'
                                      f'{"{:02d}".format(self.day)}') < \
                   date.fromisoformat(f'{"{:03d}".format(other.year)}-{"{:02d}".format(other.month)}-'
                                      f'{"{:02d}".format(other.day)}')
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __ge__(self, other):
        if isinstance(other, Calendar):
            return date.fromisoformat(f'{"{:03d}".format(self.year)}-{"{:02d}".format(self.month)}-'
                                      f'{"{:02d}".format(self.day)}') >= \
                   date.fromisoformat(f'{"{:03d}".format(other.year)}-{"{:02d}".format(other.month)}-'
                                      f'{"{:02d}".format(other.day)}')
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __le__(self, other):
        if isinstance(other, Calendar):
            return date.fromisoformat(f'{"{:03d}".format(self.year)}-{"{:02d}".format(self.month)}-'
                                      f'{"{:02d}".format(self.day)}') <= \
                   date.fromisoformat(f'{"{:03d}".format(other.year)}-{"{:02d}".format(other.month)}-'
                                      f'{"{:02d}".format(other.day)}')
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __str__(self):
        return f'the date is: {"{:03d}".format(self.year)}-{"{:02d}".format(self.month)}-{"{:02d}".format(self.day)}'


date1 = Calendar('2015-10-15')
date2 = Calendar('2022-10-31')

print(date2)
date2 -= "1y"
date2 += '13m'
print(date2)

print(date1 == date2)
print(date1 != date2)
print(date1 > date2)
print(date1 < date2)
print(date1 >= date2)
print(date1 <= date2)
