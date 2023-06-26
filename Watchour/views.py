from django.shortcuts import render
from django.db.models import Sum
from store.models import Product
from category.models import Category


def home(request):
    categories = Category.objects.all()[:7]

    products = Product.objects.annotate(total_sold=Sum('orderproduct__quantity')).order_by('-total_sold')[:20]
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html', context=context)
