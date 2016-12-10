from django import forms

from enginetoday.image.widgets import AjaxImageWidget


class AjaxImageUploadForm(forms.Form):
    images = forms.FileField(widget=AjaxImageWidget())