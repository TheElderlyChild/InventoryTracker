from django.contrib import admin
from .models import Item, Location, StorageAssignment

# Register your models here.
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(StorageAssignment)
