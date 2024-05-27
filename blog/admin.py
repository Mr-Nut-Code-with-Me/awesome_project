from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_filter = ("author", "category")
    list_display = ('title', 'author', 'category')    
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)

