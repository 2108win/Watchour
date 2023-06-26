from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from orders.models import Order, OrderProduct
from carts.models import Cart, CartItem
from .forms import RegistrationForm
from account.models import Account
from carts.views import _cart_id

import requests


def register(request):
    """
    Hàm hiển thị trang ĐĂNG KÝ,
    thực hiện việc ĐĂNG KÝ của người dùng.

    Lấy thông tin từ form -> tạo user mới -> lưu vào CSDL.

    render: Trang đăng ký (register.html).
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.is_active = True
            user.save()

            messages.success(
                request=request,
                message="Đăng ký thành công"
            )
            return redirect('login')
        else:
            messages.error(request=request, message="Đăng ký thất bại")
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


def login(request):
    """
    Hàm hiển thị trang ĐĂNG NHẬP,
    thực hiện việc ĐĂNG NHẬP của user.

    Xác thực người dùng.
    Nếu người dùng tồn tại:
        Gán user vào thuộc tính user của từng sản phẩm trong giỏ hàng hiện tại (class cart_items).
    Nếu người dùng tồn tại:
        Thông báo ĐĂNG NHẬP thất bại.

    render: Trang đăng nhập (login.html).

    Trường hợp thanh toán khi chưa đăng nhập:
        Sau khi nhấn nút thanh toán -> chuyển đến trang đăng nhập.
        Đăng nhập xong thì redirect: Trang tiếp theo sau khi nhấn nút thanh toán.
    """
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart)
                if cart_items.exists():
                    for item in cart_items:
                        item.user = user
                        item.save()
            except Exception:
                pass
            auth.login(request=request, user=user)
            messages.success(request=request, message="Đăng nhập thành công")

            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split("=") for x in query.split("&"))
                if "next" in params:
                    next_page = params["next"]
                    return redirect(next_page)
            except Exception:
                return redirect('home')
        else:
            messages.error(request=request, message="Đăng nhập thất bại")
    context = {
        'email': email if 'email' in locals() else '',
        'password': password if 'password' in locals() else '',
    }
    return render(request, 'account/login.html', context=context)


@login_required(login_url="login")
def logout(request):
    """
    Hàm thực hiện việc ĐĂNG XUẤT của user.

    Thông báo đăng xuất thành công và redirect: Trang đăng nhập (login.html)
    """
    auth.logout(request)
    messages.success(request=request, message="Bạn đã đăng xuất")
    return redirect('login')


@login_required(login_url="login")
def dashboard(request):
    """
    Hàm hiển thị trang LỊCH SỬ MUA HÀNG,
    thực hiện việc XEM LỊCH SỬ MUA HÀNG của user.

    Xuất thông các đơn hàng và các sản phẩm mà user đã đặt mua.
    Sắp xếp các đơn từ mới nhất -> cũ nhất.

    render: Trang lịch sử mua hàng (dashboard.html)
    """
    orders = Order.objects.filter(user=request.user).order_by("-updated_at")
    order_products = OrderProduct.objects.filter(user=request.user)

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(orders, 3)
    paged_order = paginator.get_page(page)
    order_count = orders.count()

    context = {
        'orders': paged_order,
        'order_count': order_count,
        'order_products': order_products,
    }
    return render(request, "account/dashboard.html", context=context)


def forgotPassword(request):
    """
    Hàm hiển thị trang QUÊN MẬT KHẨU,
    thực hiện việc NHẬP EMAIL CỦA ACCOUNT ĐÃ QUÊN MẬT KHẨU của user.

    Lấy email mà user nhập để xác thực user.
    Nếu user tồn tại:
        Lưu id của user vào request.session['uid'].
        redirect: Trang đặt lại mật khẩu (reset_password.html).
    Nếu user không tồn tại:
        Thông báo tài khoản không tồn tại
        render: Trang quên mật khẩu (forgotPassword.html).
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Account.objects.get(email__exact=email)
        except Exception:
            user = None

        if user is not None:
            request.session['uid'] = user.pk
            messages.info(request=request, message='Hãy tạo mật khẩu mới')
            return redirect('reset_password')
        else:
            messages.error(request=request,
                           message="Tài khoản này không tồn tại")

    context = {
        'email': email if 'email' in locals() else '',
    }
    return render(request, "account/forgotPassword.html", context=context)


def reset_password(request):
    """
    Hàm hiển thị trang ĐẶT LẠI MẬT KHẨU,
    thực hiện việc ĐẶT LẠI MẬT KHẨU của user.

    Lấy id từ request.session['uid'] đã lưu ở hàm forgotPassword -> truy xuất user cần đổi mật khẩu.
    Lấy mật khẩu mới cập nhật vào CSDL.

    Nếu password == confirm_password:
        Thông báo đổi mật khẩu thành công.
        redirect: Trang đăng nhập (login.html).
    Nếu password != confirm_password:
        Thông báo mật khẩu không trùng khớp.
        render: Trang đặt lại mật khẩu (reset_password.html).
    """
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, message="Đổi mật khẩu thành công")
            return redirect('login')
        else:
            messages.error(request, message="Mật khẩu không trùng khớp")
    return render(request, 'account/reset_password.html')
