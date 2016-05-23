from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Stop


@admin.register(Stop)
class StopAdmin(LeafletGeoAdmin):
    pass

