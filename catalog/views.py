from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, DetailView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'main/contact_page.html')


class DashboardView(TemplateView):
    template_name = 'main/includes/inc_main_title.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:list')
