import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps
from datetime import datetime

class Command(BaseCommand):
    help = "Export data from Student model to a csv file"
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')
    
    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        if not model:
            self.stderr.write(f"Model {model_name} not found")
            return
        
        #feth the data from database
        data = model.objects.all()
        
        #print(students)
        
        #define the csv
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_path = f"data/exported_{model_name}_data_{timestamp}.csv"
        
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            #we want to print fileds name of the model that we are trying to import
            writer.writerow([field.name for field in model._meta.fields])
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
                
        self.stdout.write(self.style.SUCCESS('Data Exported successfully!'))
            
        
        