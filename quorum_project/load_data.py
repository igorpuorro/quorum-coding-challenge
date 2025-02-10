# -*- coding: utf-8 -*-

import csv
import logging
import os
from abc import ABC, abstractmethod
from typing import Dict, Iterable

import django
from django.db.utils import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quorum_project.settings")
django.setup()

from quorum_app.models import Bill, Person, Vote, VoteResult  # noqa: E401


logging.basicConfig(
    filename=os.path.join(".", "load_data.log"),
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class DataSource(ABC):
    @abstractmethod
    def read_data(self, file_path: str) -> Iterable[Dict[str, str]]:
        pass


class StdLibCSVDataSource(DataSource):
    def read_data(self, file_path: str) -> Iterable[Dict[str, str]]:
        csv_filename = os.path.basename(file_path)

        with open(file_path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                yield row


class PandasCSVDataSource(DataSource):
    def read_data(self, file_path: str) -> Iterable[Dict[str, str]]:
        raise NotImplementedError


class PandasJSONDataSource(DataSource):
    def read_data(self, file_path: str) -> Iterable[Dict[str, str]]:
        raise NotImplementedError


class PandasExcelDataSource(DataSource):
    def read_data(self, file_path: str) -> Iterable[Dict[str, str]]:
        raise NotImplementedError


class LoadData:
    data_source: DataSource

    def __init__(self, data_source: DataSource):
        if not data_source:
            raise RuntimeError("DataSource instance is missing!")

        self.data_source = data_source

    def load_legislators(self, file_path: str) -> None:
        filename = os.path.basename(file_path)

        for row in self.data_source.read_data(file_path):
            try:
                Person.objects.create(
                    id=row["id"],
                    name=row["name"]
                )

            except IntegrityError:
                msg = f'{filename}: id={row["id"]}: duplicate id: Skipping row'
                logging.warning(msg=msg)

    def load_bills(self, file_path: str) -> None:
        filename = os.path.basename(file_path)

        for row in self.data_source.read_data(file_path):
            try:
                sponsor = Person.objects.get(id=row["sponsor_id"])

            except Person.DoesNotExist:
                msg = f'{filename}: id={row["id"]}: foreign key sponsor_id={row["sponsor_id"]} not found: Skipping row'
                logging.warning(msg=msg)

                continue

            try:
                Bill.objects.create(
                    id=row["id"],
                    title=row["title"],
                    sponsor=sponsor
                )

            except IntegrityError:
                msg = f'{filename}: id={row["id"]}: duplicate id: Skipping row'
                logging.warning(msg=msg)

    def load_votes(self, file_path: str) -> None:
        filename = os.path.basename(file_path)

        for row in self.data_source.read_data(file_path):
            try:
                bill = Bill.objects.get(id=row["bill_id"])

            except Bill.DoesNotExist:
                msg = f'{filename}: id={row["id"]}: foreign key bill_id={row["bill_id"]} not found: Skipping row'
                logging.warning(msg=msg)

                continue

            try:
                Vote.objects.create(
                    id=row["id"],
                    bill=bill
                )

            except IntegrityError:
                msg = f'{filename}: id={row["id"]}: duplicate id: Skipping row'
                logging.warning(msg=msg)

    def load_vote_results(self, file_path: str) -> None:
        filename = os.path.basename(file_path)

        for row in self.data_source.read_data(file_path):
            try:
                legislator = Person.objects.get(id=row["legislator_id"])
                vote = Vote.objects.get(id=row["vote_id"])

            except Person.DoesNotExist:
                msg = f'{filename}: id={row["id"]}: foreign key legislator_id={row["legislator_id"]} not found: Skipping row'
                logging.warning(msg=msg)

                continue

            except Vote.DoesNotExist:
                msg = f'{filename}: id={row["id"]}: foreign key vote_id={row["vote_id"]} not found: Skipping row'
                logging.warning(msg=msg)

                continue

            try:
                VoteResult.objects.create(
                    id=row["id"],
                    legislator=legislator,
                    vote=vote,
                    vote_type=row["vote_type"]
                )

            except IntegrityError:
                msg = f'{filename}: id={row["id"]}: duplicate id: Skipping row'
                logging.warning(msg=msg)


if __name__ == "__main__":
    csv_data_source: DataSource = StdLibCSVDataSource()
    load_data: LoadData = LoadData(data_source=csv_data_source)

    CSV_DIR_PATH = os.path.join("..", "csv")

    legislators_path = os.path.join(CSV_DIR_PATH, "legislators.csv")
    bills_path = os.path.join(CSV_DIR_PATH, "bills.csv")
    votes_path = os.path.join(CSV_DIR_PATH, "votes.csv")
    vote_results_path = os.path.join(CSV_DIR_PATH, "vote_results.csv")

    load_data.load_legislators(
        file_path=legislators_path
    )
    load_data.load_bills(
        file_path=bills_path
    )
    load_data.load_votes(
        file_path=votes_path
    )
    load_data.load_vote_results(
        file_path=vote_results_path
    )

    print("Data loaded successfully!")
