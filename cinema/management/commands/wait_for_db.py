import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 seconds...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))

        # for i in range(15):
        #     db_conn = connections["default"]
        #     if db_conn:
        #         self.stdout.write(self.style.SUCCESS("Database available!"))
        #     if not db_conn and attempt < 3:
        #         self.stdout.write(f"Connecting to database. Attempt: {attempt}/10")
        #         time.sleep(1)
        #     else:
        #         raise OperationalError(self.stdout.write("Database unavailable!!!"))
