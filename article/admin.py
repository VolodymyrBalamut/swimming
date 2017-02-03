from django.contrib import admin
from article.models import *
# Register your models here.
class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title',
              'article_image',
              'width_field',
              'height_field',
              'article_text']
    inlines = [ArticleInLine]
    list_filter = ['article_date']
class CountryAdmin(admin.ModelAdmin):
    fields = ['country_name',
              'country_text',
              'country_image',
              'country_image_width_field',
              'country_image_height_field',
              'country_icon',
              'country_icon_width_field',
              'country_icon_height_field',
              ]
    list_filter = ['country_name']
class SwimmerAdmin(admin.ModelAdmin):
    fields = ['name',
              'nationality',
              'birthday',
              'male',
              'swimmer_image',
              'swimmer_image_width_field',
              'swimmer_image_height_field']
    list_filter = ['nationality','male']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Distance)
admin.site.register(Style)
admin.site.register(Swimmer,SwimmerAdmin)
admin.site.register(Record)