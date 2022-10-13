from django.db import models

# Create your models here.
from django.db import models



class Snippet(models.Model):
    userid = models.IntegerField(default=0)
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    companyname = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    zip = models.IntegerField(default=0)
    email = models.CharField(max_length=100, blank=True, default='')
    web = models.CharField(max_length=100, blank=True, default='')

    