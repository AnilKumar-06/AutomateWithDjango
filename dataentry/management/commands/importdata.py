from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
from django.apps import apps
import csv

class Command(BaseCommand):
    help = "Import data from a CSV file"
    
    def add_arguments(self, parser):
        
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")
        parser.add_argument('model_name', type=str, help="Name of the model to import data into")
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        #Search for the model across all installed apps
        for app_config in apps.get_app_configs():
            #Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching if model is found
            except LookupError:
                continue #continue searching in other apps
        
        if not model:
            raise CommandError(f"Model '{model_name} not found in any app")
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Importing data successfully from CSV file..."))