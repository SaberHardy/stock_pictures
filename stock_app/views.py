from django.shortcuts import render

from stock_app.models import PictureModel


def home(request):
    pictures = PictureModel.objects.all()
    pictures_count = pictures.count()
    context = {
        'pictures': pictures,
        'pictures_count': pictures_count,
    }
    return render(request, 'stock_app/index.html', context)


def gallery(request):
    pictures = PictureModel.objects.all()
    context = {'pictures': pictures}
    return render(request, 'stock_app/gallery.html', context)


def services(request):
    last_three = PictureModel.objects.all().order_by('-date_created')[:3]
    total_images = PictureModel.objects.all().count()
    context = {'last_three': last_three, 'total_images': total_images}
    return render(request, 'stock_app/services.html', context)


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
