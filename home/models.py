from django.db import models
import os

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=50 , null=True  )
    content = models.TextField(  null=True )
    image = models.ImageField(upload_to='photos/%y/%m/%d' , null=True  )

    def __str__(self):
        return self.name  # Function to make the images in the database with its name


