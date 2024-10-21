from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category)
    published = models.DateField()

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

