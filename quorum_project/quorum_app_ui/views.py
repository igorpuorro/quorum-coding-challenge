# -*- coding: utf-8 -*-

import requests
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


API_BASE_URL = "http://localhost:8000/api/v1/quorum-app-ui"
REQUEST_TIMEOUT = 5


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request, "index.html",
    )


def legislator_summary(request: HttpRequest) -> HttpResponse:
    url = f"{API_BASE_URL}/legislators/summary/"
    response = requests.get(
        url=url,
        timeout=REQUEST_TIMEOUT
    ).json()

    return render(
        request=request,
        template_name="legislator_summary.html",
        context={"legislators": response}
    )


def bill_summary(request: HttpRequest) -> HttpResponse:
    url = f"{API_BASE_URL}/bills/summary/"
    response = requests.get(
        url=url,
        timeout=REQUEST_TIMEOUT
    ).json()

    return render(
        request=request,
        template_name="bill_summary.html",
        context={"bills": response}
    )
