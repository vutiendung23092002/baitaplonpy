from manageProduct import ManageProduct
import datetime

def display_menu():
    print("\nMENU:")
    print("1. Thêm hàng hoá")
    print("2. Hiển thị danh sách hàng hoá")
    print("3. Thoát")

    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        print("_________________________________________________")
        add_product(manager)
        display_menu()
    elif choice == 2:
        display_products(manager)
        display_menu()
    elif choice == 3:
        print("Đã thoát.")
        exit()
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        choice = int(input("Nhập lựa chọn của bạn: "))

def add_product(manager):
    while True:
        try:
            product_code = input("Nhập mã hàng hoá: ")
            product_name = input("Nhập tên hàng hoá: ")
            selling_price = float(input("Nhập giá bán: "))
            cost_price = float(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng: "))
            manufacture_date = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
            expiration_date = input("Nhập hạn sử dụng (dd/mm/yyyy): ")

            # Kiểm tra số lượng, giá nhập, giá bán > 0
            if quantity <= 0 or selling_price <= 0 or cost_price <= 0:
                raise ValueError("Số lượng và giá tiền phải lớn hơn 0.")

            # Kiểm tra định dạng ngày tháng
            datetime.datetime.strptime(manufacture_date, '%d/%m/%Y')
            datetime.datetime.strptime(expiration_date, '%d/%m/%Y')

            manager.add_product(product_code, product_name, selling_price, cost_price, quantity, manufacture_date, expiration_date)
            print("Hàng hoá đã được thêm thành công!")
            break  # Thoát vòng lặp nếu đã thêm hàng hoá thành công
        except ValueError as e:
            print(f"Lỗi: {e}")

def display_products(manager):
    manager.display_all_products()

manager = ManageProduct()
display_menu()
