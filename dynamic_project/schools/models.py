from django.db import models

# Create your models here.
class schools(models.Model):
    name = models.CharField(max_length=100, unique = True)
    location = models.CharField(max_length=100)
    established_year = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True, unique = True)
    email = models.EmailField(blank=True, null=True, unique = True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique = True)

