import phonenumbers


class Product:
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = price
        self.description = description
        self.size = size

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise Exception(f'Name of the product can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'Name of the product can\'t contain only 1 letter')
        self.__name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise Exception(f'Price value must be a number')
        if value <= 0:
            raise Exception(f'Price value can\'t be less or equal to zero')
        self._price = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value.upper() not in ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']:
            raise Exception(f'There is no such size for the product')
        self.__size = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise Exception(f'In description there must be text value')
        if len(value) < 10:
            raise Exception(f'The length of description can\'t consist of less than 10 symbols')
        self._description = value

    def __str__(self):
        return f'\n\tName of the product: {self.__name}\n' \
               f'\tPrice(in $): {self._price}\n' \
               f'\tDescription: {self._description}\n' \
               f'\tSize: {self.__size}\n'


class Customer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise Exception(f'Name of the customer can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'Name of the customer can\'t contain only 1 letter')
        if not value[0].isupper() or not value[1:].islower():
            raise Exception(f'Name of the customer must start with a capital letter '
                            f'and the rest of the letters should be in lowercase')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not value.isalpha():
            raise Exception(f'Surname of the customer can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'Surname of the customer can\'t contain only 1 letter')
        if not value[0].isupper() or not value[1:].islower():
            raise Exception(f'Surname of the customer must start with a capital letter '
                            f'and the rest of the letters should be in lowercase')
        self.__surname = value

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not phonenumbers.is_possible_number(phonenumbers.parse(value)):
            raise Exception(f'Invalid phone number was entered')
        self.__mobile_phone = value

    def __str__(self):
        return f'\n\tName: {self.__surname} {self.__name}\n' \
               f'\tMobile phone: {self.__mobile_phone}\n'


class Order:
    def __init__(self, customer, *args):
        if not isinstance(customer, Customer):
            raise Exception(f'Customer parameter must be an instance of Customer class')
        if not all(isinstance(item, Product) for item in args):
            raise Exception(f'Each item parameter must be an instance of Product class')
        self.__customer = customer
        self.__ordered_items = {item: args.count(item) for item in args}

    def add_item(self, item):
        if not isinstance(item, Product):
            raise Exception(f'Item parameter u want to add must be an instance of Product class')
        if item not in self.__ordered_items:
            self.__ordered_items[item] = 1
        else:
            self.__ordered_items[item] += 1

    def delete_item(self, item):
        if not isinstance(item, Product):
            raise Exception(f'Item parameter u want to delete must be an instance of Product class')
        if item not in self.__ordered_items:
            raise Exception(f'u\'re trying to delete the item, that isn\'t in the order')
        else:
            if self.__ordered_items[item] == 1:
                self.__ordered_items.pop(item)
            else:
                self.__ordered_items[item] -= 1

    def total_value(self):
        if not self.__ordered_items:
            return 0
        total_check = 0
        for item in self.__ordered_items:
            total_check += item.price * self.__ordered_items[item]
        return total_check

    def get_items_info(self):
        if not self.__ordered_items:
            return f'No items added'
        tmp = ''
        for item in self.__ordered_items:
            tmp += item.__str__()
            if self.__ordered_items[item] > 1:
                tmp += f'\tQuantity: {self.__ordered_items[item]}\n'
        return tmp

    def __str__(self):
        return f'Info about customer: {self.__customer.__str__()}\n' \
               f'Info about added items: {self.get_items_info()}\n' \
               f'Total value of your order: {self.total_value()}$'


item1 = Product('shirt', 380, 'leon dee t-shirt. SS 2023', 'L')
item2 = Product('jeans', 480, 'diesel jeans. AF 2022', 'M')
item3 = Product('blazer', 810, 'mugler blazer from eco-leather. SS 2023', 'L')

customer1 = Customer('Daniel', 'Dziuban', '+380662055055')

order = Order(customer1, item1, item2, item3, item1)
order.add_item(item2)
order.delete_item(item1)
print(order.__str__())
