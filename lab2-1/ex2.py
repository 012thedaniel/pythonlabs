import json
import phonenumbers
from datetime import datetime


ALL_TYPES_OF_PIZZA = ['Pizza', 'MondayPizza', 'TuesdayPizza', 'WednesdayPizza', 'ThursdayPizza',
                      'FridayPizza', 'SaturdayPizza', 'SundayPizza']


class Pizza:
    _max_additional_ingredients = 5

    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        self.name = name
        if not main_ingredients:
            raise Exception(f'ingredients value can\'t be empty')
        self._main_ingredients = []
        self._add_main_ingredients(main_ingredients)
        self.price = price
        if additional_ingredients:
            self._additional_ingredients = {}
            self.add_additional_ingredients(additional_ingredients)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception(f'pizza\'s name value must be a string')
        if not value:
            raise Exception(f'pizza\'s name can\'t be empty')
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not value:
            raise Exception(f'price value can\'t be empty')
        if not isinstance(value, int | float):
            raise Exception(f'price value must be a digit')
        if value <= 0:
            raise Exception(f'price value can\'t be equal or less than zero')
        self._price = value

    def _add_main_ingredients(self, main_ingredients):
        for ingredient in main_ingredients:
            if not ingredient:
                raise Exception(f'ingredient\'s name value can\'t be empty')
            if not isinstance(ingredient, str):
                raise Exception(f'ingredient\'s name value must be a string')
            with open('all_ingredients.json') as all_ingredients_file:
                all_ingredients = json.load(all_ingredients_file)
                if ingredient not in all_ingredients["ingredients"]:
                    raise Exception(f'pizzeria doesn\'t have such an ingredient')
            self._main_ingredients.append(ingredient)

    def add_additional_ingredients(self, additional_ingredients):
        if not hasattr(self, '_additional_ingredients'):
            setattr(self, '_additional_ingredients', {})
        for ingredient in additional_ingredients:
            if not ingredient:
                raise Exception(f'additional ingredient\'s name value can\'t be empty')
            if not isinstance(ingredient, str):
                raise Exception(f'additional ingredient\'s name value must be a string')
            with open('additional_ingredients.json') as additional_ingredients_file:
                additional_ingredients_json = json.load(additional_ingredients_file)
                if ingredient not in additional_ingredients_json:
                    raise Exception(f'pizzeria doesn\'t have such an additional ingredient({ingredient})')
            if sum(self._additional_ingredients.values()) == Pizza._max_additional_ingredients:
                raise Exception(f'u can\'t add more than {Pizza._max_additional_ingredients} '
                                f'additional ingredients to your pizza')
            if ingredient in self._additional_ingredients.keys():
                self._additional_ingredients[ingredient] += 1
            else:
                self._additional_ingredients[ingredient] = 1
            with open('additional_ingredients.json') as additional_ingredients_file:
                additional_ingredients = json.load(additional_ingredients_file)
                self.price += additional_ingredients[ingredient]

    def del_additional_ingredients(self, additional_ingredients):
        for ingredient in additional_ingredients:
            if not ingredient:
                raise Exception(f'additional ingredient\'s name value u\'re trying to delete can\'t be empty')
            if not isinstance(ingredient, str):
                raise Exception(f'additional ingredient\'s name value u\'re trying to delete must be a string')
            with open('additional_ingredients.json') as additional_ingredients_file:
                additional_ingredients_json = json.load(additional_ingredients_file)
                if ingredient not in additional_ingredients_json:
                    raise Exception(f'pizzeria doesn\'t have such an additional ingredient u\'re trying to delete')
            if ingredient not in self._additional_ingredients.keys():
                raise Exception(f'there\'s no such an additional ingredient in your pizza that u\'re trying to delete')
            if self._additional_ingredients[ingredient] == 1:
                self._additional_ingredients.pop(ingredient, None)
            else:
                self._additional_ingredients[ingredient] -= 1
            with open('additional_ingredients.json') as additional_ingredients_file:
                additional_ingredients_json = json.load(additional_ingredients_file)
                self.price -= additional_ingredients_json[ingredient]

    def _get_str_of_additional_ingredients(self):
        tmp = ''
        with open('additional_ingredients.json') as additional_ingredients_file:
            additional_ingredients_json = json.load(additional_ingredients_file)
            for ingredient in self._additional_ingredients:
                tmp += f'{ingredient}({self._additional_ingredients[ingredient]}x' \
                       f'{additional_ingredients_json[ingredient]}$), '
        return tmp[:-2]

    def __str__(self):
        if not hasattr(self, '_additional_ingredients'):
            return f'pizza\'s name: {self.name}\n' \
                   f'main ingredients: {", ".join(map(str, self._main_ingredients))}\n' \
                   f'price: {self.price}$\n'
        else:
            return f'pizza\'s name: {self.name}\n' \
                   f'main ingredients: {", ".join(map(str, self._main_ingredients))}\n' \
                   f'additional ingredients u added: {self._get_str_of_additional_ingredients()}\n' \
                   f'price: {self.price}$\n'


class MondayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class TuesdayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class WednesdayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class ThursdayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class FridayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class SaturdayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


class SundayPizza(Pizza):
    def __init__(self, name, main_ingredients, price, additional_ingredients=None):
        super().__init__(name, main_ingredients, price, additional_ingredients)


def create_pizza_of_the_day(*additional_ingredients):
    today = datetime.now().weekday()
    pizza_dictionary = {
        "0": MondayPizza,
        "1": TuesdayPizza,
        "2": WednesdayPizza,
        "3": ThursdayPizza,
        "4": FridayPizza,
        "5": SaturdayPizza,
        "6": SundayPizza
    }
    with open('pizza_of_the_day.json') as f:
        pizza_otd_list = json.load(f)
        pizza_otd = pizza_otd_list[today]
        return pizza_dictionary[str(today)](pizza_otd["name"], pizza_otd["main_ingredients"],
                                            pizza_otd["price"], additional_ingredients)


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
        return f'\nName: {self.__surname} {self.__name}\n' \
               f'Mobile phone: {self.__mobile_phone}\n'


class Order:
    def __init__(self, customer, *args):
        if not isinstance(customer, Customer):
            raise Exception(f'Customer parameter must be an instance of Customer class')
        if not all(type(item).__name__ in ALL_TYPES_OF_PIZZA for item in args):
            raise Exception(f'Each item parameter must be an instance of class Pizza or it\'s derived class')
        self._customer = customer
        self._ordered_items = {item: args.count(item) for item in args}

    def add_item(self, item):
        if not type(item).__name__ in ALL_TYPES_OF_PIZZA:
            raise Exception(f'Item parameter u want to add must be an instance of class Pizza or it\'s derived class')
        if item not in self._ordered_items:
            self._ordered_items[item] = 1
        else:
            self._ordered_items[item] += 1

    def delete_item(self, item):
        if not type(item).__name__ in ALL_TYPES_OF_PIZZA:
            raise Exception(f'Item parameter u want to delete must be an instance '
                            f'of class Pizza or it\'s derived class')
        if item not in self._ordered_items:
            raise Exception(f'u\'re trying to delete the item, that isn\'t in the order')
        else:
            if self._ordered_items[item] == 1:
                self._ordered_items.pop(item, None)
            else:
                self._ordered_items[item] -= 1

    def total_value(self):
        if not self._ordered_items:
            return 0
        total_check = 0
        for item in self._ordered_items:
            total_check += item.price * self._ordered_items[item]
        return total_check

    def get_items_info(self):
        if not self._ordered_items:
            return f'No items added\n\n'
        tmp = ''
        for item in self._ordered_items:
            tmp += item.__str__() + f'\t--Quantity: {self._ordered_items[item]}--\n\n'
        return tmp 

    def __str__(self):
        return f'--Info about customer: {self._customer}\n' \
               f'--Info about added items:\n{self.get_items_info()}' \
               f'--Total value of your order: {self.total_value()}$'


customer1 = Customer('Daniel', 'Dziuban', '+380662055055')

pizza1 = create_pizza_of_the_day()

pizza2 = create_pizza_of_the_day("bacon", "cheddar")
pizza2.add_additional_ingredients(["onion"])
pizza2.add_additional_ingredients(["parmigiano", "bacon"])
pizza2.del_additional_ingredients(["bacon"])

order1 = Order(customer1, pizza1, pizza1)
order1.add_item(pizza2)
order1.add_item(pizza2)
order1.delete_item(pizza2)
print(order1)
