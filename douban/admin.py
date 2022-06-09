from django.contrib import admin

# Register your models here.

from douban.models.bookModel import bookModel

# admin.site.register(Book)


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('bid', 'btitle', 'bscore', 'bdate')
    search_fields = ('bid', 'btitle',)
    ordering = ('bid', )


admin.site.register(bookModel, BookModelAdmin)