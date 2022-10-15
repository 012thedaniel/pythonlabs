class BinaryTree:

    def __init__(self, product_code, price):
        self.left = None
        self.right = None
        self.product_code = product_code
        self.price = price

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code):
        if not isinstance(product_code, int):
            raise TypeError("Product code must be a digit")
        if product_code <= 0:
            raise ValueError("Product code must be a positive number")

        self.__product_code = product_code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("Price must be a digit")
        if price <= 0:
            raise ValueError("Price must be a positive number")

        self.__price = price

    def insert(self, product_code, price):
        if self.product_code == product_code:
            raise ValueError("Product with such code already exists")

        if product_code < self.product_code:
            if self.left:
                self.left.insert(product_code, price)
            else:
                self.left = BinaryTree(product_code, price)
        else:
            if self.right:
                self.right.insert(product_code, price)
            else:
                self.right = BinaryTree(product_code, price)

    def get_price(self, product_code):
        if product_code < self.product_code:
            if not self.left:
                raise ValueError(f'{product_code} was not found')

            return self.left.get_price(product_code)
        elif product_code > self.product_code:
            if not self.right:
                raise ValueError(f'{product_code} was not found')

            return self.right.get_price(product_code)
        else:
            return self.price


root = BinaryTree(1, 10)
root.insert(2, 20)
root.insert(3, 30)
root.insert(4, 40)
root.insert(5, 50)

input_data = input("Enter product code and number of products you are looking for: ").split()
try:
    code_of_product = int(input_data[0])
    num_of_products = int(input_data[1])
    cost = num_of_products * root.get_price(code_of_product)
    print(cost)
except Exception as e:
    print(e)
