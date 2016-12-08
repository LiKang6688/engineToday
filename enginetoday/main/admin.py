from django.contrib import admin
from .models import Announce, User, Media

# Register your models here.
admin.site.register(User)
admin.site.register(Announce)
admin.site.register(Media)

