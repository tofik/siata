from siata.gramy.models import Granie, Uczestnik
from django.contrib import admin

class AdminGranie(admin.ModelAdmin):
    list_display = ('id', 'date')

admin.site.register(Granie, AdminGranie)
admin.site.register(Uczestnik)
