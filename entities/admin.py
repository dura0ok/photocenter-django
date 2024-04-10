from django.contrib import admin

from entities.models import *

admin.site.register(Client)
admin.site.register(OutletTypes)
admin.site.register(Outlet)
admin.site.register(Branch)
admin.site.register(Kiosk)
admin.site.register(PhotoStore)
admin.site.register(Firm)
admin.site.register(Item)
admin.site.register(VendorItem)
admin.site.register(Vendor)
admin.site.register(Storage)
admin.site.register(StorageItem)
admin.site.register(PaperType)
admin.site.register(PaperSize)
admin.site.register(PrintDiscount)
admin.site.register(PrintPrice)