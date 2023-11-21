from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def validate_title(value):
    letters = value.split()

    if len(letters) == 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    content = models.TextField()
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category")
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)

    def __str__(self):
        return self.title
