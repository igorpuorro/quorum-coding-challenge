# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BillSummaryView, BillViewSet, PersonViewSet, LegislatorSummaryView, VoteViewSet, VoteResultViewSet


router = DefaultRouter()
router.register(prefix=r"bill", viewset=BillViewSet)
router.register(prefix=r"person", viewset=PersonViewSet)
router.register(prefix=r"vote", viewset=VoteViewSet)
router.register(prefix=r"vote-result", viewset=VoteResultViewSet)

urlpatterns = [
    path(
        "api/v1/", include(router.urls)
    ),
    path(
        "api/v1/",
        include([
            path(
                "bill-summary/",
                BillSummaryView.as_view(),
                name="bill-summary"
            ),
            path(
                "legislator-summary/",
                LegislatorSummaryView.as_view(),
                name="legislator-summary"
            ),
        ])
    ),
]
