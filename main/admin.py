from django.contrib import admin

from . import models

# Register your models here.

# registering Todo model
admin.site.register(models.Todo)

# register Done model
admin.site.register(models.Done)