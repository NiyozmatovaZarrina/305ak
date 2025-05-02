from django.contrib import admin
from .models import Book
# Register your models here.

  
@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_disply=["name","adress"," phone_number","email","website"]
    list_filter=["name","phone_number"]

