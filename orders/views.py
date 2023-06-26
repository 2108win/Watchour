from django.shortcuts import render, redirect
import datetime

from .forms import OrderForm
from .models import Order, OrderProduct
from store.models import Product
from carts.models import CartItem


def place_order(
    request,
    total=0,
    quantity=0,
):
    """
    Hàm hiển thị trang XÁC NHẬN THÔNG TIN THANH TOÁN,
    lưu thông tin người nhận vào bảng order

    render: trang xác nhận thông tin thanh toán (payments.html)
    """
    current_user = request.user

    # Nếu số lượng giỏ hàng nhỏ hơn hoặc bằng 0, hãy chuyển hướng trở lại cửa hàng
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("store")

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Lưu trữ tất cả thông tin thanh toán bên trong bảng Order
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address_line_1 = form.cleaned_data["address_line_1"]
            data.province = form.cleaned_data["province"]
            data.district = form.cleaned_data["district"]
            data.ward = form.cleaned_data["ward"]
            data.order_note = form.cleaned_data["order_note"]
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()

            # Tạo mã đơn hàng
            yr = int(datetime.date.today().strftime("%Y"))
            dt = int(datetime.date.today().strftime("%d"))
            mt = int(datetime.date.today().strftime("%m"))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, order_number=order_number)
            context = {
                "order": order,
                "cart_items": cart_items,
                "total": total,
                "tax": tax,
                "grand_total": grand_total,
            }
            return render(request, "orders/payments.html", context)
    else:
        return redirect("checkout")


def order_complete(request):
    """
    Hàm hiển thị trang HOÀN TẤT THANH TOÁN,

    Chuyển hết cart_item sang order_product.
    Xóa cart_item.
    Xuất các thông tin của order_product ra màn hình

    render: trang hoàn tất thanh toán (order_complete.html)
    """
    order_number = request.GET.get("order_number")

    try:
        order = Order.objects.get(is_ordered=False, order_number=order_number)
        # Đánh dấu đơn hàng đã thanh toán
        order.is_ordered = True
        order.save()

        # Chuyển hết cart_item thành order_product
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            order_product = OrderProduct()
            order_product.order_id = order.id
            order_product.user_id = request.user.id
            order_product.product_id = item.product_id
            order_product.quantity = item.quantity
            order_product.product_price = item.product.price
            order_product.ordered = True
            order_product.save()

            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            product.save()

        # Xóa hết cart_item
        CartItem.objects.filter(user=request.user).delete()

        ordered_products = OrderProduct.objects.filter(order_id=order.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.product_price * i.quantity

        context = {
            "order": order,
            "ordered_products": ordered_products,
            "order_number": order.order_number,
            "subtotal": subtotal,
        }
        return render(request, "orders/order_complete.html", context)
    except Exception:
        return redirect("home")
