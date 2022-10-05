import math


class Rational:
    def __init__(self, numerator=1, denominator=2):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise Exception(f'Numerator and denominator must be integer numbers')
        if not denominator:
            raise Exception(f'Denominator can\'t be equal to zero')

        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator

        greatest_common_divisor = math.gcd(numerator, denominator)
        if not numerator or greatest_common_divisor == 1:
            self.__numerator = numerator
            self.__denominator = denominator
        else:
            self.__numerator = int(numerator / greatest_common_divisor)
            self.__denominator = int(denominator / greatest_common_divisor)

    def print_rational(self):
        print(f'Rational: {self.__numerator}/{self.__denominator}')

    def print_floating(self):
        print(f'Floating-point number: {self.__numerator / self.__denominator}')


your_num = Rational()
your_num.print_rational()
your_num.print_floating()

your_num1 = Rational(4, 16)
your_num1.print_rational()
your_num1.print_floating()

your_num2 = Rational(1, 16)
your_num2.print_rational()
your_num2.print_floating()

your_num3 = Rational(0, 7)
your_num3.print_rational()
your_num3.print_floating()

your_num4 = Rational(9, 7)
your_num4.print_rational()
your_num4.print_floating()

your_num5 = Rational(3, 3)
your_num5.print_rational()
your_num5.print_floating()
