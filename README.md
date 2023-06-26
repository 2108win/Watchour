# Python - Django

- Cài đặt Python
  Phiên bản hiện tại đang sử dụng là Python 3.11.3
  check version: `python --version` hoặc `python3 --version`
- Cài đặt Django
  `pip install django`
  check version: `django-admin --version`

## Cài đặt các gói cần thiết:

`npm install` <br>
`pip install -r requirements.txt`<br>

# Chạy server:

- `py manage.py runserver` hoặc `django-admin manage.py runserver`

## Login

- Có thể trải nghiệm trang web mà không cần đăng nhập
- Đăng nhập với thông tin người dùng bình thường: `2345@gmail.com` `2345`, hoặc đăng kí mới.
- Đăng nhập với quyền admin: `nongmanhbh2001@gmail.com` `minhanh123`, hoặc tài khoản `1234@gmail.com` `1234`

## Những sửa đổi mới

- Cho phép thay đổi chế độ sáng tối
- Các sản phẩm bán chạy: Cập nhật tính năng xem các sản phẩm bán chạy tại url `http://127.0.0.1:8000/` Có thể kiểm tra trang này với việc mua thêm sản phẩm
- Chức năng admin `quản lý sản phẩm` tại url `http://127.0.0.1:8000/store/product-list/` Chỉ admin mới có quyền truy cập trang này, chỉ khi đăng nhập với quyền admin menu mới hiện ra chức năng này, chỉ admin mới có quyền thao tác với các chức năng trong menu này.
- ![Admin_menu](https://github.com/minhanh32001/Python/assets/62033936/1cce5416-03c9-4058-9b0e-8eeaa147a4aa)
