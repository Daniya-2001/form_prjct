from django.db import models


# Create your models here.

class UserForm(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField()
    Phone = models.IntegerField()
    About = models.TextField()
    
    def __str__(self):
        return self.Name
    

