# -*- coding: utf-8 -*-

from django.db.models import CASCADE, CharField, ForeignKey, IntegerField, Model


class Person(Model):
    id: IntegerField = IntegerField(primary_key=True)
    name: CharField = CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Bill(Model):
    id: IntegerField = IntegerField(primary_key=True)
    title: CharField = CharField(max_length=100)
    sponsor: ForeignKey = ForeignKey(Person, on_delete=CASCADE)

    def __str__(self):
        return str(self.title)


class Vote(Model):
    id: IntegerField = IntegerField(primary_key=True)
    bill: ForeignKey = ForeignKey(Bill, on_delete=CASCADE)

    def __str__(self):
        return f"Vote {self.id} on {self.bill.title}"


class VoteResult(Model):
    VOTE_TYPES: tuple[tuple[int, str], ...] = (
        (1, "Yea"),
        (2, "Nay")
    )

    id: IntegerField = IntegerField(primary_key=True)
    legislator: ForeignKey = ForeignKey(Person, on_delete=CASCADE)
    vote: ForeignKey = ForeignKey(Vote, on_delete=CASCADE)
    vote_type: IntegerField = IntegerField(choices=VOTE_TYPES)

    def __str__(self):
        return f'{self.legislator.name} voted {"Yea" if self.vote_type == 1 else "Nay"}'
