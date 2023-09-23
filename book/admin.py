from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Book, Author, Category


@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    search_fields = ('title', 'author',)
    list_display = ('title', 'author', 'category',)
    list_filter = ('author',)


@admin.register(Author)
class AuthorAdmin(ImportExportActionModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
