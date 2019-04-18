from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse, redirect

# Create your models here.


class Record(models.Model):
    OB_no = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ID_no = models.IntegerField()
    contacts = models.IntegerField()
    area_of_stay = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date_and_time = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('pcapp:index')

    def __str__(self):
        return self.first_name


class Crime(models.Model):
    #ID_no = models.IntegerField()
    record = models.ForeignKey(Record, on_delete=models.PROTECT)
        #criminal = models.ForeignKey(Criminal, on_delete=models.PROTECT, default=1)
    nature_of_crime = models.CharField(max_length=50)
    description_of_crime = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    investigating_officer = models.CharField(max_length=50)
    section_of_CPC_offence = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('pcapp:crimelist')

    def __str__(self):
        return self.nature_of_crime


class Criminal(models.Model):
    crime = models.ForeignKey(Crime, on_delete=models.PROTECT, default=1)
    picture = models.FileField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ID_no = models.IntegerField()
    nationality = models.CharField(max_length=50)
    offences = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('pcapp:criminals')

    def __str__(self):
        return self.first_name


class Staff(models.Model):
    picture = models.FileField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    pc_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('pcapp:staffs')

    def __str__(self):
        return self.first_name



