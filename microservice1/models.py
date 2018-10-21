from django.db import models


class Pet(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    spaces = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    ages = models.IntegerField(null=True)
    vaccination = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=100)
