from django.contrib import admin

from entities.models import *

admin.site.register(Client)
admin.site.register(OutletTypes)
admin.site.register(Outlets)
admin.site.register(Branch)