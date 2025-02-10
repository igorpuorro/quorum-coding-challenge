# -*- coding: utf-8 -*-

from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from .views import BillSummaryView, BillViewSet, PersonViewSet, LegislatorSummaryView, VoteViewSet, VoteResultViewSet


router = DefaultRouter()
router.register(prefix=r"bill", viewset=BillViewSet)
router.register(prefix=r"person", viewset=PersonViewSet)
router.register(prefix=r"vote", viewset=VoteViewSet)
router.register(prefix=r"vote-result", viewset=VoteResultViewSet)

urlpatterns = [
    path(
        "api/schema/", SpectacularAPIView.as_view(), name="schema"
    ),
    path(
        "api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
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
