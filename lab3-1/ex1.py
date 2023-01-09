import math


class Rational:
    def __init__(self, numerator=1, denominator=2):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u pass a numerator must be an integer number')
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise Exception(f'the value, u pass a denominator must be an integer number')
        if not value:
            raise Exception(f'denominator can\'t be equal to zero')
        self.__denominator = value

    @staticmethod
    def minimise_rational_number(numerator, denominator):
        if numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        greatest_common_divisor = math.gcd(numerator, denominator)
        if not numerator:
            denominator = 1
        elif greatest_common_divisor != 1:
            numerator = int(numerator/greatest_common_divisor)
            denominator = int(denominator/greatest_common_divisor)
        return numerator, denominator

    def rational(self):
        return f'rational: ' + "/".join(map(str, Rational.minimise_rational_number(self.numerator, self.denominator)))

    def floating(self):
        return f'floating-point number: {self.numerator / self.denominator}'

    def __add__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator + other.numerator*self.denominator,
                                                    self.denominator*other.denominator)
            return Rational(tmp[0], tmp[1])
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __iadd__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator + other.numerator*self.denominator,
                                                    self.denominator*other.denominator)
            self.numerator = tmp[0]
            self.denominator = tmp[1]
            return self
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __sub__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator - other.numerator*self.denominator,
                                                    self.denominator*other.denominator)
            return Rational(tmp[0], tmp[1])
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __isub__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator - other.numerator*self.denominator,
                                                    self.denominator*other.denominator)
            self.numerator = tmp[0]
            self.denominator = tmp[1]
            return self
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __mul__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.numerator, self.denominator*other.denominator)
            return Rational(tmp[0], tmp[1])
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __imul__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.numerator, self.denominator*other.denominator)
            self.numerator = tmp[0]
            self.denominator = tmp[1]
            return self
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __truediv__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator, self.denominator*other.numerator)
            return Rational(tmp[0], tmp[1])
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            tmp = Rational.minimise_rational_number(self.numerator*other.denominator, self.denominator*other.numerator)
            self.numerator = tmp[0]
            self.denominator = tmp[1]
            return self
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator/self.denominator == other.numerator/other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator != other.numerator / other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator > other.numerator / other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator < other.numerator / other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator >= other.numerator / other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator <= other.numerator / other.denominator
        else:
            raise TypeError(f'unsupported operand type(s) for {type(self).__name__} and {type(other).__name__}')


your_num = Rational()
your_num1 = Rational(4, 16)
your_num2 = Rational(-1, -16)
your_num3 = Rational(0, 7)
your_num4 = Rational(9, 7)
your_num5 = Rational(3, 3)

print(your_num5.rational())
print(your_num5.floating())
your_num5.numerator = 6
print(your_num5.rational())
print(your_num5.floating())

your_num6 = your_num5 / your_num
your_num5 *= your_num
your_num -= your_num
print(your_num6.rational())
print(your_num5.rational())
print(your_num.rational())

print(your_num5 == your_num6)
print(your_num1 < your_num3)
print(your_num4 <= your_num6)
