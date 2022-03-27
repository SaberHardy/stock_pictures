from django.shortcuts import render


def home(request):
    return render(request, 'stock_app/index.html')


def gallery(request):
    return render(request, 'stock_app/gallery.html')


def services(request):
    return render(request, 'stock_app/services.html')


def about(request):
    return render(request, 'stock_app/about.html')


def contact(request):
    return render(request, 'stock_app/contact.html')
