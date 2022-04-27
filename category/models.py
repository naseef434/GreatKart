from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name