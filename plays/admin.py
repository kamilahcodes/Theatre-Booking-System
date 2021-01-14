from django.contrib import admin
from plays.models import Play, Viewing, Seat

# Register your models here.


class ViewingAdmin(admin.ModelAdmin):

    model = Viewing
    list_display = ['play_name', 'date','time']

admin.site.register(Play)
admin.site.register(Viewing, ViewingAdmin)
admin.site.register(Seat)
