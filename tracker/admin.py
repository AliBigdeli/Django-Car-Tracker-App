from django.contrib import admin

from .models import Device,Coordinate

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "token","user", "created_date"]
    search_fields = ["name", "token"]
    list_filter = ("user",)

class CoordinateAdmin(admin.ModelAdmin):
    list_display = ["lat", "lon","device", "created_date"]
    search_fields = ["device"]
    list_filter = ("device",)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
