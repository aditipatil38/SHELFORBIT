from django.contrib import admin
from .models import Book, Library

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)