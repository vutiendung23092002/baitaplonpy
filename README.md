* Quy tắc chung:
Sử dụng tiếng Anh hoặc tiếng việt (không dấu) và ghi rõ ràng:
Đặt tên mô tả rõ ràng về mục đích hoặc chức năng của biến/hàm.
Sử dụng chữ thường và gạch dưới để phân cách các từ trong tên biến/hàm (snake_case).
Sử dụng tên biến/hàm có ý nghĩa để mô tả dữ liệu hoặc thông tin mà biến đại diện.
Tránh sử dụng tên biến không rõ ràng như a, b, temp,...
Tránh sử dụng tên biến global giống với tên biến local trong một hàm hoặc lớp.
Chữ cái đầu của biến/hàm viết in thường

- invoice.py: class hoá đơn

- product.py: claas sản phẩm

- productofinvoice.py: sản phẩm thuộc hoá đơn

- manageProduct.py: lớp quản lý hàng hoá
	+ load_products_from_file() hàm đọc dữ liệu sản phẩm từ file
	+ display_products() hàm hiển thị danh sách sản phẩm theo định dạng
	+ check_by_code() hàm kiểm tra xem mã sản phẩm nhập vào có tồn tại trong product.txt chưa
	+ add_product() hàm thêm sản phẩm vào
	+ search_by_name() hàm tìm sản phẩm theo tên sản phẩm
	+ display_all_products() hàm hiển thị tất cả sản phẩm

- main.py: lớp main

- list_product.txt: Lưu danh sách sản phẩm

** Anh em không vào file list_product.txt sửa linh tinh nhé

Phân chia công việc:
- Dũng: 
	+ Thêm hàng hoá (Các hàng hoá được thêm mới sẽ được thêm vào list_product.txt)
	+ Tìm kiếm hàng hoá
	+ Hiển thị danh sách hàng hoá
- Bách:
	+ Thêm hoá đơn (Các hoá đơn được thêm mới sẽ được thêm vào list_invoice.txt)
	+ Tính tổng doanh thu theo ngày của cửa hàng
- Cường:
	+ Sắp xếp tổng doanh thu của từng mặt hàng
	+ Hiển thị 5 mặt hàng có doanh thu cao nhất
- Quang:
	+ Tổng hợp các hàng hoá đang có trong cửa hàng mà sắp hết hạn sử dụng, tính giá trị mới cho mặt hàng đó
	+ Tính tổng doanh thu theo ngày của từng mặt hàng
- Hoàng:
	+ Sửa thông tin hàng hoá (Sau khi sửa cập nhật vào list_product.txt)
	+ Mới ra viện cho làm thế thôi nhé :)))
- Hưng: 
	+ Xoá hàng hoá (Sau khi xoá cập nhật lại list_product.txt)
	+ Viết báo cáo

- Viết tets case: Ai làm chức năng gì thì tự viết test case cho chức năng đó.