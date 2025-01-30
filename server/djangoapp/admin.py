from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
# Register the CarMake model
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_origin', 'founded_year')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by name

# Register the CarModel model
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')  # Fields to display in the list view
    list_filter = ('car_make', 'type')  # Enable filtering by car make and type
    search_fields = ('name', 'car_make__name')  # Enable search by model name and car make name

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
