from django.contrib import admin
from .models import Category, Blog, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    # Prepopulation for slug
    prepopulated_fields = {'slug': ('title',)}

    # Formatting how Blog columns will be displayed on the admin page
    list_display = ('title', 'category', 'author', 'status', 'is_featured')

    # Search fields
    search_fields = ('id', 'title', 'category__category_name', 'status')

    # Add editable fields
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)