from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField( blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerceapp:products_by_category', args=[self.slug])


class Products(models.Model):

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField( blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to='product', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerceapp:prod_category', args= [self.category.slug, self.slug])