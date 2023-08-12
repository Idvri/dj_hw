from django.shortcuts import render


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
