from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

CATEGORY_PICTURES = (('Commercial', 'Commercial'),
                     ('Documentary', 'Documentary'),
                     ('Fashion', 'Fashion'),
                     ('Fashion Photography', 'Fashion Photography'),
                     ('Food', 'Food'), ('Landscape', 'Landscape'),
                     ('People Photography', 'People Photography'),
                     ('Pet Photography', 'Pet Photography'),
                     ('Photojournalism', 'Photojournalism'),
                     ('Portrait Photography', 'Portrait Photography'),
                     ('Product Photography', 'Product Photography'),
                     ('Scientific', 'Scientific'), ('Sports', 'Sports'),
                     ('Sports Photography', ' Sports Photography'),
                     ('Street Photography', 'Street Photography'),
                     ('Travel', 'Travel'), ('Underwater', 'Underwater'),
                     ('Weddings', 'Weddings'), ('Wildlife', 'Wildlife'))


class PictureModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    category = models.CharField(max_length=100, choices=CATEGORY_PICTURES, default='Uncategorized')
    like = models.ManyToManyField(User, related_name='pictures', blank=True, null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.like.count()

    def get_absolute_url(self):
        return reverse('home')
