import json
from django.contrib.gis.geos import Point

import os
from django.conf import settings

from . import models


def build_stops():
    with open(os.path.join(settings.BASE_DIR, 'core/stops.json')) as fh:
        stops = json.load(fh)
    for sj in stops:
        point = Point(x=sj['latlon'][1], y=sj['latlon'][0], srid=settings.GPS_SRID)
        try:
            stop = models.Stop.objects.get(gtfs_stop_id=sj['gtfs_stop_id'])
            stop.point = point
            created = False
        except models.Stop.DoesNotExist:
            stop = models.Stop.objects.create(gtfs_stop_id=sj['gtfs_stop_id'],
                                              name=sj['stop_name'],
                                              point=point
                                              )
            created = True

        stop.save()

