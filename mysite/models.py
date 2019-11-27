from django.db import models

class Bands(models.Model):
    band_name = models.CharField(max_length = 120)
    fans = models.CharField(max_length = 10)
    formed = models.CharField(max_length = 4)
    origin = models.CharField(max_length = 50)
    split = models.CharField(max_length = 4)
    style = models.CharField(max_length = 35)

class MetalBands(models.Model):
    band_name = models.TextField()
    fans = models.IntegerField()
    formed = models.IntegerField()
    origin = models.TextField()
    split = models.TextField()
    style = models.TextField()

class Meta:
    ordering = ['created']