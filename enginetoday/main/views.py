# views.py (the business logic)
from django.http import Http404
# from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views.generic import View
from django.template import loader

from enginetoday.main.models import *
from enginetoday.main.models import User, Announce, Media


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class GalleryView(generic.ListView):
    template_name = 'main/gallery.html'
    context_object_name = 'announceList'
    menuActiveGallery = 1

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ErrorView(generic.ListView):
    template_name = 'main/error.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ConfirmemailView(generic.ListView):
    template_name = 'main/account/confirm-email.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ContactView(generic.ListView):
    template_name = 'main/contact.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class CreateaccountView(generic.ListView):
    template_name = 'main/account/create-account.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ForgotpasswordView(generic.ListView):
    template_name = 'main/account/forgot-password.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ProfileView(generic.ListView):
    template_name = 'main/account/profile.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class RegisterView(generic.ListView):
    template_name = 'main/account/register.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class SigninView(generic.ListView):
    template_name = 'main/account/signin.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ThanksforactivatingaccountView(generic.ListView):
    template_name = 'main/account/thanks-for-activating-account.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class ThanksforcreatingaccountView(generic.ListView):
    template_name = 'main/account/thanks-for-creating-account.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class CarsView(generic.ListView):
    template_name = 'main/cars/cars.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class CarsdDetailView(generic.DetailView):
    model = Announce
    template_name = 'main/cars/cars-detail.html'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class SavedsellView(generic.ListView):
    template_name = 'main/sell/saved-sell.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


class SellView(generic.ListView):
    template_name = 'main/sell/sell.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return Announce.objects.all().order_by("-submit_time")


# class AdvertisePublishView(FormView):
#     template_name = 'main/sell/sell.html'
#     form_class = AdvertisePublishForm
#     success_url = '/saved-sell/'
#
#     def form_valid(self, form):
#         form.save(self.request.user.username)
#         return super(AdvertisePublishView, self).form_valid(form)


class DetailView(generic.DetailView):
    model = Announce
    local_fields = Announce._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]
    context_object_name = 'announceDetail'


class AnnounceCreate(CreateView):
    model = Announce
    local_fields = Announce._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]


class AnnounceUpdate(UpdateView):
    model = Announce
    local_fields = Announce._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]


class AnnounceDelete(DeleteView):
    model = Announce
    local_fields = Announce._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]
    # success_url = reverse_lazy('main:index')


class UserIndexView(generic.ListView):
    template_name = 'main/gallery.html'
    context_object_name = 'announceList'

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(generic.DetailView):
    model = User
    local_fields = User._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]
    context_object_name = 'announceDetail'


class UserCreate(CreateView):
    model = User
    local_fields = User._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]


class UserUpdate(UpdateView):
    model = User
    local_fields = User._meta.local_fields
    fields = [one_field.name for one_field in local_fields][2:]


class UserceDelete(DeleteView):
    model = User
    # success_url = reverse_lazy('main:index')


# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'main/account/register.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.Post)
#
#         if form.is_valid():
#
#             user = form.save(commit=false)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User objects if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('music:index')
#
#         return render(request, self.template_name, {'form': form})


# def index(request):
#     all_announce = Announce.objects.all()
#     template = loader.get_template('main/cars/cars')
#     context = {
#         'all_announce': all_announce,
#     }
#     return render(request, 'main/cars/cars', {'all_announce': all_announce})
#
#
# def detail(request, announce_id):
#     try:
#         announce = Announce.objects.get(pk=announce_id)
#     except Announce.DoesNotExist:
#         raise Http404("Car does not exist")
#     return render(request, 'main/cars/cars-detail', {'announce': announce})
