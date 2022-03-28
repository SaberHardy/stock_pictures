from django.db import models


class PictureModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title
