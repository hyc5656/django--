from django.contrib import admin
from app1.models import Author,Book,Publisher
# Register your models here.
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_n', 'last_n', 'email')
    search_fields = ('first_n', 'last_n')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
