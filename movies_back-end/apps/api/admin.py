from django.contrib import admin

from .models import Category, Movie, Hour, Booking

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Hour)
admin.site.register(Booking)
