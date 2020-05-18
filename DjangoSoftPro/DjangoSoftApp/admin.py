from django.contrib import admin


from .models import VegetableDatabase,FruitsDatabase

class AdminVegetableDatabase(admin.ModelAdmin):
    list_display =['Product_name', 'MRP', 'Price', 'Save', 'Big_image', 'First_image', 'Second_image', 'Category', 'About_product', 'Storage', 'Benefits', 'Weight_policy']
class AdminFruitDatabase(admin.ModelAdmin):
    list_display =['Product_name', 'MRP', 'Price', 'Save', 'Big_image', 'First_image', 'Second_image', 'Category', 'About_product', 'Storage', 'Benefits', 'Weight_policy']

admin.site.register(VegetableDatabase,AdminVegetableDatabase)
admin.site.register(FruitsDatabase,AdminFruitDatabase)

