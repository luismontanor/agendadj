from django.contrib import admin

from .models import Person, Hobbie, Reunion

admin.site.register(Person)
admin.site.register(Hobbie)
admin.site.register(Reunion)
