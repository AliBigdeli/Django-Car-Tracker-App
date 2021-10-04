from django.contrib import admin

from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    list_display = ["user", "url", "title"]
    search_fields = ["user", "url", "title"]
    list_filter = ("user",)


admin.site.register(Link, LinkAdmin)
