from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def u(obj):
    return mark_safe('<a href="{}">{}</a>'.format(obj.get_absolute_url(), str(obj)))


@register.filter()
def stop_map_init(stop):
    return 'init_stop_map_{}'.format(stop.id)


@register.filter()
def map_name(stop):
    return 'map_{}'.format(stop.id)


@register.filter()
def format_dist(dist):
    m = dist.m
    if m < 1000:
        return '{} m'.format(int(m))
    else:
        return '{:.3f} km'.format(m/1000.0)

