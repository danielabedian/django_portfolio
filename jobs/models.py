from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=300)
    
    subtitle1 = models.CharField(max_length=30, default='', blank=True)
    picture1 = models.ImageField(upload_to='images/', blank=True)
    experience1 = models.CharField(max_length=1000, default='', blank=True)

    subtitle2 = models.CharField(max_length=30, default='', blank=True)
    picture2 = models.ImageField(upload_to='images/', blank=True)
    experience2 = models.CharField(max_length=1000, default='', blank=True)

    subtitle3 = models.CharField(max_length=30, default='', blank=True)
    picture3 = models.ImageField(upload_to='images/', blank=True)
    experience3 = models.CharField(max_length=1000, default='', blank=True)



    def __str__(self):
        return self.summary