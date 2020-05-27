from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 255)
    size = models.IntegerField()
    bio = models.TextField(max_length=255)
    price = models.FloatField()
    product_image = models.ImageField(default=None, upload_to='uploads')
    

    #add new value to db
    def get_absolute_url(self):
        return reverse('products:product_list')

    def __str__(self):
        return self.name



