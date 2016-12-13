from django.conf.urls import patterns, url

from enginetoday.advertise.views import MyView


urlpatterns = patterns('',
    url('', MyView.as_view(), name='form'),
)
