from django.db import models

# Create your models here.
from django.db import models


class school(models.Model):
    date = models.DateField()
    time = models.TimeField()
    school_name = models.CharField(max_length=100)

    def __str__(self):		   
        return ' {}'.format(self.school_name)

class status(models.Model):
    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(max_length=100)

    def __str__(self):
        return ' {}'.format(self.mode)

class slip(models.Model):
    school_name = models.ForeignKey(school, on_delete=models.CASCADE)
    mode =  models.ForeignKey(status, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    photo = models.ImageField(upload_to='un_checked/' , null=True , blank=True )

    def __str__(self):
        return ' {} {} {} {}'.format(self.school_name,self.mode,self.date,self.time)


