# urls.py (the URL configuration)

from django.conf.urls import url, include


from enginetoday.main.views import *

app_name = 'main'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
    url(r'^error/$', ErrorView.as_view(), name='error'),
    url(r'^account/confirm-email/$', ConfirmemailView.as_view(), name='confirm-email'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^account/create-account/$', CreateaccountView.as_view(), name='create-account'),
    url(r'^account/forgot-password/$', ForgotpasswordView.as_view(), name='forgot-password'),
    url(r'^account/profile/$', ProfileView.as_view(), name='Profile'),


    url(r'^account/register/$', RegisterView.as_view(), name='register'),
    url(r'^account/signin/$', SigninView.as_view(), name='signin'),


    url(r'^account/thanks-for-activating-account/$', ThanksforactivatingaccountView.as_view(),
        name='thanks-for-activating-account'),

    url(r'^account/thanks-for-creating-account/$', ThanksforcreatingaccountView.as_view(),
        name='thanks-for-creating-account'),

    url(r'^cars/cars/$', CarsView.as_view(), name='cars'),

    url(r'^cars/cars-detail/$', CarsdDetailView.as_view(), name='cars-detail'),

    url(r'^sell/saved-sell/$', SavedsellView.as_view(), name='saved-sell'),
    url(r'^sell/sell/$', SellView.as_view(), name='sell'),

    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^edit/create/$', AnnounceCreate.as_view(), name='announce-create'),
    url(r'^edit/update/(?P<pk>\d+)/$', AnnounceUpdate.as_view(), name='announce-update'),
    url(r'^edit/delete/(?P<pk>\d+)/$', AnnounceDelete.as_view(), name='announce-delete'),

    # url(r'^accounts/', include('django.contrib.auth.urls'))
    # url(r'^(?P<announce_id>[0-9]+)$', views.detail, name='cars-detail'),
]


