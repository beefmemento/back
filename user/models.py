from django.db import models
from django.contrib.auth.models import AbstractUser

class Defaultuser(AbstractUser):
    name = models.CharField(max_length=255, blank=False)
    nickname = models.CharField(max_length=255, blank=False)

    subject1 = models.CharField(max_length=255, null=True, blank=True)
    subject2 = models.CharField(max_length=255, null=True, blank=True)
    subject3 = models.CharField(max_length=255, null=True, blank=True)
    subject4 = models.CharField(max_length=255, null=True, blank=True)
    subject5 = models.CharField(max_length=255, null=True, blank=True)
    subject6 = models.CharField(max_length=255, null=True, blank=True)
    subject7 = models.CharField(max_length=255, null=True, blank=True)
    grades = models.CharField(max_length=255, null=True, blank=True)
