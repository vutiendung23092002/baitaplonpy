* Quy tắc chung:
Sử dụng tiếng Anh hoặc tiếng việt (không dấu) và ghi rõ ràng:
Đặt tên mô tả rõ ràng về mục đích hoặc chức năng của biến/hàm.
Sử dụng chữ thường và gạch dưới để phân cách các từ trong tên biến/hàm (snake_case).
Sử dụng tên biến/hàm có ý nghĩa để mô tả dữ liệu hoặc thông tin mà biến đại diện.
Tránh sử dụng tên biến không rõ ràng như a, b, temp,...
Tránh sử dụng tên biến global giống với tên biến local trong một hàm hoặc lớp.
Chữ cái đầu của biến/hàm viết in thường

Phân chia công việc Nhóm 02:

- Dũng: 
	+ Thêm hàng hoá (Các hàng hoá được thêm mới sẽ được thêm vào list_product.txt)
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
	+ Tìm kiếm hàng hoá
- Hưng: 
	+ Xoá hàng hoá (Sau khi xoá cập nhật lại list_product.txt)
	+ Viết báo cáo

- Sau khi xong phần thêm sản phẩm và thêm hoá đơn anh em lên git lấy code về làm tiếp chức năng của mình (link git ghim ở nhóm facebook)
làm xong một chức năng thì gửi lên nhóm, lỗi hay bug k làm được nữa cũng gửi lên nhóm

- Viết tets case: Ai làm chức năng gì thì tự viết test case cho chức năng đó.

- invoice.py: class hoá đơn
- product.py: claas sản phẩm
- productofinvoice.py: sản phẩm thuộc hoá đơn
- manageProduct.py: lớp quản lý hàng hoá
- main.py: lớp main (Chạy chương trình mở cmd trong thư mục sau đó chạy lệnh: py main.py hoặc python main.py)

- list_product.txt: Lưu danh sách sản phẩm
- list_invoice.txt: Lưu danh sách hoá đơn (Mã hoá đơn, ngày tạo, tổng tiền)
- list_invoice_product.txt: Lưu danh sách sản phẩm thuộc hoá đơn
- update_status.txt: Gắn cờ các sản phẩm sắp hết hạn sử dụng đã được giảm giá để không bị giảm giá thêm lần nữa

** Anh em không vào file list_product.txt, list_invoice.txt, list_invoice_product.txt, update_status.txt sửa linh tinh nhé sai định dạng là chạy lỗi đấy