class Rectangle:
    def __init__(self, width=1.0, length=1.0):
        self.width = width
        self.length = length

    def perimetr(self):
        return (self._width + self._length) * 2

    def area(self):
        return self._width * self._length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if not isinstance(value, float):
            raise Exception(f'The number u want to set as width must be floating-point number')
        if not 0 < value < 20:
            raise Exception(f'The number u want to set as width must be somewhere in between 0.0 and 20.0')
        self._width = value

    @length.setter
    def length(self, value):
        if not isinstance(value, float):
            raise Exception(f'The number u want to set as width must be floating-point number')
        if not 0 < value < 20:
            raise Exception(f'The number u want to set as width must be somewhere in between 0.0 and 20.0')
        self._length = value


rect = Rectangle(5.0, 11.0)
print(f'The area of rectangle is: {rect.area()}\n'
      f'The perimetr of rectangle is: {rect.perimetr()}')
rect2 = Rectangle()
print(f'\nThe area of rectangle is: {rect2.area()}\n'
      f'The perimetr of rectangle is: {rect2.perimetr()}')
rect2.length = 2.0
rect2.width = 5.0
print(f'\nThe area of rectangle is: {rect2.area()}\n'
      f'The perimetr of rectangle is: {rect2.perimetr()}')
