from django.shortcuts import render
from products.models import ProductList, ProductCategory

def show_category_products_list(request):
    return render(request, 'category_view/category_view.html', {})