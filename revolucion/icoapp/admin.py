from django.contrib import admin
from .models import Ico


# Register your models here.
def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


# пишем класс для администрирования записей Ico - их активации и деактивации
class IcoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'starts', 'ends', 'days', 'rating', 'is_active']
    actions = [set_active]


# списко классов для регистрации
admin.site.register(Ico, IcoAdmin)
