from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)