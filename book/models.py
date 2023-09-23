from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    audio = models.FileField(upload_to='book_audio', blank=True, null=True)
    image = models.ImageField(upload_to='book_images', null=True, blank=True)
    pdf = models.FileField(upload_to='book_source', blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title