from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Label(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=100)
    measurement_unit = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.measurement_unit})"

class Meal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='meals/images/')
    description = models.TextField()
    components = models.ManyToManyField(
        Component,
        through='Quantity',
        related_name='meals'
    )
    labels = models.ManyToManyField(Label, related_name='meals')
    time_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Quantity(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

class GroceryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)