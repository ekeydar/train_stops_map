from django.conf import settings
from django.contrib.gis.db.models.functions import Distance, Centroid
from django.contrib.gis.geos import Point
from django.db.models import Func
from django.views.generic import ListView, DetailView

from . import models


class StopList(ListView):
    model = models.Stop

    @property
    def sort_by_distance(self):
        return self.sort_by == 'distance'

    @property
    def sort_by_north(self):
        return self.sort_by == 'north'

    def prepare(self):
        request = self.request
        self.sort_by = request.GET.get('sort_by', 'north')
        if self.sort_by_distance:
            self.location = Point(float(self.request.GET['lon']),
                                  float(self.request.GET['lat']),
                                  srid=settings.GPS_SRID)
        else:
            self.location = None

    def get_context_data(self, **kwargs):
        ctx = super(StopList, self).get_context_data(**kwargs)
        ctx['sort_by'] = self.sort_by
        ctx['location'] = self.location
        return ctx

    def get_queryset(self):
        self.prepare()
        qs = super(StopList, self).get_queryset()
        if self.sort_by_distance:
            qs = qs.annotate(distance=Distance('point', self.location)).order_by('distance')
        elif self.sort_by_north:
            qs = qs.extra(select={'lat':'ST_Y(point)'}).order_by('-lat')

        #qs = qs[0:3]
        return qs


class StopDetail(DetailView):
    model = models.Stop
