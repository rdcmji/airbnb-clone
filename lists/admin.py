from django.contrib import admin
from . import models


@admin.register(models.List)
class listAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    pass
