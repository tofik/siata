from siata.gramy.models import Granie, Uczestnik
from django.contrib import admin

class UczestnicyInLine(admin.TabularInline):
    model = Uczestnik
    extra = 12

class AdminGranie(admin.ModelAdmin):
    list_display = ('id', 'date')
    inlines = [UczestnicyInLine]

admin.site.register(Granie, AdminGranie)
#admin.site.register(Granie)
admin.site.register(Uczestnik)
