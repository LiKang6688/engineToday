from django.shortcuts import render
from django.views.generic import FormView

from enginetoday.advertise.forms import AjaxImageUploadForm


class MyView(FormView):
    template_name = 'advertise/form.html'
    form_class = AjaxImageUploadForm
