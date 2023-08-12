from django.db import models
from django.utils import timezone

# Create your models here.
class Animal1(models.Model):
    name = models.CharField(max_length=200)
    girraph = models.ImageField(upload_to="animal1")
    login_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Animal1"


class SpecialServices(models.Model):
    icons = models.ImageField(upload_to="icons")
    services = models.CharField(max_length=20)
    description = models.TextField()


    def __str__(self):
        return self.services
    
    class Meta:
        verbose_name_plural = "SpecialServices"



class Gallery(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Gallery"



