from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category',
                    'updated_date', 'image_tag')
    prepopulated_fields = {'slug': ('product_name',)}

    fieldsets = (
        ('Required Details', {
            'fields': ('product_name', 'model_no', 'product_category',
                       'product_details', 'slug', 'main_product_image'),
            'classes': ('required',)
        }),
        ('Optional', {
            'fields': ('addtional_image_1', 'addtional_image_2', 'addtional_image_3',
                       'addtional_image_4', 'addtional_image_5',),
            'classes': ('optional',)
        })
    )

admin.site.register(Product, ProductAdmin)
