from product import Product

class ManageProduct:
    def __init__(self):
        self.product_add = []
        self.product_show = []

    def load_products_from_file(self):
        try:
            with open('list_product.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    product_info = line.strip().split(',')
                    product = Product(product_info[0], product_info[1], float(product_info[2]), float(product_info[3]), int(product_info[4]), product_info[5], product_info[6])
                    self.product_show.append(product)
        except FileNotFoundError:
            print("File list_product.txt không tồn tại.")

    def display_products(self, products):
        row1 = '+ {:-<5} + {:-<15} + {:-<10} + {:-<10} + {:-<10} + {:-<10} + {:-<10}  +'.format('', '', '', '', '', '', '')
        row2 = '+ {:<5} + {:<15} + {:<10} + {:<10} + {:<10} + {:<10} + {:<10}  +'.format('MHH', 'Tên hàng hoá', 'Số lượng', 'Giá bán', 'Giá nhập', 'NSX', 'HSD')
        print("Danh sách hàng hoá:")
        print(row1)
        print(row2)
        print(row1)
        for product in products:
            row = '+ {:<5} + {:<15} + {:<10} + {:<10} + {:<10} + {:<10} + {:<10}  +'.format(product.get_product_code(), product.get_product_name(), product.get_quantity(), product.get_selling_price(), product.get_cost_price(), product.get_manufacture_date(), product.get_expiration_date())
            print(row)
        print(row1)

    def check_by_code(self, search_code):
        self.product_show = []
        self.load_products_from_file()
        for product in self.product_show: 
            if product.get_product_code() == search_code:
                return True
        return False

    def add_product(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date):
        product = Product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
        self.product_add.append(product)

    def search_by_name(self, search_name):
        self.product_show = []
        found_products = []
        self.load_products_from_file()
        for product in self.product_show:
            if search_name.lower() in product.get_product_name().lower():
                found_products.append(product)
        if found_products:
            print("Kết quả tìm kiếm theo tên:")
            self.display_products(found_products)
        else:
            print("Không tìm thấy sản phẩm phù hợp với tên đã nhập.")

    def display_all_products(self):
        self.product_show = []
        self.load_products_from_file()
        if len(self.product_show) == 0:
            print("Không có hàng hoá nào trong danh sách.")
        else:
            self.display_products(self.product_show)
