from django.db import models

BASE_URL = r'http://localhost:8000'

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200, default='' )
    language = models.CharField(max_length=50, default='' )
    price = models.CharField(max_length=10, default='' )
   

    def __str__(self):
        return self.name + ' => ' + self.price