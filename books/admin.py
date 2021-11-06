from django.contrib import admin
from .models import Author,Book
# Register your models here.
class BookInLineAdmin(admin.TabularInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    inlines=[BookInLineAdmin]

admin.site.register(Author,AuthorAdmin)