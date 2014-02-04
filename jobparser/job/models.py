from django.db import models

class Job(models.Model):
    company_name = models.CharField(max_length=300, blank=True, null=True)
    company_id = models.CharField(max_length=300, blank=True, null=True)
    source = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null = True)
    qualification = models.TextField(blank=True, null = True)
    all_text = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=600, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    posting_date = models.DateTimeField(null=True, blank=True)
    source_joburl = models.CharField(max_length=900, blank=True)
    company_joburl = models.CharField(max_length=900, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

class ZCTA(models.Model):
    postal_code = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.CharField(max_length=300, blank=True, null=True)
    longitude = models.CharField(max_length=300, blank=True, null=True)

class STAB(models.Model):
    state = models.CharField(max_length=300, blank=True, null=True)
    abbreviation = models.CharField(max_length=2, blank=True, null=True)

class Geo(models.Model):
    city = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=300, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)