from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import DashboardView, contact_page, ProductListView, ProductDeleteView, ProductCreateView, \
    ProductDetailView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('contact/', contact_page, name='contact'),
    path('products/', ProductListView.as_view(), name='list'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
