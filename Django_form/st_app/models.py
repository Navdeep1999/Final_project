from django.db import models

# Create your models here.
from django.db import models
class Degree(models.Model):
    title = models.CharField(max_length=25)
    branch = models.CharField(max_length=50)
    
    def __str__(self):
        template = '{0.title} {0.branch}'
        return template.format(self)
    
class Students(models.Model):
        name = models.CharField(max_length=45)
        roll_number = models.CharField(max_length=25)
        year = models.IntegerField(default = 1)
        dob = models.DateField('date of birth')
        
        
        def __str__(self):
            temp= '{0.name} {0.roll_number} {0.year} {0.dob}'
            return temp.format(self)

        
    
    