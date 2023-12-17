from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Job(models.Model):    #model class
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    year = models.CharField(null=True,max_length=4)

    def __str__(self):
        return self.summary
