from django.urls import path

from catalog.views import DashboardView, contact_page, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('contact/', contact_page, name='contact'),
    path('products/', ProductListView.as_view(), name='products'),
]
