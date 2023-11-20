class Product:
    def __init__(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date):
        self.__product_code = product_code
        self.__product_name = product_name
        self.__selling_price = selling_price
        self.__cost_price = cost_price
        self.__quantity = quantity
        self.__manufacture_date = manufacture_date
        self.__expiration_date = expiration_date

    def get_product_code(self):
        return self.__product_code

    def set_product_code(self, product_code):
        self.__product_code = product_code

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_selling_price(self):
        return self.__selling_price

    def set_selling_price(self, selling_price):
        self.__selling_price = selling_price

    def get_cost_price(self):
        return self.__cost_price

    def set_cost_price(self, cost_price):
        self.__cost_price = cost_price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_manufacture_date(self):
        return self.__manufacture_date

    def set_manufacture_date(self, manufacture_date):
        self.__manufacture_date = manufacture_date

    def get_expiration_date(self):
        return self.__expiration_date

    def set_expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date