# -*- coding: utf-8 -*-

from django.db.models import Case, Count, IntegerField, QuerySet, When
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Bill, Person, Vote, VoteResult
from .serializers import BillSerializer, BillSummarySerializer, LegislatorSummarySerializer, PersonSerializer, VoteSerializer, VoteResultSerializer


class BillViewSet(ModelViewSet):
    http_method_names: list[str] = ["delete", "get", "post", "put"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset: QuerySet[Bill.objects] = Bill.objects.all()
    serializer_class: QuerySet[BillSerializer] = BillSerializer


class PersonViewSet(ModelViewSet):
    http_method_names: list[str] = ["delete", "get", "post", "put"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset: QuerySet[Person.objects] = Person.objects.all()
    serializer_class: QuerySet[PersonSerializer] = PersonSerializer


class VoteViewSet(ModelViewSet):
    http_method_names: list[str] = ["delete", "get", "post", "put"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset: QuerySet[Vote.objects] = Vote.objects.all()
    serializer_class: QuerySet[VoteSerializer] = VoteSerializer


class VoteResultViewSet(ModelViewSet):
    http_method_names: list[str] = ["delete", "get", "post", "put"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset: QuerySet[VoteResult.objects] = VoteResult.objects.all()
    serializer_class: QuerySet[VoteResultSerializer] = VoteResultSerializer


class BillSummaryView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BillSummarySerializer
    queryset = (
        Bill.objects.annotate(
            supporters=Count(
                Case(
                    When(vote__voteresult__vote_type=1, then=1),
                    output_field=IntegerField()
                )
            ),
            opposers=Count(
                Case(
                    When(vote__voteresult__vote_type=2, then=1),
                    output_field=IntegerField()
                )
            )
        )
    )


class LegislatorSummaryView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LegislatorSummarySerializer
    queryset = (
        Person.objects.annotate(
            supported_bills=Count(
                Case(
                    When(voteresult__vote_type=1, then=1),
                    output_field=IntegerField()
                )
            ),
            opposed_bills=Count(
                Case(
                    When(voteresult__vote_type=2, then=1),
                    output_field=IntegerField()
                )
            ),
        )
    )
