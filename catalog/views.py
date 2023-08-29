from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'main/home_page.html'


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'main/contact_page.html')


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
