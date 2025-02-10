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


drf_spectacular_urlpatterns = [
    path(
        "schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui"
    ),
]

model_view_set_urlpatterns = [
    path(
        "", include(router.urls)
    ),
]

quorum_app_ui_urlpatterns = [
    path(
        "bills/summary/",
        BillSummaryView.as_view(),
        name="bill-summary"
    ),
    path(
        "legislators/summary/",
        LegislatorSummaryView.as_view(),
        name="legislator-summary"
    ),
]

urlpatterns = [
    path("api/v1/", include([
        path("quorum-app-ui/", include(quorum_app_ui_urlpatterns)),
        path("model-view-set/", include(model_view_set_urlpatterns)),
    ])),
    path("api/", include(drf_spectacular_urlpatterns)),
]
