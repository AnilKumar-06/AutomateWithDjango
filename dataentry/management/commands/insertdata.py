from django.core.management.base import BaseCommand
from dataentry.models import Student



class Command(BaseCommand):
    help ="It will insert data into database"
    
    def handle(self, *args, **kwargs):
        dataset = [
            {
                'roll_no': '102',
                'name': 'Alice',
                'age': 22,
            },
            {
                'roll_no': '103',
                'name': 'Bob',
                'age': 23,
            },
            {
                'roll_no': '104',
                'name': 'Charlie',
                'age': 21,
            },
            {
                'roll_no': '105',
                'name': 'David',
                'age': 24,
            },
            {
                'roll_no': '106',
                'name': 'Eve',
                'age': 20,
            },
            {
                'roll_no': '107',
                'name': 'Frank',
                'age': 22,
            },
            {
                'roll_no': '108',
                'name': 'Grace',
                'age': 23,
            },
            {
                'roll_no': '109',
                'name': 'Heidi',
                'age': 21,
            },
           
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Record with roll_no {roll_no} already exists."))
        
        
        self.stdout.write(self.style.SUCCESS("Data Inserted Successfully."))