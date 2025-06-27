from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254, default="")
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=15, default="") 
    desc = models.TextField(default="")
    date = models.DateField()

    def __str__(self):
        return self.name  