from django.shortcuts import render

from stock_app.models import PictureModel


def home(request):
    return render(request, 'stock_app/index.html')


def gallery(request):
    pictures = PictureModel.objects.all()
    context = {'pictures': pictures}
    return render(request, 'stock_app/gallery.html', context)


def services(request):
    return render(request, 'stock_app/services.html')


def about(request):
    return render(request, 'stock_app/about.html')


def contact(request):
    return render(request, 'stock_app/contact.html')


def detail(request, id):
    pict_detailed = PictureModel.objects.get(id=id)
    context = {
        'pict_detailed': pict_detailed
    }
    return render(request, 'stock_app/detail_pic.html', context)
