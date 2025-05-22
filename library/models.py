from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.name }"
    


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="book")
    name = models.CharField(max_length=50)
    book= models.FileField(upload_to="pdf/")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.name }"
