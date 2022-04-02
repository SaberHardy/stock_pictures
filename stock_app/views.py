from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from stock_app.forms import RegisterForm, AddPictureForm
from stock_app.models import PictureModel


def home(request):
    pictures = PictureModel.objects.all()
    pictures_count = pictures.count()
    context = {
        'pictures': pictures,
        'pictures_count': pictures_count,
        'total_user': User.objects.all().count()
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


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User name or password is incorrect')
    context = {
    }
    return render(request, 'stock_app/accounts/login.html', context)


def register_page(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'stock_app/accounts/login.html', context)


@login_required
def logout_page(request):
    logout(request)
    return render(request, 'stock_app/accounts/login.html')


@login_required
def delete(request, id):
    deletes_pict = get_object_or_404(PictureModel, id=id)
    deletes_pict.delete()
    return redirect('gallery')


def like_unlike_picture(request, id):
    id_liked = request.POST.get('picture_liked')
    pict_liked = get_object_or_404(PictureModel, id=id_liked)
    liked = False
    user_id = request.user.id
    if pict_liked.like.filter(id=user_id).exists():
        pict_liked.like.remove(request.user)
        liked = False
    else:
        pict_liked.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('detail', args=[str(id)]))


def add_picture(request):
    title = 'Create'
    form = AddPictureForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'stock_app/add_picture_form.html', context)


def update_picture(request, id):
    title = 'Update'
    picture_update = get_object_or_404(PictureModel, id=id)
    form = AddPictureForm(request.POST or None,
                          request.FILES or None,
                          instance=picture_update)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'stock_app/add_picture_form.html', context)