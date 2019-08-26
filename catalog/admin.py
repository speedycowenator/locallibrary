from django.contrib import admin

# Register your models here.
from catalog.models import Article

#admin.site.register(Book)
#admin.site.register(Author)

#admin.site.register(BookInstance)


# Register the admin class with the associated model

# Register the Admin classes for Book using the decorator
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('date_publication','author', 'topic')
