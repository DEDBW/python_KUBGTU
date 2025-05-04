# store/admin.py
from django.contrib import admin
from .models import Zhanr, Izdatel, Platforma, Razrabotchik, Strana, Yazyk, Igra, ObnovlenieIgry, Polzovatel, IgryPoPlatformam, IgryPoYazykam, SpisokDruzey

class IgraAdmin(admin.ModelAdmin):
    fields = (
        'nazvanie',
        'data_vyhoda',
        'tsena',
        'vozrastnoy_reyting',
        'razmer_igry',
    )

admin.site.register(Zhanr)
admin.site.register(Izdatel)
admin.site.register(Platforma)
admin.site.register(Razrabotchik)
admin.site.register(Strana)
admin.site.register(Yazyk)
admin.site.register(Igra, IgraAdmin)
admin.site.register(ObnovlenieIgry)
admin.site.register(Polzovatel)