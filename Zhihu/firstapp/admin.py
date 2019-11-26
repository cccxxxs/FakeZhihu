from django.contrib import admin

# Register your models here.


from firstapp.models import People, Article
admin.site.register(People)
admin.site.register(Article)

