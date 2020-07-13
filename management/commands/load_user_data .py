from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import ID, Name
from pytz import UTC

]

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from user_data.csv into our User mode"

    def handle(self, *args, **options):
        if Name.objects.exists() or ID.objects.exists():
            print('User data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating user data")
        for vaccine_name in VACCINES_NAMES:
            vac = Vaccine(name=vaccine_name)
            vac.save()
        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./pet_data.csv')):
            ID = ID()
            Name = row['Name]
            RoleID = row['RoleID']

