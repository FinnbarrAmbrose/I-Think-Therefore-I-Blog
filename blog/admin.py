from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user  # Auto-assign author if missing
        obj.save()

# Register your models here.

admin.site.register(Comment)