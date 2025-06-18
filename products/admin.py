from django.contrib import admin
from .models import Product, ProductMetaInformation, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductMetaInline(admin.StackedInline):
    model = ProductMetaInformation
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'demo_price', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductMetaInline, ProductImageInline]

# If you prefer registering manually:
# admin.site.register(Product)
# admin.site.register(ProductMetaInformation)
# admin.site.register(ProductImage)
