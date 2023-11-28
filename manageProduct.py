from product import Product
import datetime

class ManageProduct:
    def __init__(self):
        self.product_add = []
        self.product_show = []

#Lấy dữ liệu sản phẩm từ list_product.txt
    def load_products_from_file_product(self):
        try:
            with open('list_product.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    product_info = line.strip().split(',')
                    product = Product(product_info[0], product_info[1], float(product_info[2]), float(product_info[3]), int(product_info[4]), product_info[5], product_info[6])
                    self.product_show.append(product)
        except FileNotFoundError:
            print("File list_product.txt không tồn tại.")

#Hàm lấy sản phẩm
    def get_products(self):
        self.load_products_from_file_product()
        return self.product_show

#in ra sản phẩm theo định dạng
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

#Hàm kiểm tra xem mã sản phẩm có tồn tại chưa
    def check_by_code(self, search_code):
        self.product_show = []
        self.load_products_from_file_product()
        for product in self.product_show: 
            if product.get_product_code() == search_code:
                return True
        return False

#hàm tạo sản phẩm
    def set_product(self, product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date):
        product = Product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
        self.product_add.append(product)

#Hàm tìm kiếm theo tên sản phẩm
    def search_by_name(self, search_name):
        self.product_show = []
        found_products = []
        self.load_products_from_file_product()
        for product in self.product_show:
            if search_name.lower() in product.get_product_name().lower():
                found_products.append(product)
        if found_products:
            print("Kết quả tìm kiếm theo tên:")
            self.display_products(found_products)
        else:
            print("Không tìm thấy sản phẩm phù hợp với tên đã nhập.")

#hàm hiển  thị tất cả sản phẩm
    def display_all_products(self):
        self.product_show = []
        self.load_products_from_file_product()
        if len(self.product_show) == 0:
            print("Không có hàng hoá nào trong danh sách.")
        else:
            self.display_products(self.product_show)

#hàm tính tổng doanh thu sản phẩm để tiến hành sắp xếp
    def calculate_product_revenue(self, order='asc'):
        product_revenue = {}  # Lưu trữ tổng doanh thu của từng sản phẩm
        # Đọc dữ liệu từ file list_product.txt để có thông tin về giá sản phẩm
        products_info = {}
        with open('list_product.txt', 'r', encoding='utf-8') as product_file:
            for line in product_file:
                product_info = line.strip().split(',')
                products_info[product_info[0]] = float(product_info[2])  # Lưu giá sản phẩm theo mã sản phẩm
        # Tạo danh sách sản phẩm từ file list_product.txt
        all_products = products_info.keys()
        # Tính tổng doanh thu của từng sản phẩm từ danh sách sản phẩm đã tạo
        for product_code in all_products:
            if product_code in products_info:
                product_revenue[product_code] = 0  # Khởi tạo doanh thu của sản phẩm là 0
        # Đọc dữ liệu từ file list_invoice_products.txt để tính tổng doanh thu của các sản phẩm có trong hoá đơn
        with open('list_invoice_products.txt', 'r', encoding='utf-8') as invoice_products_file:
            for line in invoice_products_file:
                invoice_product_info = line.strip().split(',')
                product_code = invoice_product_info[1]  # Mã sản phẩm trong file list_invoice_products.txt
                quantity_sold = int(invoice_product_info[3])  # Số lượng sản phẩm đã bán
                if product_code in product_revenue:
                    product_revenue[product_code] += quantity_sold * products_info.get(product_code, 0)
        # Sắp xếp danh sách sản phẩm theo tổng doanh thu và thứ tự order
        sorted_products = sorted(product_revenue.items(), key=lambda x: x[1], reverse=(order.lower() == 'desc'))
        return sorted_products

# Hiển thị các hàng hoá sắp hết hạn
    def display_near_expired_products(self):
        today = datetime.datetime.now()
        near_expired_products = []
        updated_products = []
        # Đọc thông tin sản phẩm từ file list_product.txt và kiểm tra sản phẩm sắp hết hạn
        with open('list_product.txt', 'r', encoding='utf-8') as file:
            for line in file:
                product_info = line.strip().split(',')
                expiration_date = datetime.datetime.strptime(product_info[6], '%d/%m/%Y')
                time_until_expiration = expiration_date - today
                weeks_until_expiration = time_until_expiration.days / 1
                # Kiểm tra sản phẩm sắp hết hạn và cập nhật trạng thái của sản phẩm
                if 0 <= weeks_until_expiration <= 6:
                    near_expired_products.append(product_info)
                    if check_update_status(product_info[0]):
                        updated_products.append(product_info[0])
        # Hiển thị thông tin sản phẩm sắp hết hạn và trạng thái cập nhật
        print("Các sản phẩm sắp hết hạn:")
        for product in near_expired_products:
            expiration_date = datetime.strptime(product[6], '%d/%m/%Y')
            time_until_expiration = expiration_date - today
            weeks_until_expiration = time_until_expiration.days / 7
            update_status_text = "Đã cập nhật" if product[0] in updated_products else "Chưa cập nhật"
            print(f"Mã sản phẩm: {product[0]}, Tên sản phẩm: {product[1]}, Hạn sử dụng: {product[6]}, Trạng thái cập nhật: {update_status_text}")

# Cập nhật giá vào file list_product.txt
    def check_update_status(self, product_code):
        with open('update_status.txt', 'r') as file:
            updated_products = file.read().splitlines()
            return product_code in updated_products

    def update_status(self, product_code):
        with open('update_status.txt', 'a') as file:
            file.write(f"{product_code}\n")

    def update_price_for_near_expired_products(self):
        today = datetime.datetime.now()
        # Đọc thông tin sản phẩm từ file list_product.txt và kiểm tra sản phẩm sắp hết hạn
        updated_lines = []  # Danh sách chứa các dòng đã được cập nhật

        with open('list_product.txt', 'r', encoding='utf-8') as file:
            for line in file:
                product_info = line.strip().split(',')
                expiration_date = datetime.datetime.strptime(product_info[6], '%d/%m/%Y')
                time_until_expiration = expiration_date - today
                print(time_until_expiration)
                weeks_until_expiration = time_until_expiration.days / 1
                print(weeks_until_expiration)
                # Kiểm tra và cập nhật giá cho sản phẩm sắp hết hạn chưa được cập nhật
                if 0 <= weeks_until_expiration <= 6 and not self.check_update_status(product_info[0]):
                    if weeks_until_expiration >= 3:
                        new_price = float(product_info[2]) * 0.765  # Giảm 23.5%
                    else:
                        new_price = float(product_info[2]) * 0.431  # Giảm 56.9%
                    # Cập nhật giá mới cho sản phẩm trong danh sách
                    product_info[2] = str(int(new_price))
                    updated_product_info = ','.join(product_info)
                    updated_lines.append(updated_product_info)
                    # Ghi nhận rằng sản phẩm đã được cập nhật
                    self.update_status(product_info[0])
                else:
                    updated_lines.append(line.strip())

        # Ghi các dòng đã được cập nhật và không cần cập nhật vào file
        with open('list_product.txt', 'w', encoding='utf-8') as file:
            for updated_line in updated_lines:
                file.write(updated_line + '\n')
        print("Đã cập nhật giá cho các sản phẩm sắp hết hạn.")

#Hàm cập nhật lại thông tin cho sản phẩm
    def update_product_info(self, product_code):
        updated_product_info = []
        for product in self.product_show:
            if product.get_product_code() == product_code:
                print("Nhập thông tin mới cho sản phẩm:")
                product_name = input("Tên hàng hoá: ")
                selling_price = float(input("Giá bán: "))
                cost_price = float(input("Giá nhập: "))
                quantity = int(input("Số lượng: "))
                manufacture_date = input("Ngày sản xuất (dd/mm/yyyy): ")
                expiration_date = input("Hạn sử dụng (dd/mm/yyyy): ")
                # Cập nhật thông tin sản phẩm
                product.set_product_name(product_name)
                product.set_selling_price(selling_price)
                product.set_cost_price(cost_price)
                product.set_quantity(quantity)
                product.set_manufacture_date(manufacture_date)
                product.set_expiration_date(expiration_date)
                print("Thông tin hàng hoá đã được cập nhật.")
            # Thêm thông tin sản phẩm vào danh sách cập nhật
            updated_product_info.append(
                f"{product.get_product_code()},{product.get_product_name()},"
                f"{product.get_selling_price()},{product.get_cost_price()},"
                f"{product.get_quantity()},{product.get_manufacture_date()},"
                f"{product.get_expiration_date()}\n"
            )
        # Cập nhật lại file list_product.txt
        with open('list_product.txt', 'w', encoding='utf-8') as file:
            for line in updated_product_info:
                file.write(line)

#Hàm xoá sản phẩm:
    def delete_product_by_code(self, product_code):
        # Đọc thông tin sản phẩm từ file list_product.txt và tìm sản phẩm cần xoá
        lines_to_keep = []
        deleted = False
        with open('list_product.txt', 'r', encoding='utf-8') as file:
            for line in file:
                product_info = line.strip().split(',')
                # Kiểm tra xem sản phẩm có mã sản phẩm cần xoá hay không
                if product_info[0] == product_code:
                    deleted = True  # Đánh dấu sản phẩm đã được xoá
                else:
                    lines_to_keep.append(line.strip())
        # Nếu sản phẩm được tìm thấy và xoá, ghi lại thông tin các sản phẩm còn lại vào file
        if deleted:
            with open('list_product.txt', 'w', encoding='utf-8') as file:
                for line in lines_to_keep:
                    file.write(line + '\n')
            print(f"Sản phẩm với mã {product_code} đã được xoá thành công.")
        else:
            print(f"Không tìm thấy sản phẩm với mã {product_code}.")