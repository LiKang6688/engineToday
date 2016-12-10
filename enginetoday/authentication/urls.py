from django.conf.urls import patterns, include, url


urlpatterns = patterns('enginetoday.authentication.views',
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^signin/$', 'signin', name='signin'),
    url(r'^signout/$', 'signout', name='signout'),
    url(r'^reset/$', 'reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'reset_confirm', name='password_reset_confirm'),
    url(r'^success/$', 'success', name='success'),

    # url(r'^(?P<username>[^/]+)/$', 'reviews.views.reviews', name='reviews'),
)



