#Model for the database table
from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):  #magic method defines what should be printed when the print function is used
        return f"{self.first_name} {self.last_name}"




