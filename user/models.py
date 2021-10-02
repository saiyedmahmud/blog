from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    

    def __str__(self):
        return self.name                                                   