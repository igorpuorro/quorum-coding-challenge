import subprocess
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Automate setup: migrate database, load data, create superuser, set password, and generate DRF token."

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS("Running migrations...")
        )
        call_command("migrate")

        self.stdout.write(
            self.style.SUCCESS("Loading data...")
        )
        try:
            subprocess.run(["python", "load_data.py"], check=True)
        except subprocess.CalledProcessError as e:
            self.stderr.write(
                self.style.ERROR(f"Error loading data: {e}")
            )

        self.stdout.write(
            self.style.SUCCESS("Creating superuser...")
        )
        User = get_user_model()
        if not User.objects.filter(username="quorum").exists():
            User.objects.create_superuser(
                "quorum", "quorum@example.com", "qwerty"
            )
            self.stdout.write(
                self.style.SUCCESS("Superuser created successfully!")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Superuser already exists.")
            )

        self.stdout.write(
            self.style.SUCCESS("Generating DRF token...")
        )
        try:
            call_command("drf_create_token", "quorum")
        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"Error generating DRF token: {e}")
            )

        self.stdout.write(
            self.style.SUCCESS("Setup completed successfully!")
        )
