from django.contrib import admin
from .models import Post, Tag, Author, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("author", "tags", "date")  # ✅ valid fields now
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "created_at")
    list_filter = ("created_at", "post")
    search_fields = ("user_name", "user_email", "text")

admin.site.register(Author)
admin.site.register(Tag)
