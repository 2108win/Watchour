from .models import Category


def menu_links(request):
    """
    Hàm trả về danh sách các thể loại hiện có

    return với dạng dict
    """
    links = Category.objects.all()
    return dict(links=links)
