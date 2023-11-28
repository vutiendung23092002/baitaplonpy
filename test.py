from datetime import datetime, timedelta

class Product:
    def __init__(self, product_id, name, price_sell, price_buy, quantity, manufacture_date, expiry_date):
        self.product_id = product_id
        self.name = name
        self.price_sell = price_sell
        self.price_buy = price_buy
        self.quantity = quantity
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date

class InvoiceItem:
    def __init__(self, product_id, name, quantity, price_sell):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price_sell = price_sell
        self.total_price = quantity * price_sell

class Invoice:
    def __init__(self, invoice_id, date):
        self.invoice_id = invoice_id
        self.date = date
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class ManagerProduct:
    def __init__(self):
        self.products = []
        self.invoices = []

    def add_product(self, product):
        self.products.append(product)

    def search_product(self, product_id):
        # Tìm kiếm sản phẩm theo product_id và trả về thông tin sản phẩm
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    def display_products(self):
        # Hiển thị danh sách sản phẩm
        if not self.products:
            print("Không có sản phẩm nào trong danh sách.")
        else:
            print("Danh sách các sản phẩm:")
            for product in self.products:
                print(f"Mã hàng hóa: {product.product_id}")
                print(f"Tên hàng hóa: {product.name}")
                print(f"Giá bán: {product.price_sell}")
                print(f"Giá nhập: {product.price_buy}")
                print(f"Số lượng: {product.quantity}")
                print(f"Ngày sản xuất: {product.manufacture_date}")
                print(f"Hạn sử dụng: {product.expiry_date}")
                print("------------------------------")
    def calculate_daily_revenue_per_product(self, date):
        # Tính doanh thu hàng ngày của từng sản phẩm
        daily_revenue_per_product = {}
        for product in self.products:
            daily_revenue_per_product[product.product_id] = 0

        for invoice in self.invoices:
            if invoice.date == date:
                for item in invoice.items:
                    if item.product_id in daily_revenue_per_product:
                        daily_revenue_per_product[item.product_id] += item.total_price

        return daily_revenue_per_product
    def calculate_daily_revenue_store(self, month, year):
        # Tính tổng doanh thu hàng ngày của cửa hàng
        daily_revenue_store = 0

        for invoice in self.invoices:
            invoice_month = invoice.date.month
            invoice_year = invoice.date.year

            if invoice_month == month and invoice_year == year:
                for item in invoice.items:
                    daily_revenue_store += item.total_price

        return daily_revenue_store
    def sort_revenue(self, ascending=True):
        # Sắp xếp doanh thu hàng hóa
        product_revenues = {}

        for invoice in self.invoices:
            for item in invoice.items:
                if item.product_id not in product_revenues:
                    product_revenues[item.product_id] = item.total_price
                else:
                    product_revenues[item.product_id] += item.total_price

        sorted_revenues = sorted(product_revenues.items(), key=lambda x: x[1], reverse=not ascending)
        return sorted_revenues
    def top_products_by_revenue(self, n, high=True):
        # Hiển thị top sản phẩm có doanh thu cao nhất hoặc thấp nhất
        product_revenues = {}

        for invoice in self.invoices:
            for item in invoice.items:
                if item.product_id not in product_revenues:
                    product_revenues[item.product_id] = item.total_price
                else:
                    product_revenues[item.product_id] += item.total_price

        sorted_revenues = sorted(product_revenues.items(), key=lambda x: x[1], reverse=high)
        top_products = sorted_revenues[:n]
        return top_products
    def products_near_expiry(self):
        # Tổng hợp hàng hóa sắp hết hạn
        products_near_expiry = []

        current_date = datetime.now()

        for product in self.products:
            days_until_expiry = (product.expiry_date - current_date).days
            if days_until_expiry <= 42:  # 6 tuần = 42 ngày
                products_near_expiry.append(product)

        return products_near_expiry
    def update_product_info(self, product_id, new_info):
        # Sửa thông tin sản phẩm
        for product in self.products:
            if product.product_id == product_id:
                # Update thông tin sản phẩm
                if 'name' in new_info:
                    product.name = new_info['name']
                if 'price_sell' in new_info:
                    product.price_sell = new_info['price_sell']
                if 'price_buy' in new_info:
                    product.price_buy = new_info['price_buy']
                if 'quantity' in new_info:
                    product.quantity = new_info['quantity']
                if 'manufacture_date' in new_info:
                    product.manufacture_date = new_info['manufacture_date']
                if 'expiry_date' in new_info:
                    product.expiry_date = new_info['expiry_date']
                return True  # Trả về True nếu cập nhật thành công

        return False
    def delete_product(self, product_id):
        # Xóa sản phẩm
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True  # Trả về True nếu xóa thành công

        return False
    # def add_invoice(self, invoice):
    #     self.invoices.append(invoice)
    def sell_product(self, invoice_id, date, items):
        invoice = Invoice(invoice_id, date)
        for item in items:
            product = self.search_product(item.product_id)
            if product and product.quantity >= item.quantity:
                invoice_item = InvoiceItem(product.product_id, product.name, item.quantity, product.price_sell)
                invoice.add_item(invoice_item)
                product.quantity -= item.quantity
            else:
                print(f"Không đủ số lượng cho sản phẩm {item.product_id}")

        self.add_invoice(invoice)
        print("Đã bán hàng và thêm mới hóa đơn.")


# -------------------------------------------------------------------

def add_new_product(manager):
    product_id = input("Nhập mã hàng hóa: ")
    name = input("Nhập tên hàng hóa: ")
    price_sell = float(input("Nhập giá bán: "))
    price_buy = float(input("Nhập giá nhập: "))
    quantity = int(input("Nhập số lượng: "))
    manufacture_date = input("Nhập ngày sản xuất (YYYY-MM-DD): ")
    expiry_date = input("Nhập ngày hết hạn (YYYY-MM-DD): ")

    new_product = Product(product_id, name, price_sell, price_buy, quantity, manufacture_date, expiry_date)
    manager.add_product(new_product)
    print("Đã thêm mới hàng hóa thành công.")
def search_product(manager):
    product_id = input("Nhập mã hàng hóa cần tìm kiếm: ")
    product = manager.search_product(product_id)
    if product:
        print("Thông tin sản phẩm:")
        print(f"Mã hàng hóa: {product.product_id}")
        print(f"Tên hàng hóa: {product.name}")
        # In các thông tin khác của sản phẩm...
    else:
        print("Không tìm thấy sản phẩm.")

def update_product(manager):
    product_id = input("Nhập mã hàng hóa cần cập nhật: ")
    product = manager.search_product(product_id)
    if product:
        # Nhập thông tin mới cho sản phẩm...
        updated_info = {}  # Chuẩn bị thông tin mới cho sản phẩm cần cập nhật
        # Nhập các thông tin cần cập nhật từ người dùng và lưu vào updated_info
        manager.update_product_info(product_id, updated_info)
        print("Đã cập nhật thông tin sản phẩm.")
    else:
        print("Không tìm thấy sản phẩm.")
def sort_products_by_revenue(manager):
    ascending = input("Sắp xếp theo doanh thu cao đến thấp (c) hay thấp đến cao (l)? (c/l): ").lower()
    ascending_order = True if ascending == 'c' else False

    sorted_products = manager.sort_revenue(ascending_order)
    print("Danh sách sản phẩm được sắp xếp theo doanh thu:")
    for idx, product in enumerate(sorted_products, start=1):
        print(f"{idx}. Mã: {product[0]}, Doanh thu: {product[1]}")
def calculate_daily_revenue_store(manager):
    month = int(input("Nhập tháng cần thống kê (1-12): "))
    year = int(input("Nhập năm cần thống kê: "))
    daily_revenue = manager.calculate_daily_revenue_store(month, year)
    print(f"Doanh thu của cửa hàng trong tháng {month}/{year} là: {daily_revenue}")

def top_products_by_revenue(manager):
    n = int(input("Nhập số lượng hàng hóa cần hiển thị: "))
    high_low_choice = input("Doanh thu cao nhất (c) hoặc thấp nhất (l)? (c/l): ")
    ascending = True if high_low_choice.lower() == 'c' else False
    top_products = manager.top_products_by_revenue(n, ascending)
    print(f"Top {n} hàng hóa theo doanh thu {'cao nhất' if ascending else 'thấp nhất'}:")
    for idx, product in enumerate(top_products, start=1):
        print(f"{idx}. Mã: {product[0]}, Doanh thu: {product[1]}")

def display_near_expiry_products(manager):
    near_expiry_products = manager.products_near_expiry()
    if near_expiry_products:
        print("Các sản phẩm sắp hết hạn:")
        for product in near_expiry_products:
            print(f"Mã: {product.product_id}, Tên: {product.name}, Hạn sử dụng: {product.expiry_date}")
    else:
        print("Không có sản phẩm nào sắp hết hạn.")

def sell_product(manager):
    invoice_id = input("Nhập mã hóa đơn: ")
    date = input("Nhập ngày bán hàng (YYYY-MM-DD): ")
    items = []

    while True:
        product_id = input("Nhập mã sản phẩm: ")
        quantity = int(input("Nhập số lượng: "))

        items.append(InvoiceItem(product_id, "", quantity, 0))

        add_more = input("Thêm sản phẩm khác? (yes/no): ").lower()
        if add_more != 'yes':
            break

    manager.sell_product(invoice_id, date, items)

def delete_product(manager):
    product_id = input("Nhập mã hàng hóa cần xóa: ")
    success = manager.delete_product(product_id)
    if success:
        print("Đã xóa sản phẩm thành công.")
    else:
        print("Không tìm thấy sản phẩm cần xóa.")

# ------------------------------------------------------
def display_menu():
    print("===== MENU =====")
    print("1. Thêm mới hàng hóa")
    print("2. Tìm kiếm hàng hóa")
    print("3. Sửa thông tin hàng hóa")
    print("4. Sắp xếp theo doanh thu hàng hóa")
    print("5. Thống kê doanh thu theo ngày của cửa hàng")
    print("6. Thống kê top hàng hóa có doanh thu cao nhất, doanh thu thấp nhất")
    print("7. Hiển thị hàng hóa sắp hết hạn")
    print("8. Bán hàng")
    print("9. Xóa hàng hóa")
    print("10. Thoát chương trình")
# Chương trình chính
def main():
    manager = ManagerProduct()
    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            # Thêm mới hàng hóa
            # Gọi phương thức add_product của manager
            add_new_product(manager)
        elif choice == '2':
            # Tìm kiếm hàng hóa
            # Gọi phương thức search_product của manager
            search_product(manager)
        elif choice == '3':
            # Sửa thông tin hàng hóa
            # Gọi phương thức update_product_info của manager
            update_product(manager)
        elif choice == '4':
            # Sắp xếp theo doanh thu hàng hóa
            # Gọi phương thức sort_revenue của manager
            sort_products_by_revenue(manager)
        elif choice == '5':
            # Thống kê doanh thu theo ngày của cửa hàng
            date = input("Nhập ngày (YYYY-MM-DD): ")
            # Chuyển đổi chuỗi ngày nhập vào thành đối tượng datetime
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            # Gọi phương thức calculate_daily_revenue_store của manager với ngày đã chọn
            calculate_daily_revenue_store(manager)
        elif choice == '6':
            # Thống kê top hàng hóa có doanh thu cao nhất, doanh thu thấp nhất
            n = int(input("Nhập số lượng hàng hóa cần hiển thị: "))
            high_low_choice = input("Doanh thu cao nhất (c) hoặc thấp nhất (l)? (c/l): ")
            # Gọi phương thức top_products_by_revenue của manager với số lượng và lựa chọn
            top_products_by_revenue(manager)
        elif choice == '7':
            # Hiển thị hàng hóa sắp hết hạn
            # Gọi phương thức products_near_expiry của manager
            display_near_expiry_products(manager)
        elif choice == '8':
            # Bán hàng
            # Thêm mới hóa đơn
            # Gọi phương thức add_invoice của manager
            sell_product(manager)
        elif choice == '9':
            # Xóa hàng hóa
            # Gọi phương thức delete_product của manager
            delete_product(manager)
        elif choice == '10':
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
