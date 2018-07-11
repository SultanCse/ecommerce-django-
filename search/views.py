from django.shortcuts import render
from products.models import ProductList
def show_searched_products_list(request):
    query = request.GET.get('q', None)
    if query is not None:
        products_list = ProductList.objects.filter(title__icontains=query)
        context = {
            'products_list_all': products_list
        }
        return render(request, 'search/view.html', context)

    products_list = ProductList.objects.none()
    context = {
            'products_list_all': products_list
        }
    return render(request, 'search/view.html', context)

# Create your views here.
