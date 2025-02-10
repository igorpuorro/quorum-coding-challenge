# -*- coding: utf-8 -*-

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Person, Bill, Vote, VoteResult


class PersonModelDatabaseFetchTests(TestCase):
    fixtures = ["model_person_data.json"]

    def test_fetch_person_from_database(self):
        """
        Test fetching data directly from the database for the Person model.
        """

        person = Person.objects.get(id=15318)
        self.assertEqual(person.name, "Rep. Andrew Garbarino (R-NY-2)")


class ModelTests(TestCase):
    fixtures = ["model_tests.json"]

    def test_person_model(self):
        """
        Test the Person model by fetching a person by ID and
        asserting the expected name.
        """

        person = Person.objects.get(id=15318)
        self.assertEqual(person.name, "Rep. Andrew Garbarino (R-NY-2)")

    def test_bill_model(self):
        """
        Test the Bill model by fetching a bill by ID and
        asserting the expected title and sponsor.
        """

        bill = Bill.objects.get(id=2952375)
        self.assertEqual(bill.title, "H.R. 5376: Build Back Better Act")
        self.assertEqual(bill.sponsor.name, "Rep. Andrew Garbarino (R-NY-2)")

    def test_vote_model(self):
        """
        Test the Vote model by fetching a vote by ID and
        asserting the expected bill title.
        """

        vote = Vote.objects.get(id=3321166)
        self.assertEqual(vote.bill.title, "H.R. 5376: Build Back Better Act")

    def test_vote_result_model(self):
        """
        Test the VoteResult model by fetching a vote result by ID and
        asserting the expected legislator name, bill title, vote type,
        and string representation.
        """

        vote_result = VoteResult.objects.get(id=92516368)
        self.assertEqual(
            vote_result.legislator.name,
            "Rep. Andrew Garbarino (R-NY-2)"
        )
        self.assertEqual(
            vote_result.vote.bill.title,
            "H.R. 5376: Build Back Better Act"
        )
        self.assertEqual(
            vote_result.vote_type,
            1
        )
        self.assertEqual(
            str(vote_result),
            "Rep. Andrew Garbarino (R-NY-2) voted Yea"
        )


class BillSummaryViewTests(TestCase):
    fixtures = [
        "model_bill_data.json",
        "model_person_data.json",
        "model_vote_data.json",
        "model_voteresult_data.json"
    ]

    def setUp(self):
        self.client = APIClient()
        self.url = reverse(viewname="bill-summary")

    def test_bill_summary_view(self):
        """
        Test the BillSummaryView to ensure it returns the correct bill data,
        including the number of supporters and opposers for each bill.
        """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        bill_data = response.data[0]

        self.assertEqual(
            bill_data["id"], 2952375
        )
        self.assertEqual(
            bill_data["title"], "H.R. 5376: Build Back Better Act"
        )
        self.assertEqual(
            bill_data["supporters"], 1
        )
        self.assertEqual(
            bill_data["opposers"], 0
        )
