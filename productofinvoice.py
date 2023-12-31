from product import Product
class ProductOfInvoice(Product):
    def __init__(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date, sold_quantity):
        super().__init__(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
        self.__sold_quantity = sold_quantity

    def get_sold_quantity(self):
        return self.__sold_quantity

    def set_sold_quantity(self, sold_quantity):
        self.__sold_quantity = sold_quantity

    def calculate_total_price(self):
        return self.get_selling_price() * self.__sold_quantity

    def calculate_total_amount(self):
        return self.get_selling_price() * self.__sold_quantity

    #2 hàm calculate_total_price và calculate_total_amount giống nhau vì không biết phí VAT, tiền ship, hoặc các chi phí phụ khác,... nên thành tiền và tổng tiền đều sẽ được tính bằng giá mỗi sản phẩm * số lượng