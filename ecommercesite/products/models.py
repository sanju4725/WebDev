from django.db import models
from django.urls import reverse

# Create your models here.
class Catergory(models.Models):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    catergory = models.ForeignKey(Catergory, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(uploads='./products',blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse()