from django.db import models
from multiselectfield import MultiSelectField
GENDER_CHOICES= [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('others', 'others')
    ]

SPORT_CHOICES= [
    ('Cricket', 'Cricket'),
    ('Kabaddi', 'Kabbaddi'),
    ('Badmintion', 'Badmintion'),
    ('Chess', 'Chess'),
    ('Volleyball', 'Volleyball')
    ]
# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phone= models.CharField(max_length=120)
    gender=models.CharField(max_length=120,choices=GENDER_CHOICES)

    sport=MultiSelectField(max_length=120,choices =SPORT_CHOICES)
    address= models.CharField(max_length=120)
    date= models.DateTimeField()



    def __str__(self):
        return self.name