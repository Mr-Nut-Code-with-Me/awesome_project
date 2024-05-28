from django.contrib import admin

from .models import Post, Category, Comment


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_filter = ("author", "category", "created_at", 'status')
    list_display = ('title', 'author', 'status', 'category')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentItemInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
