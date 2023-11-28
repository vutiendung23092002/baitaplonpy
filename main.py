from manageProduct import ManageProduct
from invoice import Invoice
from productofinvoice import ProductOfInvoice
import datetime

def display_menu():
    print("\nMENU:")
    print("1. Thêm hàng hoá")
    print("2. Tìm kiếm hàng hoá")
    print("3. Hiển thị danh sách hàng hoá")
    print("4. Thêm hoá đơn")
    print("5. Sắp sếp sản phẩm theo doanh thu")
    print("6. Tốp 5 sản phẩm có doanh thu cao nhất")
    print("7. Hiển thị danh sách các sản phẩm sắp hết hạn sử dụng(còn 6 ngày)")
    print("8. Cập nhật giá mới cho các sản phẩm sắp hết hạn sử dụng")
    print("9. Sửa thông tin sản phẩm")
    print("10. Xoá sản phẩm")
    print("11. Tính tổng doanh thu theo ngày")
    print("0. Thoát")

    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        print("____________________________________________________________________________________________________")
        add_product(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 2:
        print("____________________________________________________________________________________________________")
        search_by_name(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 3:
        print("____________________________________________________________________________________________________")
        display_products(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 4:
        print("____________________________________________________________________________________________________")
        add_invoice(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 5:
        print("____________________________________________________________________________________________________")
        display_sorted_products_revenue(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 6:
        print("____________________________________________________________________________________________________")
        display_top_5_products_revenue(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 7:
        print("____________________________________________________________________________________________________")
        manager.display_near_expired_products()
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 8:
        print("____________________________________________________________________________________________________")
        manager.update_price_for_near_expired_products()
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 9:
        print("____________________________________________________________________________________________________")
        update_product(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 10:
        print("____________________________________________________________________________________________________")
        delete_product(manager)
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 11:
        print("____________________________________________________________________________________________________")
        calculate_daily_revenue()
        print("____________________________________________________________________________________________________")
        display_menu()
    elif choice == 0:
        print("Đã thoát.")
        exit()
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        choice = int(input("Nhập lựa chọn của bạn: "))

def add_product(manager):
    while True:
        try:
            product_code = input("Nhập mã hàng hoá: ")
            #Kiểm tra xem id có trùng không
            if manager.check_by_code(product_code) == True:
                raise ValueError("Mã hàng hoá đã tồn tại")
            product_name = input("Nhập tên hàng hoá: ")
            selling_price = int(input("Nhập giá bán: "))
            cost_price = int(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng: "))
            # Kiểm tra số lượng, giá nhập, giá bán > 0
            if quantity <= 0 or selling_price <= 0 or cost_price <= 0:
                raise ValueError("Số lượng và giá tiền phải lớn hơn 0.")
            manufacture_date = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
            expiration_date = input("Nhập hạn sử dụng (dd/mm/yyyy): ")
            # Kiểm tra định dạng ngày tháng
            datetime.datetime.strptime(manufacture_date, '%d/%m/%Y')
            datetime.datetime.strptime(expiration_date, '%d/%m/%Y')
            manager.set_product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
            with open('list_product.txt', 'a', encoding='utf-8') as file:
                file.write(f"{product_code},{product_name},{selling_price},{cost_price},{quantity},{manufacture_date},{expiration_date}\n")
            print("Hàng hoá đã được thêm thành công!")
            break
        except ValueError as e:
            print(f"Lỗi: {e}")

def display_products(manager):
    manager.display_all_products()

def search_by_name(manager):
    keyword = str(input("Nhập tên sản phẩm cần tìm kiếm: "))
    manager.search_by_name(keyword)

#kiểm tra để mã hóa đơn không bị trùng
def is_invoice_code_exist(invoice_code):
    with open('list_invoice.txt', 'r', encoding='utf-8') as file:
        for line in file:
            info = line.strip().split(',')
            if info[0] == invoice_code:
                return True
    return False

# Kiểm tra đúng định dạng ngày của hóa đơn
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_date(date_text):
    while True:
        date_components = date_text.split('/')
        if len(date_components) == 3:
            day, month, year = date_components
            try:
                day = int(day)
                month = int(month)
                year = int(year)

                if month in [1, 3, 5, 7, 8, 10, 12]:
                    days_in_month = 31
                elif month in [4, 6, 9, 11]:
                    days_in_month = 30
                elif month == 2:
                    if is_leap_year(year):
                        days_in_month = 29
                    else:
                        days_in_month = 28
                else:
                    print("Tháng không hợp lệ. Nhập lại (dd/mm/yyyy): ")
                    date_text = input("Nhập ngày hoá đơn (dd/mm/yyyy): ")
                    continue

                if 1 <= day <= days_in_month:
                    return f"{day:02d}/{month:02d}/{year:04d}"
                else:
                    print("Ngày không hợp lệ. Nhập lại (dd/mm/yyyy): ")
            except ValueError:
                pass
        print("Định dạng ngày không đúng. Nhập lại (dd/mm/yyyy): ")
        date_text = input("Nhập ngày hoá đơn (dd/mm/yyyy): ")

def add_invoice(manager):
    products = manager.get_products()
    while True:
        invoice_code = input("Nhập mã hoá đơn: ")

        if is_invoice_code_exist(invoice_code):
            print("Mã hoá đơn đã tồn tại. Vui lòng nhập mã khác.")
        else:
            break

    invoice_date = input("Nhập ngày hoá đơn (dd/mm/yyyy): ")
    validated_date = validate_date(invoice_date)
    new_invoice = Invoice(invoice_code, validated_date)
    invoice_products_info = []  # Danh sách thông tin sản phẩm trong hoá đơn

    while True:
        print("Thêm sản phẩm vào hoá đơn:")
        product_code = input("Nhập mã sản phẩm: ")

        # Kiểm tra xem sản phẩm có tồn tại và đủ số lượng không
        selected_product = None
        for product in products:
            if product.get_product_code() == product_code:
                selected_product = product
                break

        if selected_product is None:
            print("Sản phẩm không tồn tại.")
        else:
            quantity_to_add = int(input("Nhập số lượng sản phẩm: "))
            if quantity_to_add > selected_product.get_quantity():
                print("Sản phẩm không đủ số lượng.")
            else:
                selected_product.set_quantity(selected_product.get_quantity() - quantity_to_add)  # Giảm số lượng trong kho
                product_for_invoice = ProductOfInvoice(
                    selected_product.get_product_code(),
                    selected_product.get_product_name(),
                    selected_product.get_selling_price(),
                    selected_product.get_cost_price(),
                    quantity_to_add,
                    selected_product.get_manufacture_date(),
                    selected_product.get_expiration_date(),
                    quantity_to_add
                )
                new_invoice.add_product_to_invoice(
                    product_for_invoice.get_product_code(),
                    product_for_invoice.get_product_name(),
                    product_for_invoice.get_selling_price(),
                    product_for_invoice.get_cost_price(),
                    product_for_invoice.get_quantity(),
                    product_for_invoice.get_manufacture_date(),
                    product_for_invoice.get_expiration_date(),
                    product_for_invoice.get_sold_quantity()
                )
                invoice_products_info.append(f"{selected_product.get_product_code()},{selected_product.get_product_name()},{quantity_to_add}")

                # Cập nhật lại số lượng sản phẩm trong file list_product.txt
                updated_product_info = []
                with open('list_product.txt', 'r', encoding='utf-8') as file:
                    for line in file:
                        info = line.strip().split(',')
                        if info[0] == selected_product.get_product_code():
                            info[4] = str(int(info[4]) - quantity_to_add)  # Giảm số lượng sản phẩm
                        updated_product_info.append(','.join(info))

                with open('list_product.txt', 'w', encoding='utf-8') as file:
                    for line in updated_product_info:
                        file.write(f"{line}\n")

                print("Sản phẩm đã được thêm vào hoá đơn.")

        choice = input("Bạn có muốn thêm sản phẩm khác không? (Y/N): ")
        if choice.lower() != 'y':
            break  # Nếu người dùng chọn 'N', thoát khỏi vòng lặp

    # Thêm hoá đơn vào file
    with open('list_invoice.txt', 'a', encoding='utf-8') as file:
        file.write(f"{new_invoice.get_invoice_code()},{new_invoice.get_invoice_date()},{new_invoice.calculate_total_invoice_amount()}\n")

    # Thêm thông tin sản phẩm trong hoá đơn vào file
    with open('list_invoice_products.txt', 'a', encoding='utf-8') as file:
        for product_info in invoice_products_info:
            file.write(f"{invoice_code},{product_info}\n")
    print("Hoá đơn đã được thêm thành công!")

#Kiểm tra đjnh dạng ngày của tính tổng doanh thu theo ngày
def validate_date_input(date_input):
    while True:
        try:
            formatted_date_input = datetime.datetime.strptime(date_input, '%d/%m/%Y').strftime('%d/%m/%Y')
            return formatted_date_input
        except ValueError:
            print("Định dạng ngày không hợp lệ. Vui lòng nhập lại.")
            date_input = input("Nhập ngày cần tính tổng doanh thu (dd/mm/yyyy): ")

#Tính tổng doanh thu theo ngày
def calculate_daily_revenue():
    date_input = input("Nhập ngày cần tính tổng doanh thu (dd/mm/yyyy): ")
    formatted_date_input = validate_date_input(date_input)
    total_revenue = 0
    with open('list_invoice.txt', 'r', encoding='utf-8') as invoice_file:
        for line in invoice_file:
            invoice_data = line.strip().split(',')
            invoice_date = invoice_data[1]

            if invoice_date == formatted_date_input:
                total_revenue += float(invoice_data[2])
    print(f"Tổng doanh thu cho ngày {formatted_date_input}: {total_revenue}")

def display_sorted_products_revenue(manager):
    order = input("Nhập lựa chọn sắp xếp (asc/desc): ")
    sorted_products = manager.calculate_product_revenue(order)
    print("Danh sách sản phẩm được sắp xếp theo tổng doanh thu:")
    # Đọc dữ liệu từ file list_product.txt để có thông tin về tên sản phẩm
    products_info = {}
    with open('list_product.txt', 'r', encoding='utf-8') as product_file:
        for line in product_file:
            product_info = line.strip().split(',')
            products_info[product_info[0]] = product_info[1]  # Lưu tên sản phẩm theo mã sản phẩm

    for product_code, revenue in sorted_products:
        product_name = products_info.get(product_code, 'Tên không tồn tại')  # Lấy tên sản phẩm từ mã sản phẩm
        print(f"Mã sản phẩm: {product_code}, Tên sản phẩm: {product_name}, Tổng doanh thu: {revenue}")

def display_top_5_products_revenue(manager):
    sorted_products = manager.calculate_product_revenue('desc')
    print("5 sản phẩm có doanh thu cao nhất:")
    # Đọc dữ liệu từ file list_product.txt để có thông tin về tên sản phẩm
    products_info = {}
    with open('list_product.txt', 'r', encoding='utf-8') as product_file:
        for line in product_file:
            product_info = line.strip().split(',')
            products_info[product_info[0]] = product_info[1]  # Lưu tên sản phẩm theo mã sản phẩm
    top_5_products = sorted_products[:5]  # Chọn 5 sản phẩm có doanh thu cao nhất
    for product_code, revenue in top_5_products:
        product_name = products_info.get(product_code, 'Tên không tồn tại')  # Lấy tên sản phẩm từ mã sản phẩm
        print(f"Mã sản phẩm: {product_code}, Tên sản phẩm: {product_name}, Tổng doanh thu: {revenue}")

#Cập nhật sản phẩm
def update_product(manager):
    try:
        product_code = input("Nhập mã hàng hoá cần sửa: ")

        if not manager.check_by_code(product_code):
            raise ValueError("Mã hàng hoá không tồn tại.")

        manager.update_product_info(product_code)
    except ValueError as e:
        print(f"Lỗi: {e}")

#Xoá sản phẩm với mã id nhập từ bàn phím
def delete_product(manager):
    try:
        product_code = input("Nhập mã hàng hoá cần sửa: ")
        if not manager.check_by_code(product_code):
            raise ValueError("Mã hàng hoá không tồn tại.")
        manager.delete_product_by_code(product_code)
    except ValueError as e:
        print(f"Lỗi: {e}")

manager = ManageProduct()
display_menu()