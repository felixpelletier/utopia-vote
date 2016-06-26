from django.contrib import admin

import models


@admin.register(models.Sujet)
class SujetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')


@admin.register(models.Poids)
class PoinsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poids', 'ordre')
    list_editable = ('ordre',)

admin.site.register(models.Vote)
admin.site.register(models.Periode)
