from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')


def contact_page(request):
    return render(request, 'main/contact_page.html')
