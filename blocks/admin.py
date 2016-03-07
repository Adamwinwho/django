from django.contrib import admin

# Register your models here.
from models import Blocks

class BlocksAdmin(admin.ModelAdmin):
    list_display = ("name","desc","owner","last_update_timestamp")
    list_filter = ("name",)

admin.site.register(Blocks,BlocksAdmin)
