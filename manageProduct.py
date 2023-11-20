from product import Product

class ManageProduct:
    def __init__(self):
        self.product_list = [] 

    def add_product(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date):
        product = Product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
        self.product_list.append(product)

    def display_all_products(self):
        if len(self.product_list) == 0:
            print("Không có hàng hoá nào trong danh sách.")
        else:
            row1 = '+ {:-<5} + {:-<15} + {:-<10} + {:-<10} + {:-<10} + {:-<10} + {:-<10}  +'.format('','','','','','','')
            row2 = '+ {:<5} + {:<15} + {:<10} + {:<10} + {:<10} + {:<10} + {:<10}  +'.format('MHH','Tên hàng hoá','Số lượng','Giá bán','Giá nhập','NSX','HSD')
            print("Danh sách hàng hoá:")
            print(row1)
            print(row2)
            print(row1)
            for product in self.product_list:
                row = '+ {:<5} + {:<15} + {:<10} + {:<10} + {:<10} + {:<10} + {:<10}  +'.format(product.get_product_code(), product.get_product_name(), product.get_quantity(), product.get_selling_price(), product.get_cost_price(), product.get_manufacture_date(), product.get_expiration_date())
                print(row)

            print(row1)