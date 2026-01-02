from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.FAQ)
admin.site.register(models.OrgScale)
admin.site.register(models.Blog)
admin.site.register(models.TeamMember)
admin.site.register(models.Contact)
admin.site.register(models.Request)