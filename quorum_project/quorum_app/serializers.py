# -*- coding: utf-8 -*-

from typing import Type

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Person, Bill, Vote, VoteResult


class PersonSerializer(ModelSerializer):
    class Meta:
        model: Type[Person] = Person
        fields: str = "__all__"


class BillSerializer(ModelSerializer):
    sponsor: PersonSerializer = PersonSerializer(read_only=True)
    sponsor_id: PrimaryKeyRelatedField = PrimaryKeyRelatedField(
        queryset=Person.objects.all(), source="sponsor", write_only=True
    )

    class Meta:
        model: Type[Bill] = Bill
        fields: str = "__all__"


class VoteSerializer(ModelSerializer):
    bill: BillSerializer = BillSerializer(read_only=True)
    bill_id: PrimaryKeyRelatedField = PrimaryKeyRelatedField(
        queryset=Bill.objects.all(), source="bill", write_only=True
    )

    class Meta:
        model: Type[Vote] = Vote
        fields: str = "__all__"


class VoteResultSerializer(ModelSerializer):
    legislator: PersonSerializer = PersonSerializer(read_only=True)
    legislator_id: PrimaryKeyRelatedField = PrimaryKeyRelatedField(
        queryset=Person.objects.all(), source="legislator", write_only=True
    )
    vote: VoteSerializer = VoteSerializer(read_only=True)
    vote_id: PrimaryKeyRelatedField = PrimaryKeyRelatedField(
        queryset=Vote.objects.all(), source="vote", write_only=True
    )

    class Meta:
        model: Type[VoteResult] = VoteResult
        fields: str = "__all__"
