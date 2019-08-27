from django.contrib import admin

# Register your models here.
from Gavin import models
admin.site.register(models.UserInfo)
admin.site.register(models.Classify)
admin.site.register(models.Article)
admin.site.register(models.Comment)