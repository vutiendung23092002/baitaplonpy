from manageProduct import ManageProduct
import datetime

def display_menu():
    print("\nMENU:")
    print("1. Thêm hàng hoá")
    print("2. Tìm kiếm hàng hoá")
    print("3. Hiển thị danh sách hàng hoá")
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

manager = ManageProduct()
display_menu()
