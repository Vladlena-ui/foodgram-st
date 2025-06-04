from django.contrib import admin
from .models import Meal, Component, Label, Quantity

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name', 'author__username')

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)

admin.site.register(Label)
admin.site.register(Quantity)