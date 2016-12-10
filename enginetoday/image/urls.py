try:  # pre 1.6
    from django.conf.urls.defaults import url, patterns
except ImportError:
    from django.conf.urls import url, patterns

urlpatterns = patterns(
    'enginetoday.image.views',
    url(
        '^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
        'enginetoday.image.views.ajaximage',
        name='image'
    ),
)
