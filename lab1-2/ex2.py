import math


class Rational:
    def __init__(self, numerator=1, denominator=2):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise Exception(f'Numerator and denominator must be integer numbers')
        if not denominator:
            raise Exception(f'Denominator can\'t be equal to zero')
        self.numerator = numerator
        self.denominator = denominator

    def rational(self):
        if self.numerator < 0 and self.denominator < 0:
            tmp_numerator = -self.numerator
            tmp_denominator = -self.denominator
        else:
            tmp_numerator = self.numerator
            tmp_denominator = self.denominator

        greatest_common_divisor = math.gcd(tmp_numerator, tmp_denominator)

        if not tmp_numerator or greatest_common_divisor == 1:
            pass
        else:
            tmp_numerator = int(tmp_numerator/greatest_common_divisor)
            tmp_denominator = int(tmp_denominator/greatest_common_divisor)
        return f'{tmp_numerator}/{tmp_denominator}'

    def floating(self):
        return f'{self.numerator / self.denominator}'


your_num = Rational()
print(f'Rational: {your_num.rational()}')
print(f'Floating-point number: {your_num.floating()}')

your_num1 = Rational(4, 16)
print(f'Rational: {your_num1.rational()}')
print(f'Floating-point number: {your_num1.floating()}')

your_num2 = Rational(-1, -16)
print(f'Rational: {your_num2.rational()}')
print(f'Floating-point number: {your_num2.floating()}')

your_num3 = Rational(0, 7)
print(f'Rational: {your_num3.rational()}')
print(f'Floating-point number: {your_num3.floating()}')

your_num4 = Rational(9, 7)
print(f'Rational: {your_num4.rational()}')
print(f'Floating-point number: {your_num4.floating()}')

your_num5 = Rational(3, 3)
print(f'Rational: {your_num5.rational()}')
print(f'Floating-point number: {your_num5.floating()}')
