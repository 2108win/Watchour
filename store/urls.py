from django.urls import path
from . import views
from .views import add_product, product_list, delete_product, modify_product

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('add-product/', add_product, name='add_product'),
    path('product-list/', product_list, name='product_list'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('modify-product/<int:product_id>/', modify_product, name='modify_product'),
]