from django.urls import path

from catalog.views import DashboardView, contact_page, ProductListView, ProductDeleteView, ProductCreateView, \
    ProductDetailView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('contact/', contact_page, name='contact'),
    path('products/', ProductListView.as_view(), name='list'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
