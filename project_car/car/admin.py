from django.contrib import admin
from car.models import Car

admin.site.site_header = "CAR DASHBOARD"

class CarModel(admin.ModelAdmin):
    list_display = ['id','name', 'year']
    list_filter = ['name']
    search_fields = ['name']
    exclude = ['year']

admin.site.register(Car, CarModel)

