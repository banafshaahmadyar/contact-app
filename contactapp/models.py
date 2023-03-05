from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=25, blank=False, null=False)
    lastname = models.CharField(max_length=25, blank=False, null=False)
    number = models.IntegerField()
    email = models.EmailField(max_length=25, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name
