# coding: utf-8

from django.core.urlresolvers import reverse as r
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.template import RequestContext
from django.utils.html import escape
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives



def advertises(request, username):
    user = get_object_or_404(User, username__iexact=username)

    context = RequestContext(request, {
        'page_user': user,
    })

    return render_to_response('reviews/reviews.html', context)


