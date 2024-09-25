from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

