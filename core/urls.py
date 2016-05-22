from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stops/$', views.StopList.as_view(), name='stops'),
    url(r'^stops/(?P<pk>\d+)/$', views.StopDetail.as_view(), name='stop'),
]
