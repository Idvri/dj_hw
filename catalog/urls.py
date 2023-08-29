from django.urls import path

from catalog.views import home_page, contact_page, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('products/', ProductListView.as_view(), name='products'),
]
