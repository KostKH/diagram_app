from django.contrib import admin

from .models import City, PlanFact


class CityAdmin(admin.ModelAdmin):
    '''Класс для вывода на странице админа
    информации по городам.'''

    list_display = ('id', 'name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class PlanFactAdmin(admin.ModelAdmin):
    '''Класс для вывода на странице админа
    информации по план-факту.'''

    list_display = ('id', 'city', 'year', 'plan', 'fact',)
    list_filter = ('year', 'city',)
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
admin.site.register(PlanFact, PlanFactAdmin)
