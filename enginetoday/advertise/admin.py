from django.contrib import admin
from enginetoday.advertise.models import Advertise


class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['admin_thumb', '__str__', '__unicode__', 'url', 'path']

    def admin_thumb(self, obj):
        return '<img src="{0}" />'.format(obj.thumbnail.url)
    admin_thumb.allow_tags = True
    admin_thumb.short_description = 'Kitten Image'


admin.site.register(Advertise, AdvertiseAdmin)
