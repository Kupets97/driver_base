from django.contrib import admin

from comment.models import Comment  
from file.models import File
from .models import Person


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    show_change_link = True

class FileInlineAdmin(admin.StackedInline):
    model = File
    show_change_link = True

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'raiting', 'full_name', 'license')
    inlines = (CommentInlineAdmin,FileInlineAdmin)


admin.site.register(Person, PersonAdmin)
