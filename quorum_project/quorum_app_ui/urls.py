# -*- coding: utf-8 -*-

from django.templatetags.static import static
from django.urls import path
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    path(
        "", views.index, name="index"
    ),
    path(
        "favicon.png", RedirectView.as_view(url=static("favicon.png")), name="favicon"
    ),
    path(
        "legislators/", views.legislator_summary, name="legislator_summary"
    ),
    path(
        "bills/", views.bill_summary, name="bill_summary"
    ),
]
