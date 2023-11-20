from productofinvoice import ProductOfInvoice

class Invoice:
    def __init__(self, invoice_code, invoice_date):
        self.__invoice_code = invoice_code
        self.__invoice_date = invoice_date
        self.__list_of_products = []  # Danh sách sản phẩm trong hoá đơn

    def get_invoice_code(self):
        return self.__invoice_code

    def set_invoice_code(self, invoice_code):
        self.__invoice_code = invoice_code

    def get_invoice_date(self):
        return self.__invoice_date

    def set_invoice_date(self, invoice_date):
        self.__invoice_date = invoice_date

    def get_list_of_products(self):
        return self.__list_of_products

    def add_product_to_invoice(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date, sold_quantity):
        product = ProductOfInvoice(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date, sold_quantity)
        self.__list_of_products.append(product)

    def calculate_total_invoice_amount(self):
        total_amount = 0
        for product in self.__list_of_products:
            total_amount += product.calculate_total_amount()
        return total_amount
