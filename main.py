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
            selling_price = float(input("Nhập giá bán: "))
            cost_price = float(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng: "))
            # Kiểm tra số lượng, giá nhập, giá bán > 0
            if quantity <= 0 or selling_price <= 0 or cost_price <= 0:
                raise ValueError("Số lượng và giá tiền phải lớn hơn 0.")
            manufacture_date = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
            expiration_date = input("Nhập hạn sử dụng (dd/mm/yyyy): ")
            # Kiểm tra định dạng ngày tháng
            datetime.datetime.strptime(manufacture_date, '%d/%m/%Y')
            datetime.datetime.strptime(expiration_date, '%d/%m/%Y')
            manager.add_product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
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

def add_invoice(manager):
    products = manager.get_products()
    invoice_code = input("Nhập mã hoá đơn: ")
    invoice_date = input("Nhập ngày hoá đơn (dd/mm/yyyy): ")
    new_invoice = Invoice(invoice_code, invoice_date)

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

manager = ManageProduct()
display_menu()
