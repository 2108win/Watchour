"""Watchour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),
    path('account/', include('account.urls')),
    path('orders/', include('orders.urls')),
    path('store/product-list/', store_views.product_list, name='product_list'),
    # path('store/add-product/', store_views.add_product, name='add_product'),
    # path('store/delete-product/<int:product_id>/', store_views.delete_product, name='delete_product'),
    # path('store/modify-product/<int:product_id>/', store_views.modify_product, name='modify_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)