from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory)
    price = models.DecimalField(decimal_places=2, max_digits=65)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='shop')

    def __str__(self):
        return self.title



