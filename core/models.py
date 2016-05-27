from django.contrib.gis.db import models
from django.core.urlresolvers import reverse


class Stop(models.Model):
    gtfs_stop_id = models.IntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=50)
    point = models.PointField()
    parkings = models.GeometryCollectionField(null=True, blank=True)

    objects = models.GeoManager()

    def get_absolute_url(self):
        return reverse('core:stop', args=(self.id,))

    def __str__(self):
        return self.name
