from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'main/contact_page.html')


def products_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'main/products_page.html', context)
