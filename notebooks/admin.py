from django.contrib import admin
from .models import Category, Notes

# Register your models here.


admin.site.register(Notes)
admin.site.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('note_topic',), }